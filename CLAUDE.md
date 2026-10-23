# Elden Ring guides và save tools

Trả lời bằng tiếng Việt. Repo dùng trên hai máy: máy Mac chạy game qua CrossOver, máy PC chạy Windows Steam và gọi tool qua WSL. Doc hay note nào nhắc CrossOver, bottle hay `.command` là chuyện của máy Mac.

Đọc [docs/elden-ring-tools-cai-dat-va-su-dung.md](docs/elden-ring-tools-cai-dat-va-su-dung.md) trước khi chạy tool. File đó có cách cài, đường dẫn save và `regulation.bin` trên từng máy, và lệnh của từng tool.

## Luật
- Nhân vật chính ở slot 1. Luôn `--slot 1`; chạy nhầm slot thì tool trả kết quả sai mà ko báo lỗi.
- Trước khi ghi save, kiểm process xem game đã thoát chưa, đừng tin lời "đã thoát". Sửa lúc game mở thì edit mất im lặng.
- Sửa xong, nhắc quy trình Steam Cloud: mở game, load nhân vật, thoát bằng menu, đợi sync. Ko đụng `remotecache.vdf`.
- Kiểm chứng là vào game nhìn tận mắt. Trước khi tin verdict của một probe, chạy nó trên một input đã biết đáp án.
- Flag boss lấy từ `regulation.bin` qua `elden_ring_param_dump.py`, ko đoán theo quy ước ID. Boss chính sống lại cần xoá cả bộ cờ, `respawn-boss` chỉ xoá một cờ.
- Tra wiki thì kéo wikitext thô qua MediaWiki API của `eldenring.wiki.gg`, ko tin bản tóm tắt của WebFetch; bản tóm tắt từng đảo ngược phần thưởng của một questline. Ảnh cho docs cũng lấy qua API đó, vì fextralife và fandom chặn.
- Repo public: ko commit save, SteamID, username Windows hay đường dẫn chứa chúng. Save backup để ngoài git.
