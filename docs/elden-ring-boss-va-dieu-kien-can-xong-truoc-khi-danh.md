# Boss và điều kiện cần xong trước khi đánh

Một nguồn duy nhất: boss nào có ràng buộc NPC/questline/cốt truyện, phải làm gì trước, mất gì
nếu đánh sớm. Base game + Shadow of the Erdtree.

Nhân vật `dyu` slot 1 | soát 2026-09-13 | **119/206 boss đã hạ** (base 103/164, DLC 16/42)
Trạng thái đọc thẳng từ `ER0000.sl2`:
`~/.claude/skills/.venv/bin/python3 elden_ring_grace_unlock.py boss-report -f <save> --slot 1`

Giết Maliketh xong thì lệnh trên **tắt hẳn**: oracle dò base đòi cả 9 grace
`LeyndellRoyalCapital` phải sáng, mà chúng tắt sạch khi thành hoá tro, nên script từ chối mọi
offset kể cả khi truyền `--base` tay. Đã bỏ `LeyndellRoyalCapital` khỏi oracle ngày 13/09; 14 grace
còn lại vẫn cho đúng một nghiệm trên cả save cũ lẫn save mới, nên lệnh chạy lại bình thường.

Nguồn: wiki.gg là chính, đối chiếu Fextralife / PowerPyx / Game8. Mọi mục có điều kiện đều qua
một pass phản biện bắt buộc bác bỏ; những chỗ pass đó sửa đã được ghi lại theo bản sửa.

Liên quan: [Questline base game](./elden-ring-questline-checklist-va-quest-path.md) ·
[Questline DLC](./elden-ring-dlc-questline-checklist-va-quest-path.md) ·
[Boss nào đánh thoải mái - phân tích cho save hiện tại](../plans/reports/deep-research-260828-0326-boss-danh-thoai-mai-khong-hong-questline-report.md)

> Questline base game của anh đã xong 100%, nên phần base game dưới đây phần lớn là tham chiếu
> cho NG+. Phần còn sống với anh nằm ở mục ngay dưới bảng bốn cửa một chiều.

---

## Bốn cửa một chiều

Đây là bốn mốc thật sự không quay lại được. Mọi thứ khác trong game đều sửa được.

| Mốc | Ở đâu | Đóng cái gì | Trạng thái |
|---|---|---|---|
| **Rykard** | Volcano Manor | Cả nhánh Volcano Manor: 3 hợp đồng, Patches/Tragoth, Bernahl, Rya | ✅ xong |
| **Đốt Erdtree** (Forge of the Giants) | Flame Peak | Melina, 3 cử chỉ, và 2 phép của shop Corhyn | ✅ đã đốt |
| **Maliketh** | Crumbling Farum Azula | Leyndell Royal Capital thành Ashen Capital | ✅ đã qua (Leyndell giờ là Ashen Capital) |
| **Đốt Sealing Tree** | Church of the Bud, Rauh (DLC) | Các bước overworld của NPC DLC + 7 cuốn Forager Brood Cookbook | 🔴 chưa - **cửa duy nhất còn lại** |

**Đốt cây KHÔNG biến Leyndell thành Ashen Capital.** Maliketh mới làm. Rất nhiều guide gộp hai
mốc này làm một. Sau khi đốt cây, Leyndell Royal Capital vẫn vào và nhặt đồ bình thường.

---

## Còn sống VÀ có điều kiện - danh sách ngắn cần để ý

87 boss còn sống, nhưng chỉ 8 con dưới đây có ràng buộc. Còn lại giết lúc nào cũng được.

| Boss | Điều kiện còn treo |
|---|---|
| **Gideon** | Không còn gì. 4 khám phá đã nộp đủ |
| **Hoarah Loux** | Không có, chỉ 2 dấu triệu hồi tuỳ chọn |
| **Radagon / Elden Beast** | Không có. Nhớ là ending chỉ nổ khi **chạm di hài Marika**, giết xong vẫn warp ra được |
| **Mohg, the Omen** (Shunning-Grounds) | Chỉ dấu triệu hồi Dung Eater, mà mạch đó anh xong rồi. Vào bằng nắp cống trong Ashen Capital |
| 🔴 **Metyr** | Mua hết 9 phép của Ymir (80.500 rune) trước |
| **Count Ymir** | Nằm sau Metyr trong cùng một chuỗi |
| 🟡 **Romina** | Không có. Chỉ mở đường tới Sealing Tree |
| 🔴 **Promised Consort Radahn** | Hết DLC. Trang bị `Miquella's Great Rune` (đã có trong túi) |

**Messmer chết rồi**, nên ngã ba Leda/Hornsent ở Shadow Keep đóng vĩnh viễn. Phần còn lại của
mạch DLC vẫn mở, danh sách việc ở
[Sau Messmer](./elden-ring-sau-messmer-va-audit-item-con-thieu.md#phần-1---sau-khi-hạ-messmer).

Toàn bộ 206 boss kèm trạng thái ở [phụ lục cuối trang](#phụ-lục-206-boss-đã-hạ-hay-chưa).

⚠️ 206 vẫn **chưa phải con số cuối**, và 3 dòng trong bảng đang trỏ trùng cờ với dòng khác nên bị
đếm hai lần. Chi tiết + cách sửa ở
[audit bảng cờ boss](../plans/reports/boss-flag-table-260913-2106-doi-chieu-gameareaparam-va-lo-hong-report.md).

---

## Base game: boss có điều kiện

### Limgrave, Weeping Peninsula

**Godrick the Grafted.** Ba việc trước cửa sương:
1. Nói chuyện với **Nepheli Loux** trong Stormveil (phòng nhỏ sau grace Liftside Chamber, gần
   Secluded Cell), vét hết thoại. Không cần triệu hồi, chỉ cần nói chuyện.
   Wiki ghi thẳng: *"If you defeated Godrick without speaking to her in the previous step, she
   will not give the Arsenal Charm."*
2. **Không được giết Gatekeeper Gostoc**, bất cứ lúc nào. Ông chết là quest Nepheli hỏng.
   Lỡ aggro thì rửa tội ở Church of Vows bằng `Celestial Dew`.
3. Muốn nội dung **Roderika** ở Stormhill Shack thì nói chuyện trước. Cô ấy rời shack ngay khi
   Godrick chết, hoặc khi anh nghỉ ở bất kỳ grace nào của Liurnia.

Mất nếu bỏ qua: **đúng một món, `Arsenal Charm`** (+15% equip load, không có nguồn nào khác).
Mạch Nepheli **không** hỏng: cô vẫn xuất hiện ngoài phòng Gideon, vẫn sang Village of the
Albinaurics, vẫn nhận `The Stormhawk King`, vẫn cho `Ancient Dragon Smithing Stone` ở phòng ngai
Stormveil, và Kenneth Haight vẫn tôn cô làm lord of Limgrave. (Bản đầu của doc này ghi mất cả
mạch, pass phản biện bác lại.)

**Leonine Misbegotten (Castle Morne).** Lấy `Irina's Letter` ở Bridge of Sacrifice đưa cho
**Edgar** ở Castle Morne trước khi vào cửa sương. Cũng đừng gặp Hyetta trước. Bỏ qua thì mất dấu
triệu hồi Edgar, `Sacrificial Twig`, và cả đoạn kịch Irina/Edgar. Đồ cuối của Edgar vẫn lấy được
vì ông chuyển thành invader ở Revenger's Shack.

**Patches (Murkwater Cave).** 🔴 Ông có thanh máu boss (1.191 HP), đó là lý do người ta giết theo
phản xạ. Ở ~50% máu ông tự đầu hàng và ngừng đánh. **Không cần đứng im**, đánh tiếp chỉ làm ông
hung lại (và đó chính là cách lấy cử chỉ `Extreme Repentance`). Chỉ là **đừng ra đòn kết liễu**.

Giết chết thì mất: cử chỉ `Grovel for Mercy`, `Patches' Crouch`, 2 trong 3 lần lấy `Calm Down!`,
bản thân ông làm merchant, và mọi lần xuất hiện sau ở Scenic Isle, Mt. Gelmir, Volcano Manor,
Shaded Castle. `Celestial Dew` không cứu được NPC đã chết.

**Không** mất bell bearing: giết ông là được `Patches' Bell Bearing`, đưa cho Twin Maiden Husks là
khôi phục 15 món trong đó có `Margit's Shackle`. Cái mất là phần hàng mở rộng chỉ có khi ông
chuyển sang Liurnia.

**Bloodhound Knight Darriwil (Forlorn Hound Evergaol).** Chỉ ảnh hưởng dấu triệu hồi Blaidd.
Lấy cử chỉ `Finger Snap` từ Kalé ở Church of Elleh, dùng ở Mistwood Ruins để gặp Blaidd. Giết
Darriwil trước khi gặp Blaidd **không hỏng gì**, Blaidd vẫn đứng ngoài evergaol và vẫn đưa
`Somber Smithing Stone [2]`.

**Bell Bearing Hunter (Warmaster's Shack).** Vét thoại Bernahl trước, không thì nó không spawn.
Thương nhân **không bao giờ chết** ở bất kỳ trận Bell Bearing Hunter nào, chỉ biến mất trong lúc
đánh rồi quay lại.

**Recusant Henricus.** Đánh **trước khi** gia nhập Volcano Manor. Vào Manor rồi là ông không
invade nữa, mất `Hammer Talisman` cho lượt đó.

**Bloody Finger Nerijus → Ravenmount Assassin → Eleonora (mạch Yura).** 🔴 Phải xong **trước khi
dùng Grand Lift of Rold**. Lên Mountaintops sớm là Yura chết non, mất `Nagakiba`, và Shabriri
xuất hiện thay ông ở Zamor Ruins.

### Liurnia, Caelid

**Starscourge Radahn.** Festival tự khởi động khi anh làm bất kỳ việc nào: nghỉ ở grace Altus,
hỏi Blaidd về Radahn ở Siofra, hoặc hỏi Iji về Jerren. Trước khi giết Radahn:
- Đẩy **Ranni** tới bước làm chư hầu ở Ranni's Rise **trước khi festival bắt đầu**. Festival đang
  chạy thì Ranni không xuất hiện, và Blaidd bị thiếu khỏi bộ ba người hầu, mất luôn nội dung
  Ranni's Rise và Siofra của anh ta
- Nói chuyện **Jerren** trên bục để lấy cử chỉ `Heartening Cry`
- **Crucible Knight + Misbegotten Warrior** ở sân Redmane: đánh trước festival hoặc sau khi Radahn
  chết. Chúng chỉ biến mất trong lúc festival chạy, **không mất vĩnh viễn** như nhiều người tưởng

Giết Radahn không hard-break Ranni hay Blaidd, chỉ bỏ qua mấy đoạn sớm của Blaidd.

**Omenkiller (Village of the Albinaurics).** Nói chuyện Nepheli ở dốc vào làng trước, và nói lại
sau. Bẫy thật nằm ở đầu kia: **đốt Erdtree trước khi xong bước này là Nepheli biến mất vĩnh viễn**.

**Ensha of the Royal Remains.** Chỉ trở mặt khi anh cầm một nửa `Haligtree Secret Medallion`.
Muốn cử chỉ `What do you want?` thì nói chuyện trước khi nhặt nửa nào.

**Commander O'Neil.** Không có điều kiện chứng minh được. `Unalloyed Gold Needle` rơi vô điều kiện.
Thứ tự an toàn vẫn là gặp Gowry trước, nhưng không nguồn nào nói đó là bắt buộc.

**Alecto, Glintstone Dragon Adula (bản Moonlight Altar).** Không giết sớm được, chúng nằm sau
cả mạch Ranni. Adula ở Three Sisters luôn bỏ chạy ở nửa máu, đồ chỉ rơi ở bản Moonlight Altar.

### Altus, Mt. Gelmir, Volcano Manor, Leyndell

**🔴 Rykard, Lord of Blasphemy.** Cửa một chiều lớn nhất vùng. Chết là mọi nhánh Volcano Manor
đứt, bất kể đang tới đâu. Phải xong trước:

1. Gia nhập Manor, lấy `Drawing Room Key` từ Tanith
2. Hợp đồng 1: giết **Old Knight Istvan** → `Magma Shot`
3. Hợp đồng của **Patches**: giết **Great Horned Tragoth** (invade trong phòng boss Magma Wyrm
   Makar, nên Makar phải chết trước) → `Bull-Goat Set`, quay lại Patches 2 lần → `Magma Whip Candlestick`
4. Hợp đồng 2: giết **Rileigh the Idle** → `Serpentbone Blade`
5. Hợp đồng của **Bernahl**: giết **Vargram + Wilhelm** (dấu invade ở tầng trệt Fortified Manor,
   **trong Leyndell Royal Capital**) → `Raging Wolf Set`, quay lại Bernahl → `Gelmir's Fury`
6. **Rya**: đưa `Serpent's Amnion` và chốt kết cục của cô **trước hợp đồng 3**
7. Hợp đồng 3: giết **Juno Hoslow** (invade ở Shack of the Lofty, **Mountaintops**) → `Taker's Cameo`

Hai ràng buộc lịch rơi ra từ đây: Juno ở Mountaintops nên **Morgott phải chết trước**; Vargram ở
Leyndell Royal Capital nên **phải xong trước Maliketh**. Cửa sổ của cả nhánh: sau Morgott, trước
Maliketh, Rykard sống suốt.

Mất nếu giết sớm: 3 phần thưởng của Tanith, `Bull-Goat Set`, `Magma Whip Candlestick`,
`Raging Wolf Set`, `Gelmir's Fury`, và toàn bộ phần còn lại của Rya.

Dấu triệu hồi Bernahl ở trận Godskin Duo mở bằng bước **nhận `Gelmir's Fury`**, không phải bằng
cái chết của Rykard, nên nó không nằm trong danh sách mất ở đây.

Rykard chết thì mở: Tanith dời sang phòng ông (giết cô → `Consort's Set`), Patches sang Shaded
Castle, và **Bernahl sang Crumbling Farum Azula invade** → `Blasphemous Claw` (món parry Maliketh),
`Devourer's Scepter`, `Beast Champion Set`. `Blasphemous Claw` cần **cả hai**: chiêu mộ Bernahl ở
Volcano Manor **và** Rykard đã chết.

**Godskin Noble (Temple of Eiglay).** Không có điều kiện để đánh. `Serpent's Amnion` trên bàn thờ
nhặt lúc nào cũng được, nhưng **Rya chỉ nhận nó sau khi anh xong ít nhất 2 hợp đồng**.

**Godskin Apostle (Dominula).** Chỉ ảnh hưởng dấu triệu hồi Millicent, cần đã đưa cô
`Valkyrie's Prosthesis`. Questline cô **không hỏng**: giết con này chính là trigger đẩy cô sang
bước sau.

**Morgott.** Không có điều kiện, không mất gì. Tiếng đồn Morgott là point of no return là **sai**,
đó là Maliketh. Morgott chết thì mở: `Rold Medallion` → Mountaintops (nên mở được Juno Hoslow),
gỡ dấu niêm phong ở Cathedral of the Forsaken (cửa xuống Three Fingers), kết Nepheli ở phòng ngai
Stormveil, kết Kenneth Haight, và Gideon bắt đầu trao đổi thông tin.

**Mohg, the Omen (Shunning-Grounds).** Chỉ ảnh hưởng dấu triệu hồi Dung Eater. Không phải
Shardbearer, đừng nhầm với Mohg Lord of Blood ở Mohgwyn.

### Underground

**Mimic Tear (Nokron).** Bản thân trơ. Nhưng đằng sau nó là `Fingerslayer Blade`, và **đưa blade
cho Ranni là công tắc giết cả Seluvis lẫn Pidia, Carian Servant**. Xong hết việc với Seluvis trước: mua puppet, nhánh
`Seluvis's Potion`, và `Amber Starlight` đổi lấy `Amber Draught`.

**Astel, Naturalborn of the Void.** Cầm sẵn `Dark Moon Ring` trước khi đi thang Deep Ainsel Well,
không thì bị tường sương chặn và phải quay lại. Và xong hết việc với **Blaidd** và **Iji** khi
họ còn thân thiện: giết Astel khi đang cầm Dark Moon Ring chính là trigger làm Blaidd hoá dại.

**Fia's Champions / Lichdragon Fortissax.** Không giết sớm được, cả chuỗi bị gate cứng bởi mạch
Fia + `Cursemark of Death`, mà Cursemark lại nằm sau mạch Ranni.

**Mohg, Lord of Blood (Mohgwyn).** ⚠️ Tranh cãi. Xong **toàn bộ** mạch Varre trước, kể cả phần
diễn ra bên trong Mohgwyn Palace. GameFAQs và Steam nói Mohg chết là Varre hết invade; wiki.gg im
lặng, không xác nhận cũng không phủ nhận. Fextralife và Fandom không truy cập được để chốt.
Cứ làm xong Varre rồi mới giết Mohg.

### Mountaintops, Farum Azula, Haligtree

**Fire Giant.** Không mất gì. Chỉ làm hiện grace Forge of the Giants.

**Đốt Erdtree ở Forge of the Giants.** Năm thứ mất vĩnh viễn, không chỉ một:

| Món | Lấy ở đâu trước |
|---|---|
| Cử chỉ `Outer Order` | Melina, Minor Erdtree Church (Weeping Peninsula) |
| Cử chỉ `Golden Order Totality` | Goldmask, Leyndell - dùng `Law of Regression` lên tượng Radagon rồi nói thật với ông |
| Cử chỉ `Prayer` | Corhyn, Roundtable Hold - lần đầu gặp, nói là vẫn thấy được Guidance of Grace |
| `[Incantation] Great Heal` 9.000 rune | shop Corhyn ở Altus |
| `[Incantation] Lightning Fortification` 7.500 rune | shop Corhyn ở Altus |

Bốn món cuối cùng một nguyên nhân: đốt cây đẩy Corhyn và Goldmask sang giai đoạn Ashen Capital,
ở đó Corhyn trở mặt và ngừng bán.

Cũng mất Melina. **Không mất gì khác**: Leyndell vẫn là Royal Capital, Roundtable Hold vẫn nguyên.
Ngọn lửa chờ, cứ từ chối ở grace rồi đi làm nốt việc khác.

Với save của anh: `Great Heal` và `Lightning Fortification` đều đã có. Ba cử chỉ không đọc được
từ save (tool không đọc mảng gesture).

**Maliketh, the Black Blade.** ✅ Đã hạ. Giữ lại làm tham chiếu NG+. Cửa một chiều lớn nhất base
game, trước khi qua cửa sương phải:

| Việc | Vì sao | Trạng thái của anh |
|---|---|---|
| Vét sạch **Leyndell Royal Capital** | Cả thành bị chôn | ✅ `Bolt of Gransax`, `Coded Sword`, `Erdtree Bow`, `Sanctified Whetblade`, bộ Lionel's, bộ Alberich's đều đã có |
| **Boc** - bước cuối ở East Capital Rampart | Ông biến mất theo thành | ✅ xong |
| **Corhyn + Goldmask** đẩy tới cầu nam Stargazer's Ruins | Xác Goldmask chỉ spawn ở Ashen Capital nếu đã tới bước này | ✅ xong |
| **Gideon** - nộp 4 khám phá ở Roundtable | Maliketh chết là ông trở mặt | ✅ có đủ `Black Flame's Protection`, `Lord's Divine Fortification`, `Fevor's Cookbook [3]`, `Law of Causality` |
| **Bernahl** invade ở Farum Azula | Cho `Blasphemous Claw`, món parry chính Maliketh | ✅ xong |
| **Enia** - lấy `Talisman Pouch` | Cô mất thoại | ✅ có 3 cái |

**Kết luận cho save hiện tại: Maliketh không còn giữ gì của anh.** Cả 6 mục trên đều xong, nên
giết lúc nào cũng được, và giết mới lấy được `Mending Rune of Perfect Order` ở xác Goldmask.

Mất khi thành hoá tro: mọi đồ chưa nhặt trên mặt thành, Boc, dấu invade của Bernahl, thoại của
Enia, questline Gideon.

**Không** mất: Enia vẫn đổi remembrance và bán giáp boss từ xác. `Talisman Pouch` mua lại được ở
Twin Maiden Husks 500 rune. Gurranq **không** biến mất, Bestial Sanctum vẫn mở. Subterranean
Shunning-Grounds vẫn vào được qua nắp cống mở ra trong tro. Erdtree Sanctuary vẫn còn.

⚠️ Tranh cãi: guide Steam nói Maliketh giết luôn mạch Fia và D; wiki.gg và Game8 không có cảnh
báo nào như vậy.

**Sir Gideon Ofnir.** Mọi thứ muốn lấy từ ông phải xong ở Roundtable **trước Maliketh**. Bốn lần
nộp: sáng grace ở Haligtree, hạ Malenia, sáng grace ở Mohgwyn, hạ Mohg. Không mất vĩnh viễn, cả
bốn phần thưởng chuyển sang bán ở Twin Maiden Husks.

**Malenia.** Không có điều kiện. Questline Millicent **không** bị gate bởi Malenia, wiki nói rõ
là bắt đầu được cả sau khi Malenia chết. Thứ tự gọn vẫn là Millicent trước.

**Radagon / Elden Beast.** Giết xong **chưa hết game**. Anh rơi vào phòng Marika có grace, warp ra
làm nốt việc rồi quay lại được. Ending chỉ kích hoạt khi **chạm vào di hài Marika**. Nên Mending
Rune muốn dùng phải cầm sẵn lúc đó.

---

## DLC: boss có điều kiện

Chi tiết đầy đủ ở
[report riêng](../plans/reports/deep-research-260828-0326-boss-danh-thoai-mai-khong-hong-questline-report.md).
Tóm tắt:

**🔴 Messmer the Impaler.** Nguy hiểm nhất, và nó cắn **trước khi anh đánh**: chỉ cần bước vào
phòng boss từ grace Dark Chamber là hai dấu triệu hồi Leda-vs-Hornsent ở Shadow Keep mất vĩnh viễn.
Trước Messmer phải xong:
- Ngã ba **Leda vs Hornsent** (ba nhánh, xem
  [report riêng](../plans/reports/deep-research-260828-0351-hornsent-do-hay-vang-hay-bo-trong-report.md))
- **Hornsent Grandam**: lấy `Gourmet Scorpion Stew`. Wiki `Watchful Spirit` ghi thẳng
  *"Must be done before defeating Messmer the Impaler."*
- Triệu hồi **Hornsent** trong trận, không thì phần còn lại questline của anh ta bị bỏ qua

**🔴 Metyr, Mother of Fingers.** Giết là xoá dấu triệu hồi Jolán (kể cả dấu ở trận Messmer), và
quay lại Cathedral of Manus Metyr là bị ép đánh Jolán rồi Ymir. **Mua hết 9 phép của Ymir trước,
80.500 rune**, shop chết theo ông.

**🟡 Romina.** Bản thân vô hại. Nhiều guide gọi cô là point of no return, sai: cái khoá là đốt
Sealing Tree. Giết Romina xong đứng cạnh cây bao lâu cũng được.

**🔴 Promised Consort Radahn.** Hết DLC. Trang bị `Miquella's Great Rune` để phá bùa mê phase 2.

**Golden Hippopotamus.** Nằm sau mốc "Great Rune vỡ" nên không phải free kill về mặt thứ tự.
Là một trong các trigger đẩy Thiollier đi tìm St. Trina.

**Jagged Peak Drake → Bayle (mạch Igon).** Giết Drake là Igon xuất hiện. Triệu hồi Igon ở trận
Bayle rồi quay lại đấu trường Drake lấy `Igon's Greatbow`, `Igon's Set`, `Igon's Bell Bearing`.

**Mốc "Miquella's Great Rune vỡ" là trigger theo VỊ TRÍ, không phải giết boss.** Ba vùng kích
hoạt: Shadow Keep, Rauh Base, và đoạn từ Bonny Village lên bắc. Với ai mở sẵn grace bằng save
editor thì warp là dính.

---

## Boss trơ - giết lúc nào cũng được

Đã soát từng nhóm, không nhóm nào dính NPC hay questline:

**Base game.** Toàn bộ catacomb (Erdtree Burial Watchdog, Cemetery Shade, Grave Warden Duelist,
Black Knife Assassin, Spiritcaller Snail), toàn bộ hang trừ Murkwater Cave, toàn bộ tunnel
(Crystalian, Stonedigger Troll, Magma Wyrm, Scaly Misbegotten, Fallingstar Beast, Astel bản
Yelough Anix), mọi Erdtree Avatar, cả 9 Night's Cavalry, 4 Deathbird + 4 Death Rite Bird (con ở Charo's Hidden Grave là DLC, không
phải base game), mọi Tree Sentinel, cả 4 Bell Bearing Hunter, rồng lang thang, và evergaol trừ Forlorn Hound.

Ngoại lệ duy nhất trong nhóm evergaol: **Forlorn Hound** (Blaidd bị Iji nhốt ở đó sau này) và
**Ordina** (câu đố 4 ngọn nến gating Haligtree, không có boss).

**Grafted Scion** ở Chapel of Anticipation: giết hay bỏ đều được, đồ y hệt. Bỏ thì quay lại qua
Four Belfries bằng `Imbued Sword Key`. Nhưng **không đánh lại được** nếu đã giết ở màn mở đầu.

**DLC.** 24 con field/hang/gaol đều trơ: Knight of the Solitary Gaol, Rakshasa, Red Bear, Rugalea,
Ralva, cả 3 Ghostflame Dragon, Chief Bloodfiend, Black Knight Edredd, Black Knight Garrew,
Curseblade Labirith, Lamenter, Ancient Dragon Senessax, Demi-Human Swordmaster Onze, Demi-Human
Queen Marigga, Fallingstar Beast, Torch Tree Sentinel, cả 2 Death Knight, Bloodfiend Chief,
Death Rite Bird ở Charo's Hidden Grave, Divine Beast Dancing Lion **bản Rauh** (dấu Freyja và cờ
Grandam chỉ gắn bản Belurat), Jori, Ancient Dragon-Man, Midra, Commander Gaius.

Dragon Heart rơi từ 3 con Ghostflame Dragon và 2 con Jagged Peak Drake. Ancient Dragon Senessax
cho smithing stone, không cho Dragon Heart.

---

## Chưa rõ / tranh cãi

- **Mohg và Varre.** Giết Mohg có xoá dấu invade của Varre không. GameFAQs/Steam nói có, wiki.gg
  im lặng, Fextralife và Fandom không truy cập được. Cứ xong Varre rồi mới giết Mohg.
- **Maliketh và mạch Fia/D.** Guide Steam nói chết theo, wiki.gg và Game8 không cảnh báo gì.
- **Alexander và Fire Giant.** Guide Steam nói Fire Giant ảnh hưởng quest của ông; Game8 nói
  triệu hồi ở trận đó không bắt buộc để ông xuất hiện lại ở Farum Azula. Chưa chốt được.
- **Commander O'Neil và Gowry.** Mọi guide đặt Gowry trước nhưng không nguồn nào nói là bắt buộc.
- **Crucible Knight ở Stormhill Evergaol** có cần Stonesword Key không: wiki.gg nói không,
  DualShockers/GamerGuides nói có.
- **Warp vào vùng trigger DLC** có kích hoạt "Great Rune vỡ" như đi bộ không: không nguồn nào test.

---

## Phụ lục: 206 boss, đã hạ hay chưa

Đọc từ save lúc 2026-09-11 19:06, **119/206**. ✅ = đã hạ, ⬜ = còn sống.
Sinh lại bằng `elden_ring_grace_unlock.py boss-report`.

### Base game (103/164)

**Limgrave** - 21/22

- ⬜ Alabaster Lord (Evergaol)
- ✅ Beastman of Faram Azula (Groveside Cave)
- ✅ Bell Bearing Hunter (Warmaster's Shack)
- ✅ Black Knife Assassin (Deathtouched Catacombs)
- ✅ Bloodhound Knight Darriwil (Forlorn Hound Evergaol)
- ✅ Crucible Knight (Stormhill Evergaol)
- ✅ Deathbird (Limgrave)
- ✅ Demi-Human Chiefs (Coastal Cave)
- ✅ Erdtree Burial Watchdog (Stormfront Catacombs)
- ✅ Flying Dragon Agheel (Limgrave)
- ✅ Godrick the Grafted
- ✅ Grafted Scion (Chapel of Anticipation)
- ✅ Grave Warden Duelist (Murkwater Catacombs)
- ✅ Guardian Golem (Highroad Cave)
- ✅ Mad Pumpkin Head (Waypoint Ruins)
- ✅ Margit the Fell Omen
- ✅ Night's Cavalry (Limgrave)
- ✅ Patches (Murkwater Cave)
- ✅ Soldier of Godrick
- ✅ Stonedigger Troll (Limgrave Tunnels)
- ✅ Tibia Mariner (Summonwater Village)
- ✅ Tree Sentinel (Limgrave)

**Weeping Peninsula** - 9/10

- ✅ Ancient Hero of Zamor (Weeping Evergaol)
- ✅ Cemetery Shade (Tombsward Catacombs)
- ⬜ Deathbird (Weeping Peninsula)
- ✅ Edtree Burial Watchdog (Impaler's Catacombs)
- ✅ Erdtree Avatar
- ✅ Leonine Misbegotten (Morne Moangrave)
- ✅ Miranda the Blighted Bloom (Tombsward Cave)
- ✅ Night's Cavalry (Weeping Peninsula)
- ✅ Runebear (Earthbore Cave)
- ✅ Scaly Misbegotten (Morne Tunnel)

**Liurnia of the Lakes + Raya Lucaria + Ruin-Strewn Precipice** - 19/27

- ⬜ Adan, Thief of Fire (Malefactor's Evergaol)
- ✅ Alecto, Black Knife Ringleader (Ringleader's Evergaol)
- ✅ Bell Bearing Hunter (Church of Vows)
- ✅ Black Knife Assassin (Black Knife Catacombs)
- ✅ Bloodhound Knight (Lakeside Crystal Cave)
- ⬜ Bols, Carian Knight (Cuckoo's Evergaol)
- ✅ Cemetery Shade (Black Knife Catacombs)
- ✅ Cleanrot Knight (Stillwater Cave)
- ✅ Crystalian (Raya Lucaria Crystal Tunnel)
- ✅ Crystalian Spear Crystalian Staff (Academy Crystal Cave)
- ✅ Deathbird (Liurnia South)
- ⬜ Death Rite Bird (Liurnia North)
- ✅ Erdtree Avatar (Liurnia Northeast)
- ⬜ Erdtree Avatar (Liurnia Southwest)
- ✅ Erdtree Burial Watchdog (Cliffbottom Catacombs)
- ✅ Glintstone Dragon Adula (Moonlight Altar)
- ✅ Glintstone Dragon Smarag (Liurnia)
- ⬜ Night's Cavalry (Liurnia North)
- ✅ Night's Cavalry (Liurnia South)
- ✅ Omenkiller (Village of the Albinaurics)
- ⬜ Onyx Lord (Royal Grave Evergaol)
- ✅ Royal Knight Loretta (Caria Manor)
- ⬜ Royal Revenant (Kingsrealm Ruins)
- ⬜ Spiritcaller Snail (Road's End Catacombs)
- ✅ Rennala, Queen of the Full Moon
- ✅ Red Wolf of Radagon (Raya Lucaria)
- ✅ Magma Wyrm Makar (Ruin-Strewn Precipice)

**Caelid + Greyoll's Dragonbarrow** - 14/26

- ⬜ Cemetery Shade (Caelid Catacombs)
- ✅ Cleanrot Knights (Abandoned Cave)
- ✅ Commander O'Neil (Swamp of Aeonia)
- ✅ Crucible Knight. Misbegotten Warrior (Redmane Castle)
- ✅ Death Rite Bird (Caelid)
- ⬜ Decaying Ekzykes (Caelid)
- ✅ Elder Dragon Greyoll
- ⬜ Erdtree Burial Watchdogs (Minor Erdtree Catacombs)
- ✅ Fallingstar Beast (Sellia Crystal Tunnel)
- ✅ Frenzied Duelist (Gaol Cave)
- ⬜ Mad Pumpkin Heads (Caelem Ruins)
- ✅ Magma Wyrm (Gael Tunnel)
- ⬜ Night's Cavalry (Caelid)
- ✅ Nox Swordstress and Nox Priest (Sellia, Town of Sorcery)
- ⬜ Putrid Avatar (Caelid)
- ⬜ Putrid Tree Spirit (War-Dead Catacombs)
- ✅ Starscourge Radahn
- ⬜ Battlemage Hugues (Sellia Evergaol)
- ✅ Beastmen of Faram Azula (Dragonbarrow Cave)
- ⬜ Bell Bearing Hunter (Isolated Merchant's Shack)
- ✅ Black Blade Kindred (Bestial Sanctum)
- ⬜ Flying Dragon Greyll (Greyoll's Dragonbarrow)
- ✅ Godskin Apostle (Divine Tower of Caelid)
- ⬜ Night's Cavalry (Dragonbarrow)
- ⬜ Putrid Avatar (Dragonbarrow)
- ✅ Putrid Crystalians (Sellia Hideaway)

**Altus Plateau** - 10/19

- ⬜ Ancient Dragon Lansseax (Altus Plateau)
- ✅ Ancient Hero of Zamor (Sainted Hero's Grave)
- ⬜ Black Knife Assassin (Sage's Cave)
- ✅ Black Knife Assassin (Sainted Hero's Grave)
- ⬜ Crystalian Spear and Crystalian Ringblade (Altus Tunnel)
- ✅ Demi-Human Queen Gilika (Lux Ruins)
- ✅ Elemer of the Briar (The Shaded Castle)
- ✅ Erdtree Burial Watchdog (Wyndham Catacombs)
- ⬜ Fallingstar Beast (Altus Plateau)
- ✅ Godefroy the Grafted (Golden Lineage Evergaol)
- ✅ Godskin Apostle (Dominula, Windmill Village)
- ⬜ Necromancer Garris (Sage's Cave)
- ⬜ Night's Cavalry (Altus Plateau)
- ✅ Omenkiller and Miranda the Blighted Bloom (Perfumer's Grotto)
- ⬜ Perfumer Tricia and Misbegotten Warrior (Unsightly Catacombs)
- ⬜ Sanguine Noble (Writheblood Ruins)
- ⬜ Stonedigger Troll (Old Altus Tunnel)
- ✅ Tibia Mariner (Wyndham Ruins)
- ✅ Tree Sentinels (Altus Plateau)

**Capital Outskirts + Leyndell, Royal Capital** - 7/11

- ✅ Bell Bearing Hunter (Hermit Merchant's Shack)
- ⬜ Crucible Knight, Crucible Knight Ordovis (Auriza Hero Grave)
- ✅ Deathbird (Warmaster's Shack)
- ✅ Draconic Tree Sentinel (Capital Outskirts)
- ⬜ Esgar, Priest of Blood (Leyndell Catacombs)
- ⬜ Fell Twins (Divine Tower of East Altus)
- ✅ Grave Warden Duelist (Auriza Side Tomb)
- ✅ Godfrey, First Elden Lord (Golden Shade)
- ⬜ Mohg, the Omen (Cathedral of the Forsaken)
- ✅ Morgott, the Omen King
- ✅ Onyx Lord (Sealed Tunnel)

**Mt. Gelmir + Volcano Manor** - 5/10

- ⬜ Abductor Virgins (Mt. Gelmir)
- ✅ Demi-Human Queen Maggie (Hermit Village)
- ⬜ Demi-Human Queen Margot (Volano Cave)
- ⬜ Full-Grown Fallingstar Beast (Ninth Mt. Gelmir Campsite)
- ✅ God-Devouring Serpent / Rykard, Lord of Blasphemy
- ✅ Godskin Noble (Temple of Eiglay)
- ⬜ Kindred of Rot (Seethewater Cave)
- ✅ Magma Wyrm (Mt. Gelmir)
- ⬜ Red Wolf of the Champion (Gelmir Hero's Grave)
- ✅ Ulcerated Tree Spirit (Mt. Gelmir)

**Mountaintops of the Giants** - 5/9

- ⬜ Ancient Hero of Zamor (Giant-Conquring Hero's Grave)
- ✅ Borealis the Freezing Fog (Freezing Lake)
- ✅ Commander Niall (Castle Sol)
- ✅ Death Rite Bird (Mountaintops of the Giants)
- ✅ Erdtree Avatar (Mountaintops of the Giants)
- ✅ Fire Giant
- ⬜ Godskin Apostle and Godskin Noble  (Spiritcaller Cave) Spiritcaller Snail
- ⬜ Ulcerated Tree Spirit (Giants' Mountaintop Catacombs)
- ⬜ Vyke, Knight of the Roundtable (Lord Contender's Evergaol)

**Crumbling Farum Azula** - 2/3

- ⬜ Dragonlord Placidusax
- ✅ Godskin Duo
- ✅ Malekith, the Black Blade

**Forbidden Lands + Consecrated Snowfield** - 2/10

- ✅ Black Blade Kindred (Forbidden Lands)
- ⬜ Night's Cavalry (Forbidden Lands)
- ⬜ Stray Mimic Tear (Hidden Path to the Haligtree)
- ⬜ Astel, Stars of Darkness (Yelough Anix Tunnel)
- ⬜ Death Rite Bird (Consecrated Snowfield)
- ⬜ Great Wyrm Theodorix (Consecrated Snowfield)
- ⬜ Misbegotten Crusader (Cave of the Forlorn)
- ⬜ Night's Cavalry Duo (Consecrated Snowfield)
- ✅ Putrid Avatar
- ⬜ Putrid Grave Warden Duelist (Consecrated Snowfield Catacombs)

**Miquella's Haligtree + Elphael** - 2/2

- ✅ Loretta, Knight of the Haligtree
- ✅ Malenia, Goddess of Rot

**Underground - Siofra / Nokron / Ainsel / Deeproot / Mohgwyn** - 7/12

- ⬜ Ancestor Spirit (Siofra River Bank)
- ✅ Dragonkin Soldier (Siofra River Bank)
- ✅ Mohg, Lord of Blood
- ⬜ Dragonkin Soldier of Nokstella (Ainsel River)
- ✅ Mimic Tear (Nokron, Eternal City)
- ⬜ Regal Ancestor Spirit (Ancestral Woods)
- ✅ Valiant Gargoyles (Siofra Aqueduct)
- ⬜ Crucible Knight Siluria
- ✅ Fia's Champions
- ✅ Lichdragon Fortissax
- ✅ Astel, Naturalborn of the Void
- ⬜ Dragonkin Soldier (Lake of Rot)

**Leyndell, Ashen Capital + Erdtree** - 0/3

- ⬜ Godfrey, First Elden Lord (Hoarah Loux)
- ⬜ Sir Gideon Ofnir, the All-Knowing
- ⬜ Radagon of the Golden Order / Elden Beast

### Shadow of the Erdtree (16/42)

- ⬜ Ancient Dragon Senessax (Jagged Peak)
- ✅ Ancient Dragon-Man (Dragon's Pit)
- ✅ Bayle the Dread (Jagged Peak)
- ⬜ Black Knight Edredd (Scadu Altus)
- ⬜ Black Knight Garrew (Fog Rift Fort, Scadu Altus)
- ⬜ Blackgaol Knight / Knight of the Solitary Gaol (Western Nameless Mausoleum)
- ⬜ Chief Bloodfiend (Rivermouth Cave)
- ✅ Commander Gaius (Scaduview)
- ⬜ Count Ymir, Mother of Fingers (Cathedral of Manus Metyr)
- ⬜ Curseblade Labirith (Bonny Gaol)
- ✅ Dancer of Ranah (Southern Nameless Mausoleum, Cerulean Coast)
- ⬜ Death Knight (Fog Rift Catacombs)
- ✅ Death Knight (Scorpion River Catacombs)
- ⬜ Death Rite Bird (Charo's Hidden Grave)
- ⬜ Demi-Human Queen Marigga (Cerulean Coast)
- ⬜ Demi-Human Swordmaster Onze (Belurat Gaol)
- ✅ Divine Beast Dancing Lion (Belurat, Tower Settlement)
- ⬜ Divine Beast Dancing Lion (Rauh Base / Ancient Ruins of Rauh)
- ✅ Dryleaf Dane (Moorth Ruins, Scadu Altus)
- ⬜ Fallingstar Beast (Hinterland / Fingerstone Hill)
- ⬜ Ghostflame Dragon (Cerulean Coast)
- ✅ Ghostflame Dragon (Gravesite Plain)
- ⬜ Ghostflame Dragon (Scadu Altus)
- ✅ Golden Hippopotamus (Shadow Keep)
- ⬜ Jagged Peak Drake (Jagged Peak)
- ✅ Jagged Peak Drake Duo (Foot of the Jagged Peak)
- ⬜ Jori, Elder Inquisitor (Darklight Catacombs, Abyssal Woods)
- ⬜ Lamenter (Lamenter's Gaol)
- ✅ Messmer the Impaler (Specimen Storehouse)
- ⬜ Metyr, Mother of Fingers (Finger Birthing Grounds)
- ⬜ Midra, Lord of Frenzied Flame (Midra's Manse)
- ⬜ Promised Consort Radahn (Enir-Ilim)
- ✅ Putrescent Knight (Stone Coffin Fissure)
- ✅ Rakshasa (Eastern Nameless Mausoleum, Scadu Altus)
- ⬜ Ralva the Great Red Bear (Scadu Altus)
- ⬜ Red Bear (Gravesite Plain)
- ✅ Rellana, Twin Moon Knight (Castle Ensis)
- ⬜ Romina, Saint of the Bud (Ancient Ruins of Rauh)
- ⬜ Rugalea the Great Red Bear (Rauh Base)
- ✅ Scadutree Avatar (Scaduview / Scadutree Base)
- ⬜ Tree Sentinel (Hinterland, Ambush)
- ✅ Tree Sentinel (Hinterland, Exposed)