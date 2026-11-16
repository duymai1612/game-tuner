# Mod Phantom Blade Zero: danh sách và cách cài

Bộ mod để bỏ bớt phần lặt vặt: tự nhặt đồ, bản đồ có marker, nghỉ nhanh, chạy nhanh, chỉnh camera. Tải từ Nexus Mods ngày 2026-11-16, mod nào cũng ghi đã test trên Steam build 26367565. Chưa cài thử trên máy PC.

File mod ko nằm trong repo này vì tác giả nào cũng ghi ko cho up lại file lên nơi khác. Bản sao để tự cài nằm ở repo private `duymai1612/game-tuner-mods`, thư mục `phantom-blade-zero/`.

## Danh sách

| # | Mod | Bản | File Nexus | Cần |
|---|---|---|---|---|
| 1 | [UE4SS for Phantom Blade Zero](https://www.nexusmods.com/phantombladezero/mods/5) | 1.0.3 | 1780 | |
| 2 | [Mods Menu](https://www.nexusmods.com/phantombladezero/mods/149) | 0.9.8 | 3843 | |
| 3 | [Auto Collect Loot](https://www.nexusmods.com/phantombladezero/mods/70) | 1.8.0 | 3347 | Mods Menu 0.5.1 trở lên |
| 4 | [Movement Speed](https://www.nexusmods.com/phantombladezero/mods/56) | 1.4.3 | 3838 | Mods Menu 0.5.1 trở lên |
| 5 | [Map Tracker Plus](https://www.nexusmods.com/phantombladezero/mods/187) | 1.0.15 | 3919 | UE4SS 1.0.3 |
| 6 | [Phantom Tweaks](https://www.nexusmods.com/phantombladezero/mods/44) | 1.1.1 | 2202 | UE4SS |
| 7 | [Instant Rest](https://www.nexusmods.com/phantombladezero/mods/263) | 1.0.2, bản bỏ hết animation | 1569 | |
| 8 | UE4SS fix, file phụ trên trang [Mods Menu](https://www.nexusmods.com/phantombladezero/mods/149) | 0.9.7 | 3702 | chỉ cài khi UE4SS ko khởi động |

Ko gói nào có file `.exe`. Có 3 file DLL, đều là bộ nạp mod: `dwmapi.dll` và `UE4SS.dll` của UE4SS, `hid.dll` của Mods Menu.

## Trước khi cài

1. Thoát game, kiểm process `PBZ.exe` ko còn chạy.
2. Xem `buildid` trong file `appmanifest` của PBZ ở `steamapps`. Khác 26367565 thì xem trang từng mod đã có bản cho build mới chưa rồi mới cài.
3. Kiểm `platform\steam` chưa có sẵn `hid.dll` và `dwmapi.dll`. Có sẵn thì dừng lại hỏi, đừng đè.
4. Backup save ra ngoài git, cách làm ở [doc tool save](pbz-tool-cai-dat-va-su-dung.md).
5. Pull repo private rồi so mã: `cd game-tuner-mods/phantom-blade-zero && sha256sum -c SHA256SUMS`.

## Cài theo thứ tự

"Thư mục game" là `...\steamapps\common\PBZ`, thư mục có `ProjectPBZ` và `platform`. File README, LICENSE, SHA256SUMS ở gốc mỗi gói ko cần chép vào game.

1. UE4SS: giải nén vào `platform\steam`, cạnh `PBZ.exe`. Xong phải có `platform\steam\dwmapi.dll` và `platform\steam\ue4ss\`.
2. Mods Menu: giải nén vào thư mục game. Gói thêm `platform\steam\hid.dll` và `ProjectPBZ\Content\JavaScript\PBZModsMenu\`.
3. Auto Collect Loot, Movement Speed: giải nén vào thư mục game. Mỗi mod thêm một thư mục trong `ProjectPBZ\Content\JavaScript\PBZModsMenu\Mods\`.
4. Map Tracker Plus, Phantom Tweaks: giải nén vào thư mục game. Mỗi mod thêm một thư mục trong `platform\steam\ue4ss\Mods\`.
5. Instant Rest (gói `.7z`): chép 3 file `zzz_PBZInstantRest_P.pak`, `.ucas`, `.utoc` vào `ProjectPBZ\Content\Paks\~mods`, chưa có `~mods` thì tạo.

## Kiểm sau khi cài

- Vào Settings của game: có tab Mods Menu, trong đó có Auto Collect Loot và Movement Speed.
- `platform\steam\ue4ss\UE4SS.log` có dòng `Starting Lua mod`. Nếu log lặp `Was unable to find AOB for 'GNatives'` hoặc `'GUObjectArray'`: thoát game, backup `platform\steam\ue4ss\UE4SS_Signatures`, giải nén gói số 8 vào thư mục game cho đè 2 file trong đó.
- Mods Menu và Phantom Tweaks cùng dùng phím F9 để mở bảng. Chưa kiểm trong game. Nếu giẫm nhau, đổi `PanelKey` trong `platform\steam\ue4ss\Mods\PhantomTweaks\settings.ini` rồi mở lại game.
- Mở map xem marker của Map Tracker Plus, ngồi nghỉ một lần xem Instant Rest đã bỏ animation.

## Gỡ

Thoát game rồi xoá:

- UE4SS và 2 mod dùng nó: `platform\steam\dwmapi.dll`, `platform\steam\ue4ss\`.
- Mods Menu và 2 mod dùng nó: `platform\steam\hid.dll`, `ProjectPBZ\Content\JavaScript\PBZModsMenu\`.
- Instant Rest: 3 file `zzz_PBZInstantRest_P.*` trong `ProjectPBZ\Content\Paks\~mods`.

Gỡ riêng một mod thì chỉ xoá thư mục của nó: `PBZModsMenu\Mods\PBZAutoCollect`, `PBZModsMenu\Mods\PBZMoveSpeed`, `ue4ss\Mods\PbzMapTracker`, `ue4ss\Mods\PhantomTweaks`. File cấu hình `.txt` của mod trong `Paks\~mods` giữ lại cũng ko sao.

Game update xong mà kẹt ở màn hình title hoặc crash lúc mở thì gỡ hết theo danh sách trên trước, rồi mới xem mod đã có bản mới chưa.

## Mã SHA-256

Khớp với mã VirusTotal mà Nexus ghi cho từng file.

```
974a95580d7d0e4ff4503dfe0032f87c8be0cb623a098a71ef48123b35c131de  1 UE4SS 1.0.3
ea0710e16a1468d975c035fe5cd0c2016d2018d0f656e58c0e3288df293d470a  2 Mods Menu 0.9.8
5ae4fa9285e1163e33fa04694f7d9665c0b7928cdcbda0d79507f6c885798085  3 Auto Collect Loot 1.8.0
214e7b262988d547ad92e5a913f41d6a0514ab811b217419a0d62e0d3ca788ba  4 Movement Speed 1.4.3
45dc32ec4f6e6dcaa83184ca960a5c6fc218a5f50559247371c1ab97d8556e6b  5 Map Tracker Plus 1.0.15
341e8b352c7943f58631be8a0a4f682e5739a71019c48589ed19f0bf4381a936  6 Phantom Tweaks 1.1.1
70446cfdf284e7b3559c60f7147f56dbc73a048cbc98f62a93d338a6b0337ebf  7 Instant Rest 1.0.2
84faea52294ef952f3554d3dc5f736406bb5b61838a0c82539337cdcf784b7f4  8 UE4SS fix 0.9.7
```
