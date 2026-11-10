# Boss nào đánh thoải mái mà không hỏng tiến trình và questline

Ngày soát: 2026-08-28 | Nhân vật `dyu` slot 1 | Save đọc trực tiếp lúc 03:35
Trạng thái: cờ boss + inventory + grace đọc thẳng từ `ER0000.sl2`.
Luật game: 5 hướng research song song trên wiki.gg / Fextralife / PowerPyx / Game8, mỗi hướng qua
một pass phản biện bắt buộc bác bỏ. 9/13 claim bị pass đó sửa, các mục dưới là bản đã sửa.

---

## TL;DR

Base game: **giết gì cũng được, kể cả Maliketh.** Maliketh chết là Leyndell Royal Capital thành
Ashen Capital và đồ chưa nhặt trên mặt thành mất vĩnh viễn, nhưng soát lại thì anh đã nhặt hết
(`Bolt of Gransax`, `Coded Sword`, `Erdtree Bow`, `Sanctified Whetblade`, Lionel's, Alberich's),
Boc xong, Corhyn/Goldmask đã tới Mountaintops, Bernahl đã cho `Blasphemous Claw`, Gideon đã nộp
đủ 4 khám phá, Enia đã cho `Talisman Pouch`. Không còn gì để mất.

Trái với tin đồn, **đốt cây không biến Leyndell thành Ashen Capital, Maliketh mới làm** - nên
việc anh đã đốt cây không hề chôn thành.

DLC: trong 6 boss remembrance còn sống, **Midra và Commander Gaius đánh thoải mái**, cộng toàn
bộ boss field/hang/gaol. Bốn con còn lại là công tắc: Metyr, Messmer, Romina (nhẹ), Promised
Consort Radahn.

Cái nguy hiểm nhất không phải giết boss mà là **bước qua cửa sương phòng Messmer**: chưa cần
đánh, chỉ vào phòng là hai dấu triệu hồi Leda-vs-Hornsent ở Shadow Keep mất vĩnh viễn.

Và đốt Sealing Tree **không xoá sổ questline** như doc đang ghi. NPC dời vào Enir-Ilim và quest
kết thúc ở đó. Cái thật sự mất là các bước thoại còn dở ngoài overworld và 7 cuốn Forager Brood
Cookbook.

---

## Trạng thái save (khác doc hiện tại)

**Base game - 98/157 boss.**

| Việc | Trạng thái | Bằng chứng |
|---|---|---|
| Fire Giant | chết | cờ `1052520800` |
| Đốt Erdtree | **rồi** | anh xác nhận; Farum Azula 11/11 grace + Godskin Duo `13000850` chết |
| Bernahl (Farum Azula) | chết | `Devourer's Scepter` + bộ Beast Champion |
| **Maliketh** | **còn sống** | cờ `13000800` |
| Placidusax / Gideon / Hoarah Loux / Radagon | còn sống | `13000830` `11050850` `11050800` `19000810` |
| Leyndell Ashen Capital | 0/6 grace | đúng, vì Maliketh còn sống |

**DLC - đi xa hơn doc ghi nhiều.** Doc đánh ⬜ cho gần hết Chương 3-6. Inventory nói khác:

| Questline | Doc ghi | Save nói |
|---|---|---|
| **Igon** | ⬜ chưa | **xong** - nguyên bộ `Igon's Helm/Armor/Gauntlets/Loincloth` là đồ sở hữu thật, cộng `Igon's Bell Bearing` + `Igon's Furled Finger` |
| **Dryleaf Dane** | ⬜ chưa | **xong** - `Dryleaf Arts +25`, `Dane's Hat` |
| **Hornsent Grandam** | ⬜ chưa | **xong tới mốc 2** - `Divine Beast Head` + `Scorpion Stew` |
| **St. Trina / Thiollier** | ⬜ chưa | **xong nhánh invade** - `St. Trina's Smile` |
| **Ansbach ↔ Freyja** | ⬜ chưa | **xong mạch thư** - `Golden Lion Shield +10` |
| **Moore** | ⬜ chưa | **chưa** - `Verdigris` trong save là bản NPC ông đang mặc |
| **Ymir + Jolán** | ⬜ chưa | **chưa** - không có `Maternal Staff`, `High Priest Set`, `Ymir's Bell-Bearing` |

Cách đọc: `list-armor` in `[orphan]` cho đồ gắn NPC được triệu hồi chứ không nằm trong túi.
`Verdigris`, `Leda's Armor`, `Thiollier's` đều `[orphan]`. `Igon's` thì không, nên là đồ thật.

`Miquella's Great Rune` đang trong túi - rơi từ Scadutree Avatar. Trang bị nó ở trận Promised
Consort Radahn để phá bùa mê phase 2. Nó **tự kích hoạt sẵn**, không cần đi Divine Tower như
mọi Great Rune khác.

**Cờ boss DLC - đọc trực tiếp được rồi.** 42 ID lấy từ `EventFlags.json` của Smithbox, đã nạp
vào `plans/260729-1313-eldenring-event-flag-re/boss-flag-ids.tsv` nên `boss-report` giờ in cả
DLC: **112/199**. Xác thực bằng 5 control độc lập (Rellana, Bayle, Dancer of Ranah, Dryleaf Dane,
Rakshasa - đều phải DEAD theo đồ trong túi, và cả 5 đều ra DEAD).

Lưu ý: file TSV gốc thiếu newline cuối, đã sửa luôn.

| Boss | Cờ | Trạng thái |
|---|---|---|
| Divine Beast Dancing Lion (Belurat) | `20000800` | **chết** |
| Rellana | `2048440800` | **chết** |
| Putrescent Knight | `22000800` | **chết** |
| Golden Hippopotamus | `21000850` | **chết** |
| Scadutree Avatar | `2050480800` | **chết** |
| Bayle the Dread | `2054390800` | **chết** |
| Dancer of Ranah | `2046380800` | **chết** |
| Jagged Peak Drake Duo | `2052400800` | **chết** |
| Death Knight (Scorpion River) | `40010800` | **chết** |
| Commander Gaius | `2049480800` | còn sống |
| Metyr, Mother of Fingers | `25000800` | còn sống |
| Midra, Lord of Frenzied Flame | `28000800` | còn sống |
| **Messmer the Impaler** | `21010800` | còn sống |
| **Romina, Saint of the Bud** | `2044450800` | còn sống |
| **Promised Consort Radahn** | `20010800` | còn sống |
| Jagged Peak Drake | `2049410800` | còn sống |
| Knight of the Solitary Gaol | `2046410800` | còn sống |
| Death Knight (Fog Rift) | `40000800` | còn sống |

Golden Hippopotamus chết là bằng chứng cứng: mốc "Miquella's Great Rune vỡ" **chắc chắn đã qua**.

---

## Base game: giết gì cũng được

**Thoải mái:** toàn bộ evergaol, catacomb, hang, tunnel, boss field, Night's Cavalry, Death Rite
Bird, Tree Sentinel, Erdtree Avatar, rồng (Placidusax, Greyoll, Ekzykes, Greyll), Astel bản
Yelough Anix, Ancestor Spirit, Regal Ancestor Spirit, Vyke, Mohg the Omen ở Cathedral of the
Forsaken, Fell Twins, Godskin các bản. Questline base game xong 100% nên không còn NPC để hỏng.

Bell Bearing Hunter cũng an toàn: thương nhân chỉ biến mất trong lúc đánh, thắng hay chết đều
quay lại. Không mất merchant nào.

**Maliketh: cửa một chiều, nhưng với anh thì đã sạch.**

Giết Maliketh → Leyndell Royal Capital thành Ashen Capital → mọi đồ chưa nhặt trên mặt thành
cũ mất vĩnh viễn. Soát toàn bộ danh sách missable của thành thì anh **có đủ**:
`Bolt of Gransax +10`, `Coded Sword +10`, `Erdtree Bow +10`, `Sanctified Whetblade` (món wiki
cảnh báo gắt nhất, tầng 2 Fortified Manor), `Talisman Pouch` x3, `Blasphemous Claw`, nguyên bộ
`Lionel's`, nguyên bộ `Alberich's`. Boc xong, Corhyn/Goldmask đã đẩy tới Mountaintops, Gideon đã
nộp đủ 4 khám phá (`Black Flame's Protection`, `Lord's Divine Fortification`,
`Fevor's Cookbook [3]`, `Law of Causality` đều trong túi).

Không còn món nào bị đe doạ.

`Golden Order Seal` vẫn thiếu nhưng **không liên quan Maliketh**: nó ở Minor Erdtree Church trên
Altus Plateau, tây nam Leyndell, không phải trong thành. Nhặt lúc nào cũng được.

Những thứ **không** mất, trái với tin đồn:
- **Enia vẫn đổi remembrance được** dù chết trong hoạt cảnh - xác vẫn tương tác, vẫn bán giáp boss
- **Gurranq không biến mất**, Bestial Sanctum vẫn mở
- **Subterranean Shunning-Grounds và Divine Bridge vẫn vào được** ở Ashen Capital
- Roderika, Hewg, Twin Maiden Husks sống tới hết game
- Vẫn lên level bình thường sau khi Melina chết

Maliketh còn là bắt buộc nếu muốn `Mending Rune of Perfect Order` - xác Goldmask chỉ hiện ở
Ashen Capital, trên dốc gần đấu trường.

Sau Maliketh: Gideon → Hoarah Loux → Radagon/Elden Beast. Chỉ là kết game.

---

## DLC: thoải mái vs công tắc

### Đánh thoải mái

Còn sống và đánh lúc nào cũng được:

| Boss | Ghi chú |
|---|---|
| **Midra** | Hoàn toàn trơ. **Không dính Frenzied Flame ending** - ending đó chỉ gate ở Three Fingers dưới Shunning-Grounds. Anh bỏ Frenzied Flame thì Midra vô hại |
| **Commander Gaius** | Trơ. Chỉ là cửa vào Scaduview |
| **Jori, Elder Inquisitor** | Trơ. Cửa duy nhất vào Abyssal Woods để tới Midra |
| **Knight of the Solitary Gaol** | Trơ. `Greatsword of Solitude` + bộ Solitude |
| **Death Knight (Fog Rift)** | Trơ |
| **Jagged Peak Drake** | Là bước 2 của mạch Igon, nhưng anh xong Igon rồi nên giờ vô hại |

Đã hạ rồi, không khoá gì: Divine Beast Dancing Lion, Rellana, Putrescent Knight, Golden
Hippopotamus, Scadutree Avatar, Bayle, Dancer of Ranah.

**Boss field/hang/gaol trơ hết** (24 con, soát từng con trên wiki.gg): Knight of the Solitary
Gaol (tên mới của Blackgaol Knight), Rakshasa, Red Bear, Ghostflame Dragon cả 3 con, Chief
Bloodfiend, Black Knight Edredd, Black Knight Garrew, Curseblade Labirith, Lamenter, Ancient
Dragon Senessax, Demi-Human Swordmaster Onze, Demi-Human Queen Marigga, Rugalea, Fallingstar
Beast, Torch Tree Sentinel, cả hai Death Knight, Bloodfiend Chief ở Bonny Village, Death Rite
Bird ở Charo's Hidden Grave, và **Divine Beast Dancing Lion bản Ancient Ruins of Rauh** (dấu
triệu hồi Freyja và cờ Grandam chỉ gắn bản Belurat).

Dragon Heart rơi từ 3 con Ghostflame Dragon và 2 con Jagged Peak Drake. Ancient Dragon Senessax
cho smithing stone chứ không cho Dragon Heart.

Hai ngoại lệ trong nhóm field, đều thuộc mạch Igon nên với anh là **moot vì đã xong**:
Jagged Peak Drake (giết nó là Igon xuất hiện) và Ancient Dragon-Man (giữ đường lên Jagged Peak).

**Swordhand of Night Anna** thuộc mạch Ymir, nhưng cũng không đi săn lẻ được: cô ấy chỉ invade ở
Finger Ruins of Miyr, mà Miyr chỉ mở khi đã rung chuông Rhia và Dheo.

### Bốn công tắc

**🔴 Messmer - nguy hiểm nhất, và nó cắn TRƯỚC khi anh đánh.**

Chỉ cần **bước vào phòng boss** từ grace Dark Chamber là hai dấu triệu hồi Leda-vs-Hornsent ở
Shadow Keep (khu battlements có thuyền cháy, ngay trước thang máy lên Storehouse First Floor)
mất vĩnh viễn, mất luôn `Lacerating Crossed-Tree Talisman` hoặc `Ash of War: Swift Slash`.
Grace Dark Chamber nằm trong 105 grace anh mở sẵn, warp nhầm một phát là dính.

Giết Messmer thì thêm: bỏ qua phần còn lại questline Hornsent nếu không triệu hồi anh ta, và
**đóng questline Hornsent Grandam** - `Gourmet Scorpion Stew` phải lấy trước khi Messmer chết
(wiki Watchful Spirit ghi thẳng "Must be done before defeating Messmer the Impaler").

Trước Messmer phải chốt ngã ba **Leda vs Hornsent**. Ba nhánh, không phải hai:
- **Dấu vàng** giúp Hornsent: được `Lacerating Crossed-Tree`, nhưng Leda biến mất tới Enir-Ilim,
  Ansbach không xuất hiện ở phòng thư viện Storehouse, mất `Ansbach's Longbow`
- **Dấu đỏ** giúp Leda: Hornsent chết ngay tại Shadow Keep, không triệu hồi được cho Messmer,
  đổi lại `Retaliatory Crossed-Tree` và mở trận Ansbach-vs-Leda
- **Bỏ trống cả hai**: mất cả hai talisman lẫn `Ash of War: Swift Slash`, nhưng giữ được cả
  Hornsent (triệu hồi cho Messmer) lẫn trận Ansbach-vs-Leda

Phân tích riêng cho ngã ba này, kèm lý do chọn "bỏ trống" ở NG0 của anh:
`plans/reports/deep-research-260828-0351-hornsent-do-hay-vang-hay-bo-trong-report.md`

**🔴 Metyr, Mother of Fingers.** Giết Metyr là xoá dấu triệu hồi Jolán (kể cả dấu ở trận Messmer),
và quay lại Cathedral of Manus Metyr là bị ép đánh Jolán rồi Ymir, kết questline.
**Mua hết 9 phép của Ymir trước, 80.500 rune** - shop chết theo ông.

**🟡 Romina.** Bản thân vô hại, giết xong không NPC nào dời. Nhiều guide gọi Romina là point of
no return nhưng đó là thứ tự chứ không phải nhân quả: PowerPyx và Game8 đều nói thẳng cái khoá là
đốt Sealing Tree. Giết Romina xong cứ đứng cạnh cây bao lâu cũng được.

Lưu ý: Hornsent invade ở **cầu thang trước** đấu trường Romina, không phải sau.

**🔴 Promised Consort Radahn.** Hết DLC.

### Đốt Sealing Tree: doc đang ghi quá nặng

Doc ghi "mọi questline chưa xong tới lúc đó thì hỏng vĩnh viễn". Sai. Enir-Ilim **chỉ vào được
sau khi đốt cây**, và Leda, Ansbach, Freyja, Hornsent, Moore, Dane, Thiollier đều có mặt bên
trong - questline của họ **kết thúc ở đó**. Phần thưởng lớn nằm sau mốc đốt:
`Ansbach's Longbow` + `Leda's Rune` từ trận duel, bộ Ansbach + `Furious Blade of Ansbach` từ xác
sau boss cuối, bộ Hornsent từ xác ở Enir-Ilim, `Thiollier's Hidden Needle` + bộ giáp của anh ta.

Câu "chỉ ba nhánh còn làm được sau đó" (Queelign, Ymir/Jolán, Igon/Priestess) là nói ba nhánh
còn **ngoài overworld**, không phải bảy nhánh kia bị xoá.

Cái thật sự mất khi đốt: các bước thoại còn dở ngoài overworld, và **7 cuốn Forager Brood
Cookbook** (tất cả đều ở overworld).

---

## Bẫy warp

Mốc "Miquella's Great Rune vỡ" là **trigger theo vị trí, không phải giết boss**. Tranh cãi "sau
Golden Hippopotamus" đã giải quyết: đó là hiểu nhầm một câu GamesRadar dùng con Hippo làm mốc địa
lý. Cả wiki.gg lẫn Fextralife đều nói là tiếp cận Shadow Keep.

Ba vùng kích hoạt: Shadow Keep, Rauh Base, và đoạn từ Bonny Village lên bắc về phía Church District.

Grace nên coi là mìn: Shadow Keep Main Gate, Main Gate Plaza, Church District Highroad, mọi grace
trong Church District / Specimen Storehouse / Scaduview / Rauh Base / Ancient Ruins of Rauh, và
**cả 6 grace Enir-Ilim**.

Với anh mốc này **đã qua** (`Golden Lion Shield` chứng minh đã lên tới Storehouse Seventh Floor),
nên phần trên chỉ còn giá trị tham chiếu. Grace duy nhất còn phải né: **Messmer's Dark Chamber** -
đứng ở grace thì không sao, qua cửa sương là mất đồ.

Chưa nguồn nào test được là *warp* vào vùng trigger có kích hoạt không, hay chỉ *đi bộ* vào mới
kích. Cứ coi là có.

---

## Hồi ức đang cầm mà chưa đổi

Bốn cái, đều DLC. Base game đã đổi hết.

| Hồi ức | Boss |
|---|---|
| `Remembrance of the Dancing Lion` | Divine Beast Dancing Lion |
| `Remembrance of the Twin Moon Knight` | Rellana |
| `Remembrance of Putrescence` | Putrescent Knight |
| `Remembrance of the Shadow Sunflower` | Scadutree Avatar |

Đổi ở **Enia, Roundtable Hold**, lúc nào cũng được kể cả sau khi Maliketh chết.

**Không phải chọn một trong hai.** Hồi ức DLC nhân bản được. Ngoài Walking Mausoleum của base
game, DLC còn có **3 cái Remembrance Duplication Coffin không cần điều kiện gì**: Cathedral of
Manus Metyr, Finger Ruins of Dheo, Finger Ruins of Rhia. Nhân đôi hết rồi lấy cả hai món mỗi cái.

| Hồi ức | Món A | Món B | Rune nếu ăn |
|---|---|---|---|
| Dancing Lion | `Enraged Divine Beast` (talisman, +10% đòn hệ storm) | `Ash of War: Divine Beast Frost Stomp` | 30.000 |
| Twin Moon Knight | `Rellana's Twin Blades` (Light Greatsword, 13 Str/16 Dex/16 Int/16 Fai) | `Rellana's Twin Moons` (sorcery, **72 Int**) | 30.000 |
| Putrescence | `Putrescence Cleaver` (Greataxe, 28 Str/10 Dex/15 Arc) | `Vortex of Putrescence` (sorcery, 32 Int/26 Fai) | 30.000 |
| Shadow Sunflower | `Shadow Sunflower Blossom` (Colossal, 24 Str/8 Dex/25 Fai) | `Land of Shadow` (incantation, 52 Fai) | 40.000 |

Anh 8 stat đều 99 nên requirement không phải vấn đề, cứ nhân đôi lấy hết.

Còn cầm `Mending Rune of the Death-Prince` (Fia, ending Age of the Duskborn) và
`Mending Rune of the Fell Curse` (Dung Eater, ending Blessing of Despair). Thiếu
`Mending Rune of Perfect Order` (Goldmask, ending Age of Order) - phải giết Maliketh mới có.
Ba ending đó anh đang giữ đủ đường chọn.

---

## Vài chi tiết đáng sửa trong doc

- **Moore không cần đánh, và cả ba nhánh đều cho đủ bộ Verdigris.** "Remain sad forever" = ông
  tự tử, nằm trên vách bắc Church of the Crusade, nhặt xác không phải đánh. "Put it behind you" =
  ông sang Enir-Ilim đánh cùng phe Leda. Giết **2** con forager brood mới làm ông invade, giết 1
  con chỉ bị mắng. `Moore's Bell-Bearing` chỉ rủi ro ở nhánh invade, và ngay cả đó nguồn cũng
  mâu thuẫn nhau.
- **`Forager Brood Cookbook [7]`** lấy bằng cách hơ ấm con brood ốm ở phía bắc Church of the
  Crusade bằng `Warming Stone` hoặc `Sunwarmth Stone`. Cũng con đó cho cuốn [4] khi nói lại sau
  reload.
- **St. Trina cần 6 ngụm** (nghe cô ấy nói 3 lần), không phải 4, thì thoại sau invade mới chạy.
- **Mohg's Great Rune chạy được khi chơi đơn**, không phải chỉ multiplayer: spirit ash triệu hồi
  ra tự động có `Blessing of Blood`, +30% sát thương cho ash và hồi máu cho anh khi gây bleed.
  Đáng trang bị khi đi solo với Mimic Tear hoặc Tiche.

---

## Thứ tự đề xuất

1. Nhặt `Golden Order Seal` ở Minor Erdtree Church (Altus, tây nam Leyndell) - không gấp
2. Đổi 4 hồi ức ở Enia
3. Moore: gom hết Forager Brood Cookbook trước, rồi mới trả lời câu hỏi số phận
4. Ngã ba Leda vs Hornsent ở Shadow Keep - bỏ trống cả hai dấu (xem report riêng)
5. Grandam: lấy `Gourmet Scorpion Stew`, **phải xong trước khi Messmer chết**
6. Ymir: mua hết 9 phép, triệu hồi Jolán ở trận Messmer nếu muốn
7. Messmer (triệu hồi Hornsent)
8. Hornsent invade ở cầu thang Church of the Bud → Romina
9. Metyr → Jolán → Ymir
10. Midra, Gaius, Scadutree Avatar, boss field còn lại - lúc nào cũng được
11. Đốt Sealing Tree → dọn nốt questline trong Enir-Ilim
12. Promised Consort Radahn
13. Maliketh → Gideon → Hoarah Loux → Radagon

---

## Chưa rõ

- Dấu triệu hồi Ansbach-vs-Leda có còn sau khi Messmer chết không: bình luận PowerPyx nói còn,
  không wiki nào xác nhận. Cứ giải quyết trước khi vào phòng Messmer.
- Warp vào vùng trigger có kích hoạt "Great Rune vỡ" như đi bộ không - không nguồn nào test.
