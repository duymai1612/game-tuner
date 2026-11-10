# Backhand Blade: option nào ngon hơn - báo cáo deep research

Nhân vật `dyu` (slot 1, Lv 713, cả 8 stat 99) | 2026-08-14
Nguồn: Perplexity Deep research (15 nguồn) + Brave/WebSearch + phản biện đa mô hình (3 Codex trả lời, Gemini và Grok timeout).
Phiên bản game: nguồn dẫn từ 1.13.1 tới **Regulation 1.16.1**.

---

## TL;DR

**Giữ `Backhand Blade` Blood +25 đang có.** Nó là lựa chọn đúng cho lối chơi deflect, vì
`Curseblade's Cirque` dính bug khiến `Deflecting Hardtear` và `Curved Sword Talisman` **không
cộng vào guard counter** của nó - đúng hai thứ mà build deflect sống nhờ.

Nhưng câu "Cirque kém hơn hoàn toàn" là **sai**: nó có **45 Guard Boost so với ~15**, tức đỡ đòn
an toàn hơn hẳn khi bấm deflect trượt. Đó là vũ khí để *học* deflect, không phải để tối đa sát thương.

Biến thể đáng thử hơn cả hai option trong video: **powerstance hai cây Backhand Blade**, vốn là
trạng thái mặc định của lớp vũ khí này khi cầm hai tay.

---

## Findings

### 1. Blood thắng đua bleed, nhưng KHÔNG đương nhiên thắng tổng sát thương `[đã sửa sau phản biện]`

Nhận định ban đầu của tôi - "99 Arcane làm Blood vượt hẳn Keen + Bloodflame Blade" - bị **cả 3
model Codex bác cùng một chỗ**:

- Bleed có soft cap ở **25 / 45 / 60 Arcane**. Tới 60 Arcane đã đạt ~90% khả năng scale. Đi từ
  60 lên 99 chỉ thêm khoảng **114 → 117 bleed**. Tức 99 Arcane gần như là scaling chết. `[đồng thuận 3/3]`
- `Bloodflame Blade` không chỉ cho 40 bleed phẳng: nó còn cộng **Fire AR bằng 40% incantation
  scaling theo Faith của seal**. Ở 99 Faith đó là sát thương thật, không nhỏ. `[đồng thuận 3/3]`

Kết luận đúng: **Blood thắng rõ ở tốc độ proc bleed**; còn tổng damage thì tuỳ boss và tuỳ seal,
chưa có bằng chứng Blood thắng phổ quát.

### 2. `Curseblade's Cirque` không "kém hơn hoàn toàn" `[đã sửa sau phản biện]`

| | Backhand Blade | Curseblade's Cirque |
|---|---|---|
| Trần nâng cấp | +25 (Smithing) | +10 (Somber) |
| Infuse / buff | được | **không** cả hai |
| Bleed nội tại | không (Blood affinity thì có, scale Arcane) | có, **cố định**, không scale Arcane |
| **Guard Boost** | ~15-16.5 | **45** |
| Skill | Blind Spot (đổi được) | Deadly Dance (khoá) |

Guard Boost gấp 3 là ưu thế thật cho người đang tập deflect: bấm trễ một nhịp thì Cirque vẫn đỡ
được, Backhand Blade thì không. `[đồng thuận 3/3]`

Về bleed thì Cirque thua chắc: bleed cố định, 99 Arcane vô dụng với nó.

⚠️ **Số bleed nội tại của Cirque đang tranh cãi**: Perplexity ghi 82, một model Codex ghi 45.
Chưa nguồn nào thắng. Không ảnh hưởng kết luận vì cả hai đều không scale.

### 3. Bug guard counter của Cirque - điểm quyết định cho câu hỏi deflect `[một nguồn]`

Trên `Curseblade's Cirque`, `Deflecting Hardtear` và `Curved Sword Talisman` **không cộng vào
guard counter** (wiki commenter, còn tồn tại tới ít nhất 1.13.1). Bản **1.14 đã sửa** lỗi tương
tự cho `Backhand Blade` thường.

Đây là lý do chính khiến Backhand Blade thắng cho build deflect - nhưng nó **chỉ có một nguồn**
(Perplexity dẫn bình luận wiki), ba model Codex không xác nhận cũng không bác. Cần kiểm trong game
nếu muốn chắc.

### 4. Blood chặn grease và phép bôi vũ khí, KHÔNG chặn Golden Vow `[đã sửa sau phản biện]`

Chỉ **Standard / Heavy / Keen / Quality** nhận được weapon buff (grease, `Bloodflame Blade`).
Blood/Occult/Cold/Magic/Fire/Lightning/Sacred/Poison thì không. `[đồng thuận nhiều nguồn]`

Nhưng tôi đã nói sai một ý: `Golden Vow` **vẫn dùng được** với vũ khí Blood, vì nó là aura lên
người chứ không phải buff lên vũ khí. Mọi body buff đều thế. `[đồng thuận 3/3]`

### 5. Occult: cao AR nhất ở 99 Arcane, nhưng không thêm bleed

Perplexity: Occult có **A-rank Arcane scaling** so với **D-rank** của Blood, nên ở 99 Arcane
Occult cho AR thô cao hơn. Nhưng Backhand Blade **không có bleed nội tại**, mà Occult chỉ khuếch
đại bleed sẵn có - nên Occult không thêm status. `[đồng thuận]`

Công dụng thật của Occult ở đây: **đánh boss miễn nhiễm bleed**, nơi Blood thành vô dụng.

⚠️ Bảng AR của Perplexity (Standard 257 / Keen 220 / Occult 225 / Blood 215) là **damage gốc ở
mức nâng cấp tối đa, chưa gồm scaling**. Ở 99 stat thì phần scaling mới quyết định, nên đừng đọc
bảng đó như xếp hạng cuối cùng.

### 6. Biến thể đáng thử: powerstance hai cây

Backhand Blade khi cầm hai tay **tự nhân đôi sang tay trái** - powerstance là trạng thái mặc định
của lớp này. Cộng đồng xếp **dual Backhand Blade + Blind Spot (hoặc Swift Slash)** là cấu hình
mạnh nhất lớp, và cả hai lưỡi mang cùng buff/status cùng lúc.

`Smithscript Cirque` thì tôi đã đánh giá quá cao: model Codex chỉ ra scaling của nó dựa một phần
vào **bug bản launch**, và stance damage gần như bằng 0 (8 so với 33 tối thiểu của vũ khí khác).
`[đồng thuận, hạ khuyến nghị]`

---

## Bất đồng chưa giải quyết

| Điểm | Hai phía | Cách chốt |
|---|---|---|
| Bug guard counter của Cirque | Perplexity + wiki commenter nói có; 3 Codex không đề cập | Thử trong game: đánh có/không Curved Sword Talisman, so số |
| Bleed nội tại Cirque | 82 (Perplexity) vs 45 (Codex terra) | Đọc trong game |
| Occult vs Blood tổng damage ở 99 stat | Occult cao AR (Perplexity) vs Blood thắng vì proc (Codex) | Rèn thử rồi đọc AR ngay trong menu |

## Câu hỏi còn mở

- Không nguồn nào có số AR đo thật ở đúng 99/99/99/99. Con số cộng đồng gần nhất là 14 Str/80 Dex:
  Backhand Blade 579 AR vs Cirque 603 AR - Cirque nhỉnh hơn ở mức stat đó.
- Chưa xác minh `Deflecting Hardtear` có cộng damage cho guard counter của Backhand Blade ở
  Regulation 1.16.1 hay không; nguồn chỉ nói tới 1.14.
