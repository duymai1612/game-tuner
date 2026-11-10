# Bộ tool Elden Ring: cài đặt và sử dụng

Tool offline để sửa save `ER0000.sl2` và đọc `regulation.bin` bản PC. Chạy được trên Windows qua WSL và trên Mac qua CrossOver.

## Cài trên PC (Windows + WSL)

1. Clone vào home của WSL. Đừng clone vào `/mnt/c` vì git chạy trên đó rất chậm.

   ```bash
   mkdir -p ~/game && cd ~/game
   git clone https://github.com/duymai1612/game-tuner.git
   cd game-tuner/elden-ring
   ```

   Repo public nên clone và pull ko cần đăng nhập. Mọi lệnh bên dưới chạy từ thư mục `game-tuner/elden-ring`. Muốn push từ PC thì `gh auth login` bằng account duymai1612, hoặc add SSH key của account đó.

2. Save editor và grace tool chỉ cần `python3` có sẵn trên Ubuntu. Các tool đọc `regulation.bin` cần thêm hai lib:

   ```bash
   sudo apt install -y python3-venv
   python3 -m venv .venv
   .venv/bin/pip install pycryptodome zstandard
   ```

3. Tìm file save rồi gán đường dẫn vào biến cho đỡ gõ. Muốn giữ biến cho các lần sau thì thêm vào `~/.bashrc`.

   ```bash
   ls /mnt/c/Users/*/AppData/Roaming/EldenRing/*/ER0000.sl2
   export ER_SAVE="/mnt/c/Users/<WinUser>/AppData/Roaming/EldenRing/<SteamID64>/ER0000.sl2"
   export ER_REG="/mnt/c/Program Files (x86)/Steam/steamapps/common/ELDEN RING/Game/regulation.bin"
   ```

   Nếu Steam library nằm ở ổ khác thì sửa `ER_REG` theo, ví dụ `/mnt/d/SteamLibrary/steamapps/common/ELDEN RING/Game/regulation.bin`.

4. Chạy `selftest` một lần để chắc tool đọc đúng file:

   ```bash
   python3 elden_ring_save_editor.py -f "$ER_SAVE" selftest
   ```

## Trên Mac (CrossOver)

- Save nằm ở `~/Library/Application Support/CrossOver/Bottles/Steam/drive_c/users/crossover/AppData/Roaming/EldenRing/<SteamID64>/ER0000.sl2`.
- `regulation.bin` nằm trong bottle ở `.../drive_c/Program Files (x86)/Steam/steamapps/common/ELDEN RING/Game/`.
- `warp.command` mở bản Việt hoá qua me3, `luyen-tap.command` mở save luyện tập riêng. Hai file này chỉ chạy được trên Mac. Cách cài Việt hoá xem [elden-ring-viet-hoa-macos-crossover-setup.md](elden-ring-viet-hoa-macos-crossover-setup.md).

## Luật trước khi sửa save

1. Thoát game hẳn. Game giữ save trong RAM và ghi đè file ở lần autosave kế tiếp, nên sửa lúc game đang mở thì edit mất mà ko có lỗi nào báo. Tool sẽ từ chối ghi khi thấy `eldenring.exe` đang chạy; trong WSL tool đọc danh sách process qua `tasklist.exe`. Muốn tự kiểm thì chạy `tasklist.exe | grep -i eldenring`.
2. Nhân vật chính nằm ở slot 1, slot 0 là nhân vật mồi. Mọi lệnh mặc định chạy slot 0 và chạy nhầm slot thì tool ko báo lỗi, nên luôn thêm `--slot 1`. Chạy `list` để xem các slot.
3. Mỗi lần ghi, tool bắt gõ `yes` để xác nhận và tạo một file `.bak-<ngày giờ>` cạnh file save. Thêm `-y` để bỏ bước xác nhận.
4. Chơi hai máy qua Steam Cloud: Steam chỉ sync lúc game mở và lúc game thoát, nên sửa save xong phải làm đủ bước này thì máy kia mới thấy bản sửa:
   1. Mở game. Nếu Steam hỏi Cloud Conflict thì chọn bản local, tức bản mới hơn.
   2. Load nhân vật và kiểm tra thứ vừa sửa.
   3. Thoát bằng menu trong game, đừng tắt cứng cửa sổ.
   4. Đợi Steam sync xong rồi mới qua máy kia.

   Đừng sửa `remotecache.vdf`, Steam sẽ tưởng file đã sync và bỏ qua bước upload.
5. Tool báo checksum sạch chưa có nghĩa là edit còn. Kiểm chứng là vào game nhìn tận mắt.

## Sửa save: `elden_ring_save_editor.py`

```bash
python3 elden_ring_save_editor.py -f "$ER_SAVE" list                      # nhân vật theo slot
python3 elden_ring_save_editor.py -f "$ER_SAVE" list-items --slot 1       # đồ đang giữ (--goods-only, --array key)
python3 elden_ring_save_editor.py -f "$ER_SAVE" set-rune --slot 1 5000000
python3 elden_ring_save_editor.py -f "$ER_SAVE" set-stats --slot 1 --vigor 60 --mind 30
python3 elden_ring_save_editor.py -f "$ER_SAVE" set-qty --slot 1 --name "Rune Arc" --qty 99
python3 elden_ring_save_editor.py -f "$ER_SAVE" add-item --slot 1 --name "Rune Arc" --qty 10
python3 elden_ring_save_editor.py -f "$ER_SAVE" add-aow --slot 1 --name "Golden Parry"
python3 elden_ring_save_editor.py -f "$ER_SAVE" list-armor --slot 1
```

- `set-stats` tự tính lại level bằng tổng stat trừ 79. Stat gồm `--vigor --mind --endurance --strength --dexterity --intelligence --faith --arcane`, còn `--wretch` đưa cả 8 stat về 10.
- `add-item` thêm được consumable và talisman (`--talisman`). Medallion, map, cookbook, crystal tear là key item, phải thêm `--key`. Tool ko thêm được vũ khí hay giáp mới.
- `replace-weapon --source <đang có> --target <muốn có>` biến một vũ khí đang có thành vũ khí khác. Vũ khí nguồn mất luôn và vũ khí mới về +0. `replace-armor` làm việc tương tự với giáp.
- Ash of War đang gắn trên vũ khí ko hiện trong `list-items`, nên ko thấy ash trong list chưa có nghĩa là chưa có ash đó.
- `set-hp` vô dụng vì game tính lại HP từ Vigor lúc load nhân vật.

## Grace, map, boss: `elden_ring_grace_unlock.py`

```bash
python3 elden_ring_grace_unlock.py -f "$ER_SAVE" --slot 1 report          # grace đã sáng theo vùng, kèm tên vùng
python3 elden_ring_grace_unlock.py -f "$ER_SAVE" --slot 1 unlock --region <Vùng>
python3 elden_ring_grace_unlock.py -f "$ER_SAVE" --slot 1 unlock-maps     # cả unlock-whetblades, unlock-cookbooks, unlock-summoning-pools
python3 elden_ring_grace_unlock.py -f "$ER_SAVE" --slot 1 boss-report     # boss đã giết, base game và DLC
python3 elden_ring_grace_unlock.py -f "$ER_SAVE" --slot 1 respawn-boss --boss "Bell Bearing Hunter (Church of Vows)"
```

- `unlock` ko có `--region` thì thắp mọi grace, trừ Ashen Capital và Farum Azula; thêm `--include-endgame` để thắp luôn hai vùng đó.
- Dòng đầu của `report` in ra `event_flags @ 0x...`, nên ghi lại giá trị này. Lần sau tool báo ko tìm được offset thì truyền nó vào `--base 0x...`.
- `--boss` nhận tên hoặc flag id. Tên khớp nhiều boss thì tool liệt kê ra rồi dừng, ko ghi gì, lúc đó ghi đủ tên kèm phần trong ngoặc.
- `respawn-boss` chỉ xoá cờ defeat. Field boss vậy là đủ để sống lại. Boss chính có thêm cờ đi kèm, ví dụ Malenia cần xoá cả 5 cờ `15000800`, `15000801`, `9120`, `1120`, `71500` và giữ nguyên `61120`, `510200` để giết lại ko nhận thêm Great Rune. Tool chưa có lệnh cho bộ cờ này.
- Bảng flag nằm ở `plans/260729-1313-eldenring-event-flag-re/`.

## Đọc `regulation.bin`

```bash
.venv/bin/python3 elden_ring_param_dump.py bosses "$ER_REG"   # cờ defeat và map id của từng boss
.venv/bin/python3 elden_ring_param_dump.py graces "$ER_REG"   # cờ grace và map id
.venv/bin/python3 elden_ring_param_dump.py maps "$ER_REG"     # map dungeon trỏ về ô overworld nào
```

Đây là nguồn chuẩn để tìm flag boss, đừng đoán ID theo quy ước: bảng boss dựng tay trước đây từng thiếu cả Radahn.

`elden_ring_regulation.py` dùng để unpack hoặc repack `regulation.bin`, còn `elden_ring_patch_hp_curve.py <src> <dst>` dùng để nâng đường HP theo Vigor khi luyện parry. Trên CrossOver, ghi đè `regulation.bin` trong thư mục game làm game crash. Trên Windows chưa ai thử. Đọc docstring của hai file và [elden-ring-macos-modding-capability-notes.md](elden-ring-macos-modding-capability-notes.md) trước, và backup `regulation.bin` gốc trước khi thử.

## Tài liệu khác trong `docs/`

- Questline: [base game](elden-ring-questline-checklist-va-quest-path.md), [DLC](elden-ring-dlc-questline-checklist-va-quest-path.md), [boss cần xong gì trước khi đánh](elden-ring-boss-va-dieu-kien-can-xong-truoc-khi-danh.md).
- Build: [Malenia no-hit](elden-ring-malenia-solo-no-hit-build-guide.md), [Moonveil và Dark Moon INT](elden-ring-moonveil-darkmoon-int-build-guide.md), [bleed katana](elden-ring-bleed-katana-build-guide.md).
- Audit đồ: [sau Messmer](elden-ring-sau-messmer-va-audit-item-con-thieu.md), [playlist 32 build](elden-ring-playlist-32-build-audit-do-con-thieu.md).
- Lore: [lore/README.md](lore/README.md).
