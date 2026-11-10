#!/usr/bin/env python3
"""Phantom Blade Zero (PC Steam) save tool: read and edit PBZSaveGame.sav offline.

File format (PBZS v3, documented by the community):
  header  "PBZS" u8 version=3, u8 flags=1, u16 slot_count, u32 directory_block_size
  then one sealed directory block, then one sealed block per slot.
  sealed block = "PBZS\\x01\\x01\\x00\\x00" + 12-byte nonce + 16-byte GCM tag + ciphertext
  cipher = AES-256-GCM; the directory plaintext starts with a copy of the 12-byte header,
  then per slot: u16 name_len, name, u8 algorithm (0 none, 1 zlib, 2 Oodle Kraken),
  u8 flag=1, u32 raw_size, u32 offset, u32 block_size.
  Each slot decompresses to UTF-8 JSON.

The AES key is not stored here. It sits in platform/steam/PBZ.exe as two 32-byte halves
that XOR into the key, right after a UTF-16 anchor string; this tool finds it and only
accepts a candidate that authenticates the save's directory block. Key location method
and format notes come from PBZ-Editor (github.com/qry6868/PBZ-Editor, MIT).

Oodle decoding uses codec/ (a tiny wrapper over the MIT oozextract crate). Writing never
needs an Oodle encoder: edited slots are stored as Oodle "stored" blocks, which the game
reads like any other Kraken stream. Untouched slots keep their original ciphertext.

Writes always: refuse while PBZ.exe runs, refuse if the slot JSON does not re-serialise
byte for byte, back up outside the Steam Cloud folder, write atomically, then decrypt the
written file again and compare every slot.
"""
import argparse
import ctypes
import glob
import json
import mmap
import os
import shutil
import struct
import subprocess
import sys
import time
import zlib

try:
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
    from cryptography.exceptions import InvalidTag
except ImportError:
    raise SystemExit("Missing dependency: python3-cryptography (sudo apt install python3-cryptography)")

HERE = os.path.dirname(os.path.abspath(__file__))
SEAL = b"PBZS\x01\x01\x00\x00"
KEY_ANCHOR = "sealed but block is PLAINTEXT".encode("utf-16-le") + b"\0\0"
MAX_SLOT = 64 * 1024 * 1024
STORED_CHUNK = 0x40000

# Upgrade materials, named from the game's own DT_InventoryData table (build 26367565).
MATERIALS = {
    "Weapon_Material_01": "Forged Metal (One-Handed, to Lv10)",
    "Weapon_Material_02": "Polished Forged Metal (One-Handed, Lv10-20)",
    "Weapon_Material_03": "Flawless Forged Metal (One-Handed, Lv20-max)",
    "Weapon_Material_04": "Twinned Metal (Dual-Wielded, to Lv10)",
    "Weapon_Material_05": "Polished Twinned Metal (Dual-Wielded, Lv10-20)",
    "Weapon_Material_06": "Flawless Twinned Metal (Dual-Wielded, Lv20-max)",
    "Weapon_Material_07": "Broadplate Metal (Two-Handed, to Lv10)",
    "Weapon_Material_08": "Polished Broadplate Metal (Two-Handed, Lv10-20)",
    "Weapon_Material_09": "Flawless Broadplate Metal (Two-Handed, Lv20-max)",
    "Weapon_Material_10": "Solvent (all weapons, to Lv10)",
    "Weapon_Material_11": "Concentrated Solvent (all weapons, Lv10-20)",
    "Weapon_Material_12": "Universal Solvent (all weapons, Lv20-max)",
    "Weapon_Material_13": "Exotic Copper Ingot (Martial Phantom Edge, to Lv10)",
    "Weapon_Material_14": "Otherworldly Copper (Martial Phantom Edge, Lv10-20)",
    "Weapon_Material_15": "Forged Otherworldly Copper (Martial Phantom Edge, Lv20-max)",
    "Weapon_Material_16": "Darkfire Charcoal (Destruction Phantom Edge, to Lv10)",
    "Weapon_Material_17": "Blazing Darkfire Charcoal (Destruction Phantom Edge, Lv10-20)",
    "Weapon_Material_18": "Searing Darkfire Charcoal (Destruction Phantom Edge, Lv20-max)",
    "Weapon_Material_19": "Mechanical Gear (Artifice Phantom Edge, to Lv10)",
    "Weapon_Material_20": "Precision Mechanical Gear (Artifice Phantom Edge, Lv10-20)",
    "Weapon_Material_21": "Ying Mechanical Gear (Artifice Phantom Edge, Lv20-max)",
    "Weapon_Material_22": "Ancient Timber (Ranged Phantom Edge, to Lv10)",
    "Weapon_Material_23": "Camphor Timber (Ranged Phantom Edge, Lv10-20)",
    "Weapon_Material_24": "Forbidden Camphor Timber (Ranged Phantom Edge, Lv20-max)",
    "Weapon_Material_25": "Incense Ash (Summon Phantom Edge, to Lv10)",
    "Weapon_Material_26": "Illusory Incense Ash (Summon Phantom Edge, Lv10-20)",
    "Weapon_Material_27": "Incense Ash for the Lady (Summon Phantom Edge, Lv20-max)",
    "Ac_Material_1": "Tainted Crystal Shard (accessory polish +1)",
    "Ac_Material_4": "Refined Indigo Crystal (accessory polish +2)",
    "Medi_Material_1": "Apprentice Healer's Memory (medicine upgrade)",
    "Medi_Material_2": "Skilled Healer's Memory (medicine upgrade)",
    "Medi_Material_3": "Master Healer's Memory (medicine upgrade)",
    # Not a material, but a plain stackable good. DT_InventoryData row holds 99 twice.
    "Item_Traversing": "Traversal Talisman (warp to any rung Bell when away from one)",
}
WEAPONS = {
    "IronBlade": "Jagged Steel", "Long": "Sanguine Reach", "Tang": "Sanguine",
    "Double": "Sanguine Twin", "WoodenSwordHun": "Wooden Sanguine", "BrutalAxe": "Dread Axe",
}


def die(msg):
    raise SystemExit("ERROR: " + msg)


# ---------------------------------------------------------------- lossless JSON
# The game writes 17-significant-digit floats and "-0"; Python would shorten them.
# Numbers are kept as their original literal so untouched values round-trip exactly.

class Num:
    __slots__ = ("raw",)

    def __init__(self, raw):
        self.raw = raw

    def value(self):
        return float(self.raw) if any(c in self.raw for c in ".eE") else int(self.raw)


def jload(raw):
    return json.loads(raw, parse_float=Num, parse_int=Num)


def jdump(v):
    if isinstance(v, dict):
        return "{" + ",".join(json.dumps(k, ensure_ascii=False) + ":" + jdump(x) for k, x in v.items()) + "}"
    if isinstance(v, list):
        return "[" + ",".join(jdump(x) for x in v) + "]"
    if isinstance(v, Num):
        return v.raw
    if isinstance(v, bool) or v is None:
        return json.dumps(v)
    if isinstance(v, int):
        return str(v)
    if isinstance(v, str):
        return json.dumps(v, ensure_ascii=False)
    die(f"cannot serialise {type(v).__name__}")


def num(v, default=0):
    if v is None:
        return default
    return v.value() if isinstance(v, Num) else v


def plain(v):
    if isinstance(v, dict):
        return {k: plain(x) for k, x in v.items()}
    if isinstance(v, list):
        return [plain(x) for x in v]
    return num(v)


# ---------------------------------------------------------------- Oodle codec

class Codec:
    def __init__(self, path=None):
        path = path or os.environ.get("PBZ_CODEC") or os.path.join(
            HERE, "codec", "target", "release", "libpbz_codec.so")
        if not os.path.isfile(path):
            die(f"Oodle decoder not built: {path}\n"
                "  Build it once: see docs/pbz-tool-cai-dat-va-su-dung.md (cargo build --release in codec/).")
        self.fn = ctypes.CDLL(path).pbz_decode
        self.fn.restype = ctypes.c_ssize_t
        self.fn.argtypes = [ctypes.c_void_p, ctypes.c_size_t, ctypes.c_void_p, ctypes.c_size_t]

    def decompress(self, data, size):
        if size == 0:
            return b""
        out = ctypes.create_string_buffer(size)
        n = self.fn(data, len(data), out, size)
        if n != size:
            die(f"Oodle decode failed ({n})")
        return out.raw

    def compress_stored(self, data):
        # 0xCC 0x06 = Kraken block header with the "uncompressed" bit: raw bytes follow.
        out = b"".join(b"\xcc\x06" + data[p:p + STORED_CHUNK] for p in range(0, len(data), STORED_CHUNK))
        if self.decompress(out, len(data)) != data:
            die("stored-block self check failed")
        return out


# ---------------------------------------------------------------- container

def unseal(key, block):
    if len(block) < 36 or block[:8] != SEAL:
        die("bad sealed block header")
    return AESGCM(key).decrypt(block[8:20], block[36:] + block[20:36], None)


def seal(key, clear):
    nonce = os.urandom(12)
    ct = AESGCM(key).encrypt(nonce, clear, None)
    return SEAL + nonce + ct[-16:] + ct[:-16]


def find_key(exe, src):
    """Scan PBZ.exe for the anchor; accept only a key that authenticates this save."""
    dsize = struct.unpack_from("<I", src, 8)[0]
    directory = src[12:12 + dsize]
    tried = 0
    with open(exe, "rb") as fh, mmap.mmap(fh.fileno(), 0, access=mmap.ACCESS_READ) as m:
        pos = 0
        while True:
            pos = m.find(KEY_ANCHOR, pos)
            if pos < 0:
                break
            pos += len(KEY_ANCHOR)
            for pad in range(16):
                mat = m[pos + pad:pos + pad + 64]
                if len(mat) < 64:
                    break
                key = bytes(a ^ b for a, b in zip(mat[:32], mat[32:]))
                tried += 1
                try:
                    clear = AESGCM(key).decrypt(directory[8:20], directory[36:] + directory[20:36], None)
                except InvalidTag:
                    continue
                if clear[:12] == src[:12]:
                    return key
    die(f"no key in {exe} authenticates this save ({tried} candidates). Game update changed the scheme?")


def decode(src, key, codec):
    if len(src) < 12 or src[:4] != b"PBZS":
        die("not a PBZS save")
    version, flags, count, dsize = struct.unpack_from("<BBHI", src, 4)
    if version != 3 or flags != 1:
        die(f"unsupported container version {version} flags {flags}")
    directory = unseal(key, src[12:12 + dsize])
    if directory[:12] != src[:12]:
        die("directory header copy mismatch")
    cur, end, slots = 12, 0, []
    base = 12 + dsize
    for _ in range(count):
        n = struct.unpack_from("<H", directory, cur)[0]
        cur += 2
        name = directory[cur:cur + n].decode("utf8")
        cur += n
        alg, flag, size, off, bsize = struct.unpack_from("<BBIII", directory, cur)
        cur += 14
        if flag != 1 or off != end or size > MAX_SLOT:
            die(f"slot {name}: unexpected directory entry")
        block = src[base + off:base + off + bsize]
        payload = unseal(key, block)
        if alg == 0:
            raw = payload
        elif alg == 1:
            raw = zlib.decompress(payload)
        elif alg == 2:
            raw = codec.decompress(payload, size)
        else:
            die(f"slot {name}: unknown compression {alg}")
        if len(raw) != size:
            die(f"slot {name}: size mismatch")
        slots.append({"name": name, "alg": alg, "raw": raw, "block": block})
        end = off + bsize
    if cur != len(directory) or base + end != len(src):
        die("trailing bytes in directory or file")
    return slots


def encode(slots, key, codec, replaced):
    rows, blocks, off = [], [], 0
    for s in slots:
        alg, raw, block = s["alg"], s["raw"], s["block"]
        if s["name"] in replaced:
            raw = replaced[s["name"]]
            if alg == 2:
                payload = codec.compress_stored(raw)
            elif alg == 1:
                payload = zlib.compress(raw)
            else:
                payload = raw
            block = seal(key, payload)
        name = s["name"].encode("utf8")
        rows.append(struct.pack("<H", len(name)) + name + struct.pack("<BBIII", alg, 1, len(raw), off, len(block)))
        blocks.append(block)
        off += len(block)
    dsize = 12 + sum(map(len, rows)) + 36
    header = b"PBZS" + struct.pack("<BBHI", 3, 1, len(slots), dsize)
    return header + seal(key, header + b"".join(rows)) + b"".join(blocks)


# ---------------------------------------------------------------- paths & guards

def find_game(arg):
    cands = [arg] if arg else ([os.environ["PBZ_GAME"]] if os.environ.get("PBZ_GAME") else
                               glob.glob("/mnt/*/SteamLibrary/steamapps/common/PBZ") +
                               glob.glob("/mnt/*/Program Files (x86)/Steam/steamapps/common/PBZ"))
    cands = [c for c in cands if os.path.isfile(os.path.join(c, "platform", "steam", "PBZ.exe"))]
    if len(cands) != 1:
        die("cannot find the game folder (need platform/steam/PBZ.exe). Pass --game or set PBZ_GAME.")
    return cands[0]


def find_save(arg, game):
    if arg:
        return arg
    if os.environ.get("PBZ_SAVE"):
        return os.environ["PBZ_SAVE"]
    cands = glob.glob(os.path.join(game, "ProjectPBZ", "Saved", "SaveGames", "Steam", "*", "PBZSaveGame.sav"))
    if len(cands) != 1:
        die(f"found {len(cands)} PBZSaveGame.sav files; pass --save or set PBZ_SAVE.")
    return cands[0]


def game_running():
    cmd = ["tasklist.exe", "/fo", "csv", "/nh"] if "microsoft" in os.uname().release.lower() else \
        (["tasklist", "/fo", "csv", "/nh"] if os.name == "nt" else None)
    if cmd is None:
        return False
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, errors="replace", timeout=15).stdout
    except (OSError, subprocess.SubprocessError):
        die("cannot list processes to check that the game is closed; refusing to write.")
    if not out.strip():
        die("empty process list; refusing to write.")
    return any(line.lower().startswith('"pbz.exe"') for line in out.splitlines())


def backup_dir(arg):
    return arg or os.environ.get("PBZ_BACKUP_DIR") or os.path.expanduser("~/game/backups/phantom-blade-zero")


# ---------------------------------------------------------------- session

class Save:
    def __init__(self, args):
        self.game = find_game(args.game)
        self.path = find_save(args.save, self.game)
        self.src = open(self.path, "rb").read()
        self.codec = Codec(args.codec)
        self.key = find_key(os.path.join(self.game, "platform", "steam", "PBZ.exe"), self.src)
        self.slots = decode(self.src, self.key, self.codec)
        self.json = {s["name"]: jload(s["raw"]) for s in self.slots}
        adv = self.json.get("__Advanced__", {})
        self.current = adv.get("LastContinueSlot", "")

    def game_slots(self):
        return [s["name"] for s in self.slots if isinstance(self.json[s["name"]].get("Inventory"), dict)]

    def pick(self, slot):
        slot = slot or self.current
        if slot not in self.game_slots():
            die(f"slot '{slot}' not found; game slots: {', '.join(self.game_slots())}")
        raw = next(s["raw"] for s in self.slots if s["name"] == slot)
        if jdump(self.json[slot]).encode("utf8") != raw:
            die(f"slot {slot} does not re-serialise byte for byte; refusing to edit it.")
        return slot

    def write(self, slot, changes, args):
        out = encode(self.slots, self.key, self.codec, {slot: jdump(self.json[slot]).encode("utf8")})
        check = decode(out, self.key, self.codec)
        for old, new in zip(self.slots, check):
            if old["name"] != slot and old["raw"] != new["raw"]:
                die(f"self check: untouched slot {old['name']} changed")
        print(f"\nSave: {self.path}\nSlot: {slot}" + (" (the one Continue loads)" if slot == self.current else ""))
        for line in changes:
            print("  " + line)
        if args.dry_run:
            print("Dry run, nothing written.")
            return
        if game_running():
            die("PBZ.exe is running. Quit the game from its menu first; the game rewrites the save from memory.")
        if not args.yes and input("Type 'yes' to write (a backup is made first): ").strip().lower() != "yes":
            raise SystemExit("Aborted, no changes written.")
        if open(self.path, "rb").read() != self.src:
            die("the save changed on disk since it was read; run again.")
        bdir = backup_dir(args.backup_dir)
        os.makedirs(bdir, exist_ok=True)
        bak = os.path.join(bdir, f"PBZSaveGame-{time.strftime('%Y%m%d-%H%M%S')}.sav")
        shutil.copy2(self.path, bak)
        print("Backup:", bak)
        tmp = self.path + ".tmp-pbz-tool"
        with open(tmp, "wb") as fh:
            fh.write(out)
        os.replace(tmp, self.path)
        again = decode(open(self.path, "rb").read(), self.key, self.codec)
        if [s["raw"] for s in again] != [s["raw"] for s in check]:
            die(f"readback mismatch! restore with: restore {bak}")
        print("Written and read back OK. Now: launch, load, check in game, quit from the menu, let Steam sync.")


# ---------------------------------------------------------------- commands

def goods(inv):
    return inv.setdefault("InventoryInfos", {})


def cmd_list(sv, args):
    print(f"Save: {sv.path}")
    for name in sv.game_slots():
        g = sv.json[name].get("PBZGameSystem", {})
        mark = "  <- Continue" if name == sv.current else ""
        print(f"  {name:10} {g.get('DateTimeString', '')}  {g.get('CurrentLevelName', '')}{mark}")
    slot = sv.pick(args.slot)
    d = sv.json[slot]
    p, inv = d.get("Player", {}), d.get("Inventory", {})
    print(f"\n[{slot}] Dust {num(p.get('Dust'))}  RemainingDays {num(p.get('RemainingDays'))}  "
          f"Deaths {num(d.get('PBZDeathMeta', {}).get('DiedTimes'))}")
    print("Weapons:", ", ".join(f"{w} ({WEAPONS.get(w, '?')})" for w in inv.get("MainWeaponInfos", {})))
    print("Phantom edges:", ", ".join(f"{w} ({WEAPONS.get(w, '?')})" for w in inv.get("ShaChiWeaponInfo", {})))
    print("Materials:")
    for k, v in goods(inv).items():
        if k in MATERIALS or args.all:
            print(f"  {k:20} {num(v.get('CurrentAmount')):>7}  {MATERIALS.get(k, '')}")


def cmd_materials(sv, args):
    for k, v in MATERIALS.items():
        print(f"  {k:20} {v}")


def cmd_dump(sv, args):
    os.makedirs(args.out, exist_ok=True)
    for name, j in sv.json.items():
        with open(os.path.join(args.out, name + ".json"), "w", encoding="utf8") as fh:
            json.dump(plain(j), fh, ensure_ascii=False, indent=1)
    print(f"Wrote {len(sv.json)} slots to {args.out}")


def cmd_dust(sv, args):
    slot = sv.pick(args.slot)
    p = sv.json[slot]["Player"]
    old = num(p.get("Dust"))
    new = old + args.amount if args.cmd == "add-dust" else args.amount
    if not 0 <= new <= 2_000_000_000:
        die("Dust out of range")
    p["Dust"] = new
    sv.write(slot, [f"Dust {old} -> {new}"], args)


def cmd_item(sv, args):
    slot = sv.pick(args.slot)
    pairs = args.pairs
    if len(pairs) % 2:
        die("give ID QTY pairs, e.g. add-item Weapon_Material_01 20 Weapon_Material_10 20")
    d = sv.json[slot]
    inv = goods(d["Inventory"])
    stamp = time.strftime("%Y.%m.%d-%H.%M.%S")
    changes = []
    for item, qty in zip(pairs[::2], pairs[1::2]):
        try:
            qty = int(qty)
        except ValueError:
            die(f"quantity for {item} is not a number: {qty}")
        if item not in MATERIALS and not args.allow_unknown:
            die(f"{item} is not a known item (see 'materials'); use --allow-unknown to force.")
        rec = inv.get(item)
        old = num(rec.get("CurrentAmount")) if rec else 0
        new = old + qty if args.cmd == "add-item" else qty
        if not 0 <= new <= 2_000_000_000:
            die(f"{item}: quantity out of range")
        if rec is None:
            inv[item] = {"CurrentAmount": new, "MaxAmount": new, "FirstAddTime": stamp, "DirtyTime": stamp,
                         "AcquiredCycle": num(d.get("PBZGameSystem", {}).get("CycleCount"))}
        else:
            rec["CurrentAmount"] = new
            rec["MaxAmount"] = max(num(rec.get("MaxAmount")), new)
            rec["DirtyTime"] = stamp
        changes.append(f"{item} ({MATERIALS.get(item, '?')}) {old} -> {new}")
    sv.write(slot, changes, args)


def cmd_restore(sv, args):
    data = open(args.backup, "rb").read()
    decode(data, sv.key, sv.codec)  # must decrypt with this game's key
    print(f"Restore {args.backup}\n   -> {sv.path}")
    if args.dry_run:
        return print("Dry run, nothing written.")
    if game_running():
        die("PBZ.exe is running; quit the game first.")
    if not args.yes and input("Type 'yes' to overwrite the current save: ").strip().lower() != "yes":
        raise SystemExit("Aborted.")
    bdir = backup_dir(args.backup_dir)
    os.makedirs(bdir, exist_ok=True)
    bak = os.path.join(bdir, f"PBZSaveGame-{time.strftime('%Y%m%d-%H%M%S')}-before-restore.sav")
    shutil.copy2(sv.path, bak)
    print("Current save backed up to", bak)
    shutil.copyfile(args.backup, sv.path)
    print("Restored.")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--game", help="game folder containing platform/steam/PBZ.exe (or PBZ_GAME)")
    ap.add_argument("--save", help="path to PBZSaveGame.sav (or PBZ_SAVE)")
    ap.add_argument("--codec", help="path to libpbz_codec.so (or PBZ_CODEC)")
    ap.add_argument("--backup-dir", help="backup folder (or PBZ_BACKUP_DIR; default ~/game/backups/phantom-blade-zero)")
    ap.add_argument("--slot", help="slot to read/edit (default: the slot Continue loads)")
    ap.add_argument("-y", "--yes", action="store_true", help="skip the yes prompt")
    ap.add_argument("-n", "--dry-run", action="store_true", help="show the change, write nothing")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("list", help="slots, Dust, weapons, materials")
    p.add_argument("--all", action="store_true", help="show every inventory entry, not just materials")
    p.set_defaults(fn=cmd_list)
    sub.add_parser("materials", help="known item IDs (materials, Traversal Talisman)").set_defaults(fn=cmd_materials)
    p = sub.add_parser("dump", help="write every slot as readable JSON")
    p.add_argument("--out", required=True)
    p.set_defaults(fn=cmd_dump)
    for name in ("set-dust", "add-dust"):
        p = sub.add_parser(name, help=f"{name.split('-')[0]} Remnant Dust")
        p.add_argument("amount", type=int)
        p.set_defaults(fn=cmd_dust)
    for name in ("add-item", "set-qty"):
        p = sub.add_parser(name, help="add to / set item quantities: ID QTY [ID QTY ...]")
        p.add_argument("pairs", nargs="+", metavar="ID QTY")
        p.add_argument("--allow-unknown", action="store_true")
        p.set_defaults(fn=cmd_item)
    p = sub.add_parser("restore", help="put a backup back")
    p.add_argument("backup")
    p.set_defaults(fn=cmd_restore)
    args = ap.parse_args()
    args.fn(Save(args), args)


if __name__ == "__main__":
    main()
