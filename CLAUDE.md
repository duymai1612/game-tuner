# game-tuner

Trả lời bằng tiếng Việt. Repo gom tool sửa save và guide cho các game anh chơi, mỗi game một thư mục, mỗi thư mục có `CLAUDE.md` riêng. Repo dùng trên hai máy: máy Mac chạy game qua CrossOver, máy PC chạy Windows Steam và gọi tool qua WSL.

- [elden-ring/](elden-ring/CLAUDE.md): save editor, grace/boss tool, guide build và questline.
- [phantom-blade-zero/](phantom-blade-zero/CLAUDE.md): tool sửa save PBZ.

## Luật chung
- Repo public: ko commit save, SteamID, username Windows hay đường dẫn chứa chúng. Save backup để ngoài git.
- Trước khi ghi save, kiểm process xem game đã thoát chưa, đừng tin lời "đã thoát". Sửa lúc game mở thì game ghi đè mất edit mà ko báo lỗi.
- Sửa xong, nhắc quy trình Steam Cloud: mở game, load save, kiểm tận mắt, thoát bằng menu, đợi sync. Ko đụng `remotecache.vdf`.
- Kiểm chứng là vào game nhìn tận mắt. Tool báo đọc lại OK chưa có nghĩa là game nhận.
- Thêm game mới thì tạo thư mục `<ten-game>/` với `CLAUDE.md` và doc cài đặt riêng, rồi thêm một dòng vào danh sách trên và vào `README.md`.
