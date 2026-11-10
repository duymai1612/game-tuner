# game-tuner

Tool offline để sửa save, cùng guide cho các game single-player trên PC Steam. Dùng trên Windows qua WSL, một số tool chạy được trên Mac qua CrossOver.

| Game | Thư mục | Có gì |
|---|---|---|
| Elden Ring | [elden-ring/](elden-ring/) | Save editor (rune, stat, item, vũ khí), mở grace và map, reset boss, đọc `regulation.bin`, guide build và questline. [Cài đặt và sử dụng](elden-ring/docs/elden-ring-tools-cai-dat-va-su-dung.md) |
| Phantom Blade Zero | [phantom-blade-zero/](phantom-blade-zero/) | Đọc và sửa `PBZSaveGame.sav`: Remnant Dust, nguyên liệu nâng cấp. [Cài đặt và sử dụng](phantom-blade-zero/docs/pbz-tool-cai-dat-va-su-dung.md), [map 1: nhiệm vụ dễ lỡ](phantom-blade-zero/docs/pbz-map-1-weeping-creek-valley-missables.md) |

Repo này đổi tên từ `elden-ring-guides`. Link cũ trên GitHub vẫn tự chuyển về đây.

```bash
mkdir -p ~/game && cd ~/game
git clone https://github.com/duymai1612/game-tuner.git
```

Tất cả là tool cộng đồng, ko liên quan tới nhà phát triển game. Luôn thoát game trước khi sửa và giữ backup.
