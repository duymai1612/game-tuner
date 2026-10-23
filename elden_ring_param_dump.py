#!/usr/bin/env python3
"""Dump the regulation.bin param tables that name boss flags and map ids.

    python3 elden_ring_param_dump.py bosses     # defeatBossFlagId + arena map id
    python3 elden_ring_param_dump.py graces     # grace event flag + map id
    python3 elden_ring_param_dump.py maps       # dungeon map id -> overworld tile

Why these three: a small-dungeon boss flag looks like {areaNo}{blockNo}0800, but the
convention alone cannot say WHICH dungeon a map id is, and it is wrong often enough
to matter (Sealed Tunnel is m34_12, not an m32 tunnel). GameAreaParam gives the flag
outright, BonfireWarpParam names a map through the grace inside it, and
WorldMapLegacyConvParam pins a map to an overworld tile for the dungeons that have no
grace of their own.

Field offsets come from soulsmods/Paramdex ER/Defs/*.xml. The trap in all three: the
two bitfields opening every row (`u8 disableParam_NT:1` + `dummy8 ...:7`) share ONE
byte, so a parser that gives them a byte each shifts every later offset by 4.

Needs pycryptodome and zstandard, same as elden_ring_regulation.py."""
import os
import struct
import sys

import elden_ring_regulation as R

REGULATION = os.path.expanduser(
    "~/Library/Application Support/CrossOver/Bottles/Steam/drive_c/Program Files "
    "(x86)/Steam/steamapps/common/ELDEN RING/Game/regulation.bin")

TABLES = {
    # command: (param file, {label: (offset, struct format)})
    "bosses": ("GameAreaParam.param",
               {"defeat_flag": (68, "<I"), "map": (84, "<BBB")}),
    "graces": ("BonfireWarpParam.param",
               {"event_flag": (4, "<I"), "map": (32, "<BBB")}),
    "maps":   ("WorldMapLegacyConvParam.param",
               {"src": (4, "<BBB"), "dst": (20, "<BBB")}),
}


def rows(bnd, filename):
    """Row entries are (u32 id, u32 pad, u64 dataOffset, u64 nameOffset). The table
    start is not at a fixed offset across param versions, so find it: demand zero
    pad, ascending unique ids, in-range data offsets, and one constant stride."""
    ent = next(e for e in R.bnd4_entries(bnd)
               if e["name"].split("\\")[-1] == filename)
    buf = bytes(bnd[ent["data_off"]:ent["data_off"] + ent["size"]])
    count, = struct.unpack_from("<H", buf, 0x0A)
    for start in range(0x20, 0x80, 4):
        try:
            table = [struct.unpack_from("<IIQQ", buf, start + i * 24)
                     for i in range(count)]
        except struct.error:
            continue
        ids, offs = [r[0] for r in table], [r[2] for r in table]
        if any(r[1] for r in table) or ids != sorted(ids) or len(set(ids)) != len(ids):
            continue
        if any(not (0 < o < len(buf)) for o in offs):
            continue
        if len({b - a for a, b in zip(offs, offs[1:])}) == 1:
            return buf, table
    raise SystemExit(f"{filename}: could not locate the row table ({count} rows)")


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd not in TABLES:
        raise SystemExit(f"usage: {sys.argv[0]} {{{'|'.join(TABLES)}}} [regulation.bin]")
    path = sys.argv[2] if len(sys.argv) > 2 else REGULATION
    filename, fields = TABLES[cmd]
    bnd, _ = R.unpack(path)
    buf, table = rows(bnd, filename)
    print("row_id\t" + "\t".join(fields))
    for rid, _, off, _ in table:
        cells = []
        for name, (rel, fmt) in fields.items():
            vals = struct.unpack_from(fmt, buf, off + rel)
            cells.append(f"m{vals[0]:02d}_{vals[1]:02d}_{vals[2]:02d}"
                         if len(vals) == 3 else str(vals[0]))
        print(f"{rid}\t" + "\t".join(cells))


if __name__ == "__main__":
    main()
