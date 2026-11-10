# Có nên mua DLC Elden Ring mới ra mắt không?

Ngày tra: 2026-09-14 · Save đọc trực tiếp cùng ngày (`dyu`, slot 1, Lv713)

## TL;DR

Mua. DLC mới là **Tarnished Pack**, ra 28/08/2026, **119.000₫** trên Steam VN, không giảm giá.

Launcher đã sửa xong 14/09 (xem mục dưới) - trước đó `warp.command` chạy binary cũ từ 20/07 nên
bản Việt hóa chưa thực sự ở 1.17.

Biết trước ba điều: đây là gói gear + cosmetic chứ không phải expansion (không map mới, không boss
mới); một trong hai NPC invasion đã mất trên character `dyu` **ở chu kỳ này** (lấy lại ở NG+); và
phần thay đổi gameplay lớn nhất đợt này là patch 1.17 **miễn phí**.

Món đáng tiền nhất cho anh: `Reed Great Katana` - great katana đầu tiên nằm ở Lands Between
(không phải Realm of Shadow), 55 Blood Loss sẵn, nằm ở Caelid lấy được ngay.

## `Warp` là bản cũ - ĐÃ SỬA 14/09

`warp.command:18` trỏ vào `Game\Warp`. Comment trong script nói `Warp` là hardlink **cùng inode**
với `eldenring.exe`, tốn 0 byte. Điều đó **không còn đúng**:

| File | inode | size | ngày |
|---|---|---|---|
| `Warp` | 104598139 | 86.998.096 | **20/07** |
| `eldenring.exe` | 134916549 | 87.042.128 | **09/09** |

Khác inode, lệch 44KB. Steam patch bằng cách ghi file mới chứ không sửa tại chỗ, nên hardlink đứt
lúc lên 1.17 và `Warp` thành một bản copy mồ côi của exe **trước 1.17**.

Hệ quả: chạy qua `warp.command` = chạy exe cũ trên data 1.17. Nghĩa là bản Việt hóa của anh
**không có** buff parry / fix Great Katana crit, và nếu mua Tarnished Pack thì đồ mới nhiều khả
năng không hiện. Chạy qua Steam thẳng (`eldenring.exe`) thì đúng 1.17.1.

**Đã sửa 14/09:**

1. Nối lại hardlink. `Warp` và `eldenring.exe` giờ cùng inode `134916549`, link count 2. Exe cũ
   giữ lại ở `Warp.old-260720` (87MB, xoá lúc nào cũng được - một mình nó không roll back được gì
   vì `regulation.bin` và `Data0` đã là 1.17).
2. Vá `warp.command` để tự chữa: mỗi lần chạy nó so inode `Warp` với `eldenring.exe`, lệch thì
   `ln -f` lại rồi mới launch, nối thất bại thì dừng hẳn chứ không chạy nhầm exe cũ. Đã test 3
   nhánh (link đứt / đã khớp / `Warp` bị xoá) trong sandbox, `sh -n` sạch.

Nên từ giờ Steam patch bao nhiêu lần cũng không cần nhớ làm tay.

**Rủi ro thứ hai: text Việt hóa của đồ mới sẽ trống.** Đã soi cụ thể, mod override
`mod/msg/engus/` gồm `item.msgbnd.dcx`, `menu.msgbnd.dcx` và 4 file dlc, tất cả ngày **25/07**.
me3 override nguyên file theo path, mà tên + mô tả đồ Tarnished Pack nằm trong bản `item/menu
.msgbnd` của 1.17. File đè lên nó là bản cũ hơn nên không có mấy entry đó.

Không crash, chỉ là tên/mô tả trống. Cách vòng: săn đồ mới thì chạy thẳng qua Steam
(`eldenring.exe`, tiếng Anh), chơi cốt truyện thì dùng `warp.command`. Hoặc chờ The Red Team cập
nhật. Chưa quan sát trong game, mới suy từ ngày file + cách me3 override.

## Cái gì vừa ra

| | |
|---|---|
| Tên | ELDEN RING Tarnished Pack (Steam app `3655690`) |
| Ra mắt | 28/08/2026, cùng ngày bản Switch 2 `Tarnished Edition` |
| Giá | $4.99 / €4.99 / ¥550 · **119.000₫** ở VN, 0% giảm |
| Yêu cầu | Base game + patch 1.17. **Không** bao gồm Shadow of the Erdtree |
| Steam review | Mixed, ~46-48% positive, ~1.700-2.400 review |

`Tarnished Edition` là gói Switch 2 (game + SOTE + đồ mới). `Tarnished Pack` là phần đồ mới bán
riêng cho PS/Xbox/PC. Anh chỉ cần cái sau.

Điểm thấp chủ yếu vì **giá so với lượng nội dung**: bắt người đã mua game trả thêm cho nội dung
bonus của bản Switch 2, so sánh với "horse armor" $5 của Oblivion. Đừng gạt đi như review-bomb lạc
đề - đó đúng là câu hỏi anh đang hỏi. Coi nó là dữ kiện: phần đông người mua thấy gói này mỏng so
với giá. Anh vẫn có thể thấy đáng vì lý do riêng (xem mục dưới), nhưng đó là ngoại lệ có lý do, chứ
không phải vì đám đông sai.

## Trong gói có gì, và cái nào anh lấy được

Patch notes 1.17 chính thức ghi nguyên văn: *"The following elements will be added upon purchase of
the 'Tarnished Pack' DLC."* Toàn bộ danh sách dưới đây bị khoá sau ownership - không mua thì xác
nằm đó rỗng, không có prompt nhặt.

**Lấy được ngay trên save hiện tại:**

| Món | Chỗ lấy |
|---|---|
| `Reed Great Katana` | Caelid, mound lớn phía bắc grace `Fort Faroth` (Dragonbarrow), leo bằng Torrent. 158 phys, D/D Str/Dex, **55 Blood Loss**, skill `Overhead Stance` |
| `Reverse-Bladed Sword` | Mua ở Twin Maiden Husks, Roundtable Hold |
| `Ritual Thrusting Shield` | Caelid Colosseum, sau Great Jar, từ grace `Deep Siofra Well` đi tây |
| `Hefty Scimitar` | Nomadic Merchant phía bắc grace `Fort Haight West`, nam Limgrave |
| `Idus Sword` + `Silver Grooved Set` | Kiếm dưới gốc cây bắc grace `Liurnia Lake Shore`; giáp mua ở Nomadic Merchant bắc `Bellum Church` |
| `Steel Set` | Isolated Merchant's Shack, Weeping Peninsula |
| `Knight Leontiel Set` + `Leontiel's Greatsword` | Quay lại arena Starscourge Radahn qua grace, đi bắc → Knight Leontiel invade. Radahn đã chết nên mở |
| 3 Torrent skin | `Tree Sentinel` (Stormveil, sau Godrick) · `Silver of Caria` (Liurnia, Ranni's Rise) · `Funereal Night` (Altus Plateau) |

**Đã mất trên chu kỳ này:**

`Golden Order Flail` + `Broken Gold Mask` + `Gold Tattoo` (chest/arm/leg) - drop từ invader
`The Noble Broken Mask` ở Erdtree Sanctuary, **Leyndell Royal Capital**. Điều kiện: cast
`Law of Regression` (cần 37 INT) trước tượng Radagon.

Mốc khoá là **Maliketh chết → Leyndell thành Ashen Capital**. Save của anh: flag `13000800`
(`Malekith, the Black Blade`) = **dead**. Nên event này không bao giờ fire nữa ở cycle hiện tại.
Đây là payout to nhất của cả gói: một vũ khí unique + nguyên set 4 món từ một trận.

Lấy lại được ở **NG+** (Leyndell reset về Royal Capital). Hoarah Loux và Gideon vẫn `alive` trong
save nên anh chưa qua NG+, còn nguyên cơ hội ở vòng sau. Nhớ làm **trước khi đốt Erdtree** vòng đó.

## Cái anh đã có miễn phí

Patch 1.17 (27/08) là bản balance đầu tiên sau gần 1 năm, miễn phí cho tất cả. Máy anh đã lên rồi:
`regulation.bin` ngày 09/09, `Data0.bdt` ngày 11/09 → đang ở 1.17.1.

Liên quan trực tiếp đến build anh đang chơi:

- **Parry buff** - giảm thời gian hồi sau khi parry với Dagger, Curved Sword, Small Shield. Đúng
  thứ doc `elden-ring-build-parry-dagger-va-great-stars.md` đang xoay quanh.
- **Great Katana** - fix bug crit yếu bất thường khi đánh enemy to.
- `Rakshasa's Great Katana` - nerf delay tay phải khi cầm nó tay trái (áp dụng chung). Phần ăn thêm
  damage lúc attack là **PvP-only**, anh chơi offline nên không dính. Đừng bỏ vũ khí vì tưởng bị nerf nặng.
- Shield: **14 cái** tăng guard boost + giảm weight, **9 cái** chỉ tăng guard boost, **1 cái** chỉ
  giảm weight. `Storm Wall` hết tốn FP.

Nói cách khác: thứ làm thay đổi cách chơi nhiều nhất trong đợt này là bản **miễn phí**, không phải
119k. Nhưng xem mục `Warp` ở trên - nếu anh chơi bản Việt hóa thì hiện chưa thực sự có nó.

## Mấy thứ khác cần biết

**CrossOver không cản.** Hai NPC invasion là sự kiện NPC offline, không phải PvP, nên EAC hỏng
không ảnh hưởng. Entitlement DLC do Steam quản, tách khỏi EAC. Toàn bộ gói chơi solo được.

**Save-edit thay cho mua: được một phần, nhưng không thay được hết.** Nói cho đúng thay vì nói cho
xuôi: editor `add-item` được goods/talisman/AoW (anh làm hôm 13/09 với lightning strike), và
`replace-armor`/`replace-weapon` retarget được món đang có - phá món cũ, rẻ với inventory Lv713.
Em **không có bằng chứng** game check entitlement lúc runtime offline; bản vá 1.17.1 chỉ bịt một
đường multiplayer, không liên quan tới người chơi offline.

Ranh giới thật là: **NPC invasion event thì tool không tạo được**, và ID đồ mới phải có sẵn trong
regulation 1.17 (`elden_ring_param_dump.py` kiểm được). Nên lựa chọn thật là "119k mua đường chính
thức, hay tự bơm phần đồ rồi mất hai trận invasion". Với 119k trên một save Lv713 đã 500+ giờ thì
đường chính thức gọn hơn.

**Không có gì để chờ.** Không tìm thấy DLC Elden Ring nào khác được công bố kèm ngày. Món trả phí
gần đây khác trong franchise là `Nightreign: The Forsaken Hollows` (04/12/2025, $15 / ~300.000₫)
nhưng nó cần **Nightreign - game riêng, không thấy cài trong bottle**. Chu kỳ DLC của Nightreign
được *báo chí* cho là đã khép, không phải FromSoft tuyên bố.

## Nguồn

- Patch notes 1.17 chính thức: https://en.bandainamcoent.eu/elden-ring/news/elden-ring-patch-notes-version-117
- Cách lấy nội dung mới (Bandai): https://en.bandainamcoent.eu/elden-ring/news/how-get-new-elden-ring-classes-weapons-and-torrent-skin-customizations
- Steam: https://store.steampowered.com/app/3655690/ELDEN_RING_Tarnished_Pack/
- Fextralife Tarnished Pack: https://eldenring.wiki.fextralife.com/Tarnished_Pack
- wiki.gg `Reed Great Katana` (xác nhận exclusive DLC): https://eldenring.wiki.gg/wiki/Reed_Great_Katana
- wiki.gg `Golden Order Flail`: https://eldenring.wiki.gg/wiki/Golden_Order_Flail
- Fextralife `The Noble Broken Mask`: https://eldenring.wiki.fextralife.com/The_Noble_Broken_Mask
- KeenGamer (mốc khoá Maliketh + NG+): https://www.keengamer.com/articles/guides/how-to-find-knight-leontiel-and-noble-broken-mask-in-elden-ring-tarnished-edition/
- Patch 1.17.1 vá đường lấy đồ DLC miễn phí: https://www.eurogamer.net/elden-ring-patch-1-17-1-fix-tarnished-dlc-duplication-glitch
- Review bombing: https://www.thegamer.com/elden-ring-tarnished-pack-mixed-reviews-steam/

## Độ tin của từng claim

| Claim | Mức |
|---|---|
| Tên/ngày/giá USD-EUR/nội dung gói | confirmed - patch notes chính thức + 3 nguồn độc lập |
| Nội dung bị khoá sau ownership trong lối chơi solo bình thường | confirmed - patch notes nguyên văn + wiki.gg ghi "exclusive to" + nhiều guide ghi xác rỗng nếu không có DLC. Không phải bằng chứng mọi đường transfer/mod đều bị chặn |
| Malekith đã chết trên save | confirmed - flag `13000800` đọc trực tiếp, **và** `docs/elden-ring-boss-va-dieu-kien-can-xong-truoc-khi-danh.md:35,234` đã ghi đúng như vậy từ trước |
| Leyndell invasion mất ở cycle này, lấy lại ở NG+ | confirmed - patch notes ghi mốc Ashen Capital; KeenGamer + nerdschalk ghi trigger là Maliketh chết và NG+ mở lại |
| `Warp` là exe cũ trước 1.17 | confirmed - `ls -li` cho inode + size + ngày khác nhau, tự kiểm |
| **Giá 119.000₫** | **single-sourced** - SteamDB regional pricing; Steam storefront chặn từ môi trường này. $4.99 thì confirmed |
| Steam review ~46-48% Mixed | confirmed - 3 snapshot, lệch do thời điểm crawl và bộ lọc ngôn ngữ |
| Chưa sở hữu Tarnished Pack | **suy ra, chưa chắc** - `InstalledDepots` thiếu `3655690` chỉ chứng minh **chưa cài**, không phải chưa mua. Kiểm trong Steam library trước |
| Caelid invasion còn mở | **suy ra** - guide ghi "no deadline" và Radahn đã chết; chưa tự xác minh đủ điều kiện trigger |
| Không có DLC ER nào sắp ra | ở mức "không tìm thấy công bố có ngày" - không phải bảo chứng đã ngừng phát triển |
| Text Việt hóa hỏng với đồ mới | **chưa xác minh** - suy từ ngày file `mod/msg/` (25/07) + cách me3 override |

## Câu chưa chốt

- Số vũ khí mới: nguồn ghi **6 hoặc 7** tuỳ có tính `Ritual Thrusting Shield` là weapon hay không.
  Patch notes chính thức không nêu số.
- Giá 119.000₫ chưa tự xác minh tại checkout - mở store xem lại trước khi bấm mua.
- Torrent attire là item loại goods hay unlock flag? Nếu là goods thì `add-item` có thể tự bơm -
  chưa kiểm. Ranh giới chắc chắn duy nhất mà tool không làm được là **NPC invasion event**.
- Gói này có thêm achievement nào không - chưa tra.
- `docs/elden-ring-questline-checklist-va-quest-path.md:513` ghi Maliketh **chưa giết**, mâu thuẫn
  với save và với chính doc boss. Doc đó stale, soát lại các dòng phụ thuộc mốc Maliketh.
