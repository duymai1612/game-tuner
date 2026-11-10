# Phantom Blade Zero save tool

Luật chung của repo ở [../CLAUDE.md](../CLAUDE.md). Đọc [docs/pbz-tool-cai-dat-va-su-dung.md](docs/pbz-tool-cai-dat-va-su-dung.md) trước khi chạy tool. Checklist nhiệm vụ dễ lỡ của map 1 ở [docs/pbz-map-1-weeping-creek-valley-missables.md](docs/pbz-map-1-weeping-creek-valley-missables.md).

## Luật
- Chỉ sửa slot mà Continue load (`__Advanced__.LastContinueSlot`); tool mặc định làm vậy, `list` đánh dấu slot đó.
- Anh chỉ muốn bỏ phần cày: Dust và nguyên liệu nâng cấp. Ko tự ý thêm vũ khí chưa nhặt, mở skill, sửa cờ boss/quest hay `RemainingDays`; muốn sửa mấy thứ đó thì hỏi trước.
- Dust thêm vừa phải (vài chục nghìn mỗi lần), ko để vô hạn, để anh vẫn phải chọn nâng gì trước.
- Tên item lấy từ bảng `DT_InventoryData` trong file game, ko đoán theo ID. Item mới chưa có trong `MATERIALS` thì tra lại từ file game rồi mới thêm vào bảng.
- Key AES lấy từ `PBZ.exe` lúc chạy. Ko commit key, save hay file JSON dump vào repo.
- Repo GitHub có nhiều repo "PBZ trainer" cùng số sao, cùng ngày cập nhật, nhìn như mồi malware. Ko dùng và ko giới thiệu chúng. Nguồn tin cậy là PBZ-Editor (qry6868/PBZ-Editor, MIT).
- Guide nhiệm vụ: tên nhiệm vụ, bước và item lấy từ `Game.locres` và `PBZstory/PBZQuest/*` trong file game; deadline lấy từ guide cộng đồng, các nguồn lệch nhau thì ghi mốc sớm nhất.
