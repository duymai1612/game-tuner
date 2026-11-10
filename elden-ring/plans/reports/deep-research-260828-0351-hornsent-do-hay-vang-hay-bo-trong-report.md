# Hornsent questline: đỏ, vàng, hay bỏ trống - chọn gì trong NG0

Ngày 2026-08-28 · nhân vật `dyu` slot 1 Lv713 · save đọc lúc 03:18 cùng ngày
Nguồn gốc: wikitext thô từ `eldenring.wiki.gg` API (không qua bản tóm tắt), đối chiếu PowerPyx +
Fextralife + Game8. Validate đối kháng: `gpt-5.6-sol` + `gpt-5.6-terra` qua Codex CLI.

---

## TL;DR

**Bỏ trống cả hai dấu.** Rồi triệu hồi Hornsent ở trận Messmer, và tới màn Leda đấu Ansbach thì
đứng về phía Ansbach.

Lý do một câu: mọi thứ nhánh "bỏ trống" đánh mất đều là talisman và Ash of War, tức là đúng hai
loại tool `elden_ring_save_editor.py` bơm được miễn phí; còn thứ nó giữ lại được là **vũ khí**,
loại duy nhất tool không tạo mới được mà phải hy sinh một cây khác.

Nhánh vàng là nhánh tệ nhất, ngược hẳn với câu trả lời tôi đưa lúc 03:20. Trang
[`Ash of War: Swift Slash`](https://eldenring.wiki.gg/wiki/Ash_of_War%3A_Swift_Slash) ghi thẳng nó
*"mutually exclusive with Ansbach's Longbow, Lacerating Crossed-Tree, and Retaliatory Crossed-Tree,
and ends Leda's questline until Enir-Ilim"*. Giúp Hornsent là **cắt luôn màn Leda đấu Ansbach**,
mất `Ansbach's Longbow`.

Và chưa được đánh Messmer. Bước vào phòng boss là hai dấu biến mất, kể cả chưa đánh.

---

## Ba nhánh làm gì

Dấu nằm ở Shadow Keep, trên tường thành ngay trước grace `Storehouse, First Floor`, chỗ đám
thuyền cháy. Điều kiện xuất hiện: Miquella's Great Rune đã vỡ, và đã nói chuyện để Leda chốt
mục tiêu là Hornsent (chọn "Hornsent" hoặc "không ai" đều ra Hornsent).

| | Đỏ - giúp Leda | Vàng - giúp Hornsent | Bỏ trống |
|---|---|---|---|
| Hornsent | chết tại chỗ | sống | sống |
| Thưởng ngay | `Falx` + `Hornsent Set` | `Ash of War: Swift Slash` + `Leda's Rune` | không |
| Talisman từ Leda | `Lacerating Crossed-Tree` | không | không |
| Triệu hồi Hornsent ở Messmer | mất | được | được |
| Hornsent invade ở Church of the Bud | mất | được | được |
| **Leda đi tìm Ansbach** | **có** | **KHÔNG** | **có** |

Dòng cuối là dòng quyết định. Nguyên văn wiki.gg trang `Needle Knight Leda` bước 6:
*"If nothing is done and Hornsent is summoned against Messmer, Leda will go after Ansbach."*
Trang `Swift Slash` nói rõ hơn: nhánh vàng *"ends Leda's questline until Enir-Ilim"*.

`Falx` và `Hornsent Set` rơi ở **cả ba nhánh**, chỉ khác chỗ. Đỏ thì rơi ngay Shadow Keep, hai
nhánh kia rơi ở màn Hornsent invade tại Church of the Bud. Nên vũ khí Hornsent không hề bị treo.

## Bảng sổ item, xếp theo thứ bơm được hay không

Đây là chỗ quyết định, vì tool của anh không đối xử đều với mọi loại item.

| Món | Loại | Bơm bằng tool? | Đỏ | Vàng | Bỏ trống |
|---|---|---|---|---|---|
| `Ansbach's Longbow` | **vũ khí** | `replace-weapon`, **tốn một cây donor** | ✅ | ❌ | ✅ |
| `Obsidian Lamina` | **vũ khí** | `replace-weapon`, tốn donor | ✅¹ | ❓ | ✅¹ |
| `Falx` | vũ khí | tốn donor | ✅ | ✅ | ✅ |
| `Hornsent Set` (4 món) | giáp | `replace-armor`, tốn donor | ✅ | ✅ | ✅ |
| `Ansbach's Set` + `Wise Man's Mask` | giáp | tốn donor | ✅² | ❓ | ✅² |
| `Lacerating Crossed-Tree` | talisman | **`add-item` id 8140, miễn phí** | ✅ | ❌ | ❌ |
| `Retaliatory Crossed-Tree` | talisman | **`add-item` id 8130, miễn phí** | ✅³ | ❌ | ✅³ |
| `Ash of War: Swift Slash` | AoW | **`add-aow` id 410000, miễn phí** | ❌ | ✅ | ❌ |
| `Furious Blade of Ansbach` | incantation | **`add-item`, miễn phí** | ✅¹ | ❓ | ✅¹ |
| `Furnace Visage` x3 | goods | **`add-item`, miễn phí** | ❌ | ✅ | ✅ |

¹ chỉ khi giúp Ansbach ở màn đấu, rồi nhặt xác anh ta sau trận Radahn
² chỉ khi giúp Leda giết Ansbach
³ chỉ khi giúp Leda giết Ansbach

Đọc bảng theo cột: nhánh vàng mất một **vũ khí** (`Ansbach's Longbow`) để đổi lấy một **AoW** bơm
được miễn phí. Đó là một cuộc đổi chác lỗ, không có mặt nào bù lại. Nhánh đỏ và bỏ trống ngang
nhau về vũ khí, khác nhau ở chỗ đỏ giết Hornsent sớm nên mất phần đuôi questline của anh ta để
lấy một talisman cũng bơm được miễn phí.

Xếp hạng: **bỏ trống > đỏ > vàng.**

## Thứ tự việc còn phải làm

Save hôm nay không có `Messmer's Kindling`, không có `Remembrance of the Impaler` → **Messmer chưa
chết**. Đang giữ sẵn `Scorpion Stew` x1 và `Thiollier's Concoction` x1.

**Trước khi mở cửa phòng Messmer**

1. Backup save khi game đã tắt hẳn.
2. Ra Shadow Keep, chỗ thuyền cháy, **xác nhận hai dấu có thật ở đó**. Nếu không thấy, đừng đoán
   lý do: có thể anh đã bước vào phòng Messmer rồi, hoặc chưa nói chuyện đủ với Leda ở Highroad
   Cross để cô chốt mục tiêu.
3. Đưa `Scorpion Stew` cho Hornsent → `Furnace Visage` x3.
4. **Không bấm dấu nào cả.**
5. Chuỗi Storehouse, đúng thứ tự này: gặp Freyja tầng 7 → hỏi Ansbach **về Freyja trước** → mới đưa
   `Secret Rite Scroll` → nhận `Letter to Freyja` → đưa Freyja → `Golden Lion Shield` → báo lại
   Ansbach. Đưa scroll trước khi hỏi về Freyja là gãy mạch thư.
6. Dọn nốt Dryleaf Dane (đấu tay đôi ở Moorth Ruins), Moore (chọn "Remain sad forever"), Thiollier
   / St. Trina.

**Trận Messmer**

7. Triệu hồi Hornsent trong trận, và phải là **lượt thắng**. Đây là điều kiện kép: vừa mở màn
   invade ở Church of the Bud, vừa là điều kiện để Leda chuyển mục tiêu sang Ansbach.

**Sau Messmer, trước khi đốt Sealing Tree**

8. Quay lại Leda ở Highroad Cross, cô sẽ nhắm Ansbach.
9. Ở phòng cũ của Ansbach tại `Storehouse, First Floor`, **bấm dấu vàng giúp Ansbach**. Được
   `Ansbach's Longbow` + `Leda's Rune`, Ansbach sống, triệu hồi được ở Enir-Ilim và ở Radahn,
   và sau trận Radahn nhặt xác được `Ansbach's Set` + `Obsidian Lamina` + `Furious Blade of Ansbach`.
10. Đi bộ từ `Rauh Ancient Ruins, West` lên cầu thang tới `Church of the Bud, Main Entrance` để
    kích màn Hornsent invade → `Falx` + `Hornsent Set`. Đừng warp thẳng vào grace.
11. Đốt Sealing Tree cuối cùng. Đây là điểm không quay lại của toàn bộ NPC.

**Bơm bù sau khi xong**: `add-item` talisman 8140 và 8130, `add-aow` 410000. Bơm sau chứ đừng bơm
trước, tránh trường hợp game vẫn định trao món đó.

## Chỗ cần sửa trong doc

`docs/elden-ring-dlc-questline-checklist-va-quest-path.md:152` ghi triệu hồi Hornsent làm đồng minh
ở trận Leda tại Enir-Ilim. Sai. Bảng `Cooperators` của wiki.gg liệt kê đồng minh cho
`Miquella's Followers` tại Enir-Ilim chỉ gồm `Sir Ansbach`, `Thiollier`, và `Sanguine Noble Nataan`
(thế chỗ khi Ansbach chết). Không có Hornsent. Hornsent ở đó luôn là địch, và chỉ xuất hiện nếu
còn sống.

Dòng `:186` ghi *"Chọn dấu đỏ của Leda. Người bị săn chết luôn"* thì đúng, nhưng thiếu vế quan
trọng hơn: nhánh **vàng** mới là nhánh cắt cụt questline Leda và mất `Ansbach's Longbow`.

Dòng `:22` ghi Messmer "ít nhất đã chạm" dựa trên `Ember of Messmer` trong túi. Ember rơi từ lính
trong Shadow Keep, không chứng minh đã vào phòng boss. Trạng thái đó phải kiểm bằng mắt trong game.

---

## Bất đồng giữa các nguồn

**Game8 đảo ngược phần thưởng hai nhánh.** Bản Game8 tôi đọc gán `Swift Slash` cho nhánh đỏ và
`Lacerating Crossed-Tree` cho nhánh vàng. Sai. wiki.gg, PowerPyx, Fextralife và GameRant đều thống
nhất ngược lại, và trang acquisition của chính hai món đó nói rõ: `Lacerating Crossed-Tree` là
*"assisting her in assassinating the vengeful Hornsent"*, `Swift Slash` là *"using a golden summon
sign to aid him"*.

**Fextralife nói nhánh vàng vẫn dẫn tới Ansbach.** Trang `Needle Knight Leda` của Fextralife mô tả
"Path B: Support Hornsent → Leda then targets Ansbach". wiki.gg mâu thuẫn trực tiếp với câu đó.
Tôi theo wiki.gg vì nó phát biểu ở dạng phủ định tường minh trên trang `Swift Slash`
(*"mutually exclusive with Ansbach's Longbow"*, *"ends Leda's questline until Enir-Ilim"*), trong
khi Fextralife chỉ là một dòng mô tả xuôi. Cả hai model Codex chạy độc lập cũng đọc ra kết luận
của wiki.gg. **Nếu anh muốn chắc chắn tuyệt đối thì nhánh bỏ trống an toàn hơn cả**, vì nó nằm
đúng vào cái case mà wiki.gg phát biểu khẳng định, không phụ thuộc việc ai đúng.

**`Obsidian Lamina` + `Furious Blade of Ansbach` ở nhánh vàng: chưa rõ.** Trang
`Furious Blade of Ansbach` điều kiện hoá phần thưởng vào *"siding with him against Needle Knight
Leda"*. Nhánh vàng không hề có màn đấu đó để mà đứng phe. Không tìm được nguồn nào nói thẳng
chuyện gì xảy ra khi màn đấu không tồn tại. Đây là lý do nữa để tránh nhánh vàng.

## Câu hỏi chưa giải quyết

- Hai dấu ở Shadow Keep còn hay mất? Không đọc được từ save, phải nhìn trong game.
- Leda đã chốt mục tiêu Hornsent chưa? Cũng không đọc được từ save. Nếu chưa, phải nói chuyện
  cạn với cô ở Highroad Cross rồi ngồi grace trước.
- `Secret Rite Scroll` không có trong túi. Chưa nhặt, hay đã đưa Ansbach rồi? Không phân biệt được
  từ inventory.
- Nhánh vàng có giữ được `Obsidian Lamina` / `Furious Blade of Ansbach` không (xem trên).
- Patch 1.17 ra ngày 2026-08-27, một ngày trước hôm nay. Bản patch note chính thức không nhắc quest,
  nhưng tôi chưa đối chiếu từng dòng. Chạy `selftest` trước khi ghi save nếu game đã tự cập nhật.
