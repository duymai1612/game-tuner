# Tool save Phantom Blade Zero: cài đặt và sử dụng

`pbz_save_tool.py` đọc và sửa `PBZSaveGame.sav` bản Steam PC, chạy trong WSL. Hiện sửa được Remnant Dust và số lượng nguyên liệu nâng cấp. Đã test với game build 26367565.

## Save nằm ở đâu

Save PBZ ko nằm trong AppData mà nằm trong thư mục game:

```
<Steam library>\steamapps\common\PBZ\ProjectPBZ\Saved\SaveGames\Steam\<SteamID64>\PBZSaveGame.sav
```

Cùng thư mục có `1RealTime/`, `2Hourly/`, `3Daily/`: game tự backup vào đó. `%LOCALAPPDATA%\ProjectPBZ` chỉ chứa config đồ hoạ (`GameUserSettings.ini`) và log.

Tool tự tìm game trong `/mnt/*/SteamLibrary/steamapps/common/PBZ` và `/mnt/*/Program Files (x86)/Steam/steamapps/common/PBZ`. Nằm chỗ khác thì đặt `PBZ_GAME` hoặc thêm `--game`.

## Cài trên PC (WSL)

1. Python cần `cryptography`. Ubuntu thường có sẵn, thiếu thì `sudo apt install -y python3-cryptography`.
2. Build bộ giải nén Oodle một lần. Nó là một thư viện Rust nhỏ bọc crate `oozextract` (MIT):

   ```bash
   sudo apt install -y build-essential
   curl -sSf https://sh.rustup.rs | sh -s -- -y --profile minimal
   cd ~/game/game-tuner/phantom-blade-zero/codec
   ~/.cargo/bin/cargo build --release
   ```

   Ko có quyền sudo để cài `build-essential` thì dùng zig làm linker:

   ```bash
   mkdir -p ~/.local/opt ~/.local/bin && cd ~/.local/opt
   curl -sSfL https://ziglang.org/download/0.13.0/zig-linux-x86_64-0.13.0.tar.xz | tar xJ
   printf '#!/bin/sh\nexec ~/.local/opt/zig-linux-x86_64-0.13.0/zig cc -target x86_64-linux-gnu "$@"\n' > ~/.local/bin/zigcc
   chmod +x ~/.local/bin/zigcc
   cd ~/game/game-tuner/phantom-blade-zero/codec
   CC=~/.local/bin/zigcc CARGO_TARGET_X86_64_UNKNOWN_LINUX_GNU_LINKER=~/.local/bin/zigcc ~/.cargo/bin/cargo build --release
   ```

   Kết quả là `codec/target/release/libpbz_codec.so`; git đã bỏ qua thư mục `target/`.
3. Chạy thử: `python3 pbz_save_tool.py list`.

## Lệnh

Chạy từ `phantom-blade-zero/`:

```bash
python3 pbz_save_tool.py list                              # slot, Dust, vũ khí, nguyên liệu
python3 pbz_save_tool.py materials                         # bảng ID nguyên liệu và tên
python3 pbz_save_tool.py add-dust 30000                    # cộng thêm Remnant Dust
python3 pbz_save_tool.py set-dust 50000                    # đặt Dust về đúng số này
python3 pbz_save_tool.py add-item Weapon_Material_01 20    # thêm 20 Forged Metal
python3 pbz_save_tool.py set-qty Weapon_Material_10 40     # đặt Solvent = 40
python3 pbz_save_tool.py -n add-dust 30000                 # chạy thử, ko ghi
python3 pbz_save_tool.py dump --out /tmp/pbz-json          # xuất mọi slot ra JSON để đọc
python3 pbz_save_tool.py restore ~/game/backups/phantom-blade-zero/PBZSaveGame-<ngày giờ>.sav
```

- Mặc định tool sửa slot mà Continue load. Muốn slot khác thì thêm `--slot AutoSave1`.
- Mỗi lần ghi, tool bắt gõ `yes`. Thêm `-y` để bỏ bước này.
- Backup nằm ở `~/game/backups/phantom-blade-zero/`, ngoài thư mục save vì Steam Cloud sync cả thư mục đó. Đổi chỗ bằng `--backup-dir` hoặc `PBZ_BACKUP_DIR`.

### Nguyên liệu theo loại vũ khí

Mỗi loại có 3 bậc: đến Lv10, Lv10–20, Lv20 trở lên. Ví dụ Forged Metal là `01`, `02`, `03`.

| ID bậc 1 | Tên | Dùng cho |
|---|---|---|
| `Weapon_Material_01` | Forged Metal | vũ khí một tay |
| `Weapon_Material_04` | Twinned Metal | vũ khí đôi |
| `Weapon_Material_07` | Broadplate Metal | vũ khí hai tay |
| `Weapon_Material_10` | Solvent | mọi vũ khí chính |
| `Weapon_Material_13` | Exotic Copper Ingot | Phantom Edge hệ Martial |
| `Weapon_Material_16` | Darkfire Charcoal | Phantom Edge hệ Destruction |
| `Weapon_Material_19` | Mechanical Gear | Phantom Edge hệ Artifice |
| `Weapon_Material_22` | Ancient Timber | Phantom Edge hệ Ranged |
| `Weapon_Material_25` | Incense Ash | Phantom Edge hệ Summon |

Nâng một vũ khí chính từ Lv1 lên Lv10 tốn khoảng 52 kim loại, 26 Solvent và 27.000–30.000 Dust. Phantom Edge tốn khoảng 26 nguyên liệu và 17.000 Dust. Revert trong game trả lại 100% Dust và nguyên liệu đã dùng.

## Luật trước khi sửa save

1. Thoát game hẳn, bằng menu. Tool từ chối ghi khi thấy `PBZ.exe` trong `tasklist.exe`.
2. Sửa xong thì làm đủ quy trình Steam Cloud: mở game, nếu Steam hỏi Cloud Conflict thì chọn bản local, load save, kiểm tra tận mắt, thoát bằng menu, đợi Steam sync.
3. File save to lên sau khi sửa, vì slot đã sửa được ghi lại ở dạng Oodle ko nén. Lần sau game tự lưu thì nó nén lại.

## Tool hoạt động thế nào

- Save là container `PBZS` v3: mỗi slot được mã hoá AES-256-GCM, nén Oodle Kraken, bên trong là JSON. Định dạng do cộng đồng giải ra: [PBZ-Editor](https://github.com/qry6868/PBZ-Editor) và [phantom-blade-zero-save-format](https://github.com/fancydirty/phantom-blade-zero-save-format).
- Key ko nằm trong repo. Tool dò key trong `platform/steam/PBZ.exe` mỗi lần chạy và chỉ nhận key nào giải mã được save, nên game update đổi vị trí key vẫn chạy được.
- Game ghi số thực đủ 17 chữ số và có cả `-0`. Tool giữ nguyên từng literal, và từ chối sửa slot nào mà đọc vào rồi ghi ra ko giống hệt bản cũ.
- Trước khi ghi, tool giải mã lại kết quả và kiểm các slot ko sửa vẫn giữ nguyên. Sau khi ghi, nó đọc file trên đĩa thêm lần nữa để so.
- Khi viết tool, em đã cho bộ đọc của PBZ-Editor đọc thử file tool ghi ra để kiểm chéo.

## Ko sửa được

- Thêm vũ khí, phụ kiện hay trang phục chưa có. PBZ-Editor làm được việc này nếu cần.
- Item quest: thêm vào ko làm xong quest.
- Số lần dùng thuốc: game tự nạp lại theo luật riêng lúc load.
