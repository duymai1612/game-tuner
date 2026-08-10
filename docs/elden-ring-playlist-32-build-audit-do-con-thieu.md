# 🎒 Audit 32 build trong playlist VoChoChoiGame - anh còn thiếu đồ gì

> Đối chiếu [playlist 32 build](https://www.youtube.com/playlist?list=PLWsanzojPwHeUgh6RGB0hJv9Ni4_OcRUV) (kênh VoChoChoiGame) với save thật của **dyu (slot 1, Lv 713)**, đọc trực tiếp `ER0000.sl2` ngày **2026-08-07**.
> Vũ khí lõi lấy từ **mô tả video** (ground truth), phần talisman/tear/AoW mà mô tả không nói thì lấy từ meta build đã tra wiki - có ghi rõ chỗ nào là suy đoán.
>
> Trạng thái sở hữu quét bằng **gaitem map**, nên tính cả đồ trong **rương** và **Ash of War đang gắn trên vũ khí** - hai chỗ mà `list-items` không thấy.

---

## ⚠️ Cập nhật 2026-08-09 - user đã chơi tiếp trên máy khác

Save kéo về ngày 2026-08-09 cho thấy **4 món trong bản audit này đã có rồi**, phần thân dưới
chưa được viết lại nên các con số tổng ở [TL;DR](#1-tldr) đang tính dư:

| Món | Build | Trạng thái mới |
|---|---|---|
| `Flowerstone Gavel` | #8 | ✅ đã có (nhánh standard của Priestess) |
| `Priestess Heart` | #8 | ✅ đã có |
| `Queelign's Greatsword` | - | ✅ đã có, nằm trong túi |
| `Heart of Bayle` | - | ✅ đã bơm 2026-08-09, đổi được `Bayle's Flame Lightning` ở Grand Altar |

Đã bơm thêm bằng `add-item` cùng ngày: `Dragonbolt of Florissax` (2006910) và spirit ash
`Ancient Dragon Florissax` (2215000), tức phần thưởng của **nhánh Priestess mà user đã bỏ**.

🔴 **Ba món vừa bơm CHƯA được kiểm chứng trong game.** Đây là lần đầu dùng `add-item` cho
spirit ash và incantation. Trước khi tin là đã có, phải mở game xem ash có trong danh sách
chuông triệu hồi và phép có memorize được không.

Còn thiếu và không đổi: `Bloodfiend's Arm` (#26), `Fire Knight's Greatsword` (#13, khác hẳn
`Queelign's Greatsword`, xem [checklist DLC](./elden-ring-dlc-questline-checklist-va-quest-path.md)),
`Maternal Staff` (#29, chơi nốt questline Ymir là ra).

---

## Mục lục
1. [TL;DR](#1-tldr)
2. [Vũ khí còn thiếu](#2-vũ-khí-còn-thiếu-24-loại)
3. [Talisman, tear, AoW, phép còn thiếu](#3-talisman-tear-aow-phép-còn-thiếu)
4. [Bảng 32 build](#4-bảng-32-build)
5. [Chiến lược gom đồ](#5-chiến-lược-gom-đồ)
6. [Cách kiểm chứng và điểm chưa chắc](#6-cách-kiểm-chứng-và-điểm-chưa-chắc)

---

## 1. TL;DR

Không build nào trong 32 cái là **đủ 100%** đồ, nhưng đa số chỉ thiếu vặt.

| Nhóm | Số build | Ý nghĩa |
|---|---|---|
| **Chỉ thiếu tear/talisman** (vũ khí đã có) | **13** build | #2, #3, #4, #9, #15, #17, #19, #21, #23, #24, #31, #32, #5 (thiếu 1 cây thứ 2) |
| Thiếu 1 vũ khí | 13 build | #1, #7, #11, #13, #14, #16, #18, #20, #22, #25, #26, #27, #28, #30 |
| Thiếu 2 vũ khí | 5 build | #8, #10, #12, #29, và #6 (cần cả 2 cây Cross-Naginata) |

Điểm mấu chốt: **thiếu nhiều nhất không phải vũ khí mà là crystal tear**. `Bloodsucking Cracked Tear` cần cho **9 build**, `Cerulean Hidden Tear` cần cho **6 build**, và cả hai anh đều chưa có. Hai món này lấy xong là nâng cấp được hơn nửa playlist cùng lúc.

Vũ khí thì **23 loại còn thiếu, trong đó 11 là đồ DLC**, mà anh mới ở đầu DLC nên gom được theo cụm khi đi Land of Shadow.

**Bloodfiend's Arm: đã dò kỹ, anh chưa có.** Món dễ nhầm là `Bloodfiend's Blood Fork` (anh có 2 cây, cũng đồ Bloodfiend ở DLC) - đó là vũ khí khác hẳn: Fork là great spear id 16540000, Arm là colossal weapon id 12530000. Xem cách kiểm chứng ở [mục 6](#6-cách-kiểm-chứng-và-điểm-chưa-chắc).

---

## 2. Vũ khí còn thiếu (23 loại)

⚠️ **Vũ khí là thứ duy nhất save editor KHÔNG thêm mới được.** Tool chỉ có `replace-weapon` (đổi một cây đang có thành cây khác, **cây gốc bị mất**), vì thêm entry mới cần thêm 13 byte mà slot save đã đầy. Anh có sẵn ~51 cây rác `+0` (Scimitar, Broadsword, Falchion, Weathered Straight Sword, Pike, Whip...) làm vật hiến tế, nên vẫn đủ dùng cho cả 24 món.

### DLC (11 loại) - gom theo cụm khi đi Land of Shadow

| Vũ khí | Build | Lấy ở đâu |
|---|---|---|
| **Bloodfiend's Arm** | #26 | Prospect Town, Gravesite Plain - Bloodfiend cầm chùy tay |
| **Great Katana** | #25 | Xác cạnh Ghostflame Dragon đang ngủ, hồ phía tây grace Greatbridge North |
| **Dragon-Hunter's Great Katana** | #30 | Ancient Dragon-Man đáy hầm Dragon's Pit, Gravesite Plain |
| **Rellana's Twin Blades** | #27 | Đổi remembrance Rellana ở chỗ Enia |
| **Backhand Blade** | #28 | Gravesite Plain, gần grace Castle Front |
| **Fire Knight's Greatsword** | #13 | Fire Knight cầm greatsword ở Shadow Keep (~4%) |
| **Messmer Soldier's Spear** | #22 | Messmer Soldier cầm giáo, khu Castle Ensis (~2%) |
| **Falx** | #16 | Giết NPC Hornsent trong questline (invade Shadow Keep / Church of the Bud / Enir-Ilim) |
| **Verdigris Greatshield** | #10 | Đánh bại Moore cuối questline của ông |
| **Maternal Staff** | #29 | Phần thưởng questline Count Ymir |
| ~~**Flowerstone Gavel**~~ | #8 | ✅ đã có từ 2026-08-09, xem block cập nhật đầu file |

> Lưu ý cho #16 và #10: hai món này **gắn với questline DLC**, mà questline hỏng thì mất luôn. Xem thứ tự an toàn ở [checklist DLC](./elden-ring-dlc-questline-checklist-va-quest-path.md).

### Base game (12 loại)

| Vũ khí | Build | Lấy ở đâu |
|---|---|---|
| **Sword of Night and Flame** | #11 | Rương tầng hầm Caria Manor, Liurnia |
| **Death's Poker** | #14 | Death Rite Bird ban đêm, đông grace Southern Aeonia Swamp Bank (Caelid) |
| **Lusat's Glintstone Staff** | #12 | Sellia Hideaway, cần `Sellian Sealbreaker` |
| **Carian Glintstone Staff** | #12 | Preceptor Miriam, Caria Manor |
| **Gravel Stone Seal** | #8 | Godskin Apostle ở Divine Tower of Caelid |
| **Clayman's Harpoon** | #7 | Clayman khu Raya Lucaria |
| **Antspur Rapier** | #10 | Maleigh Marais / invade Volcano Manor |
| **Grave Scythe** | #1 | Skeleton cầm lưỡi hái, nghĩa địa tây grace Lake-Facing Cliffs (~2%) |
| **Pickaxe** | #18 | Miner trong hầm mỏ, sớm nhất là Limgrave Tunnels (~2%) |
| **Bandit's Curved Sword x2** | #20 | Skeletal Bandit, dễ nhất ở ngoài Church of Pilgrimage (~1.5%) |
| **Cross-Naginata x2** | #6 | Hang phụ Gael Tunnel (Giant Land Octopus canh) - **chỉ 1 cây/lượt chơi** |
| **Godskin Peeler** (cây thứ 2) | #5 | Godskin Apostle ở Dominula - **chỉ 1 cây/lượt chơi** |

> #5, #6 và #20 là ba build **không farm đủ 2 cây trong một lượt chơi được** (Cross-Naginata và Godskin Peeler mỗi lượt chỉ 1 cây). Muốn powerstance thì hoặc NG+, hoặc dùng `replace-weapon` tạo cây thứ hai từ vũ khí rác.

---

## 3. Talisman, tear, AoW, phép còn thiếu

Nhóm này **thêm bằng editor được hết** (`add-item` cho talisman/tear/phép, `add-aow` cho Ash of War), nên rẻ hơn vũ khí rất nhiều.

### Crystal tear - ưu tiên số 1

| Tear | Số build cần | Ghi chú |
|---|---|---|
| **Bloodsucking Cracked Tear** | **9** | Tăng damage đổi lấy mất máu dần, món chủ lực của mọi build bleed |
| **Cerulean Hidden Tear** | **6** | FP không tốn trong 10 giây, xương sống của build spam skill/phép |
| Flame-Shrouding Cracked Tear | 2 | #4, #13 |
| Greenburst Crystal Tear | 1 | #17 |
| **Deflecting Hardtear** | 1 | #28 - món này định nghĩa cả build (mở cơ chế deflect) |

### Talisman

| Talisman | Số build | | Talisman | Số build |
|---|---|---|---|---|
| Two-Handed Sword Talisman | 5 | | Bull-Goat's Talisman | 2 |
| Fire Scorpion Charm | 3 | | Rellana's Cameo (DLC) | 2 |
| Dragoncrest Greatshield Talisman | 3 | | Faithful's Canvas Talisman | 1 |
| Graven-Mass Talisman | 3 | | Spear Talisman | 1 |
| | | | Graven-School Talisman | 1 |

Thiếu thêm cho build #9: **Ironjar Aromatic**. (**Priestess Heart** cho #8 thì đã có từ 2026-08-09.)

### Ash of War

`Royal Knight's Resolve` (3 build: #18, #19, #22) · `Ice Spear` (#7) · `Flame Skewer` (#13) · `Overhead Stance` (#25) · `Savage Lion's Claw` (#26) · `Blind Spot` (#28) · `Savage Claws` (#31)

> **Spinning Strikes (#1) anh đã có** - nó đang gắn trên một vũ khí nên không hiện trong túi đồ.

> **Seppuku anh đã có** (đang gắn trên vũ khí nên không hiện trong túi đồ), và 999 Lost Ashes of War đã set sẵn để nhân bản ở chỗ Hewg. Nhiều build bleed trong playlist dùng chung Seppuku nên coi như đã xong.

### Phép

`Knight's Lightning Spear` + `Ancient Dragons' Lightning Strike` (#8) · `Carian Slicer` (#12) · `Pest-Thread Spears` (#21, DLC) · `Impenetrable Thorns` (#29, DLC) · `Terra Magica` (#23, **chưa xác minh được tên trong DB item**)

---

## 4. Bảng 32 build

Cột "thiếu" đếm số món, không phải mức độ khó.

| # | Build | Vũ khí thiếu | Đồ khác thiếu |
|---|---|---|---|
| 1 | Scythe + Spinning Strikes | Grave Scythe | Bloodsucking Tear (AoW đã có) |
| 2 | Rivers of Blood | - | Bloodsucking Tear |
| 3 | Dual Bloodfiend's Fork | - (đã có 2 cây) | Bloodsucking Tear |
| 4 | Dual Magma Blade | - (đã có 2 cây) | Fire Scorpion Charm, Flame-Shrouding Tear |
| 5 | Dual Godskin Peeler | Peeler cây thứ 2 | Bloodsucking Tear |
| 6 | Dual Cross-Naginata | cả 2 cây | Bloodsucking Tear |
| 7 | Clayman's Harpoon + Ice Spear | Clayman's Harpoon | AoW Ice Spear |
| 8 | Dragon Cult Lightning | Gravel Stone Seal, Flowerstone Gavel | 2 phép, Faithful's Canvas Talisman |
| 9 | Great Stars tank | - | Bull-Goat's Talisman, Ironjar Aromatic |
| 10 | Verdigris Greatshield tank | Verdigris Greatshield, Antspur Rapier | Dragoncrest Greatshield, Bull-Goat's |
| 11 | Sword of Night and Flame | Sword of Night and Flame | Magic-Shrouding Tear |
| 12 | Carian Slicer battle-mage | Lusat's + Carian Glintstone Staff | Carian Slicer, Graven-Mass |
| 13 | Fire Knight's Greatsword | Fire Knight's Greatsword | AoW Flame Skewer, Fire Scorpion, Flame-Shrouding |
| 14 | Death's Poker | Death's Poker | Cerulean Hidden Tear |
| 15 | Moonveil | - | Cerulean Hidden Tear |
| 16 | Falx | Falx | - |
| 17 | Gargoyle's Twinblade | - | Greenburst Crystal Tear |
| 18 | Pickaxe | Pickaxe | AoW Royal Knight's Resolve |
| 19 | Giant-Crusher | - | AoW RKR, Two-Handed Sword, Dragoncrest Greatshield |
| 20 | Dual Bandit's Curved Sword | cả 2 cây | - |
| 21 | Pest-Thread Spears | - | phép Pest-Thread Spears, Cerulean Hidden Tear |
| 22 | Messmer Soldier's Spear | Messmer Soldier's Spear | AoW RKR, Spear + Two-Handed Sword Talisman |
| 23 | Dark Moon Greatsword | - | Terra Magica |
| 24 | Marais Executioner's Sword | - | Cerulean Hidden Tear |
| 25 | Great Katana "4 trong 1" | Great Katana | AoW Overhead Stance, Rellana's Cameo, 2H Sword, Bloodsucking |
| 26 | Bloodfiend's Arm | Bloodfiend's Arm | AoW Savage Lion's Claw + 2 món |
| 27 | Rellana's Twin Blades | Rellana's Twin Blades | Rellana's Cameo |
| 28 | Backhand Blades + Deflect | Backhand Blade | Deflecting Hardtear, AoW Blind Spot |
| 29 | Impenetrable Thorns | Maternal Staff (Guilty đã có) | phép Impenetrable Thorns, Graven-Mass, Cerulean Hidden |
| 30 | Dragon-Hunter's Great Katana | Dragon-Hunter's Great Katana | 2H Sword Talisman, Bloodsucking |
| 31 | Beast Claw (DLC) | - | AoW Savage Claws, Bloodsucking Tear |
| 32 | Night Comet + Staff of Loss | - | Graven-Mass, Graven-School, Cerulean Hidden |

---

## 5. Chiến lược gom đồ

Xếp theo tỉ lệ "công bỏ ra / số build mở khoá":

**Bước 1 - hai crystal tear, mở khoá 15 build.** `Bloodsucking Cracked Tear` (9 build) và `Cerulean Hidden Tear` (6 build). Thêm bằng `add-item --key` là xong trong một lệnh.

**Bước 2 - dọn nốt talisman + AoW + phép bằng editor.** Toàn bộ mục 3 làm được offline, không phải chạy đi đâu. Sau bước này mọi build chỉ còn thiếu đúng vũ khí.

**Bước 3 - đi DLC một chuyến, gom 11 vũ khí DLC.** Trùng luôn với việc anh đang cần làm questline DLC. Hai món `Falx` và `Verdigris Greatshield` phải theo questline nên bám đúng thứ tự trong checklist DLC.

**Bước 4 - vũ khí base game.** 13 món, phần lớn là farm drop tỉ lệ thấp (Grave Scythe 2%, Pickaxe 2%, Bandit's Curved Sword 1.5%). Nếu ngại farm thì `replace-weapon` từ đám vũ khí rác `+0`, nhưng nhớ là cây gốc mất luôn.

---

## 6. Cách kiểm chứng và điểm chưa chắc

**Đã kiểm chứng:**
- Trạng thái sở hữu: quét **gaitem map** của slot 1 (không phải `list-items`), đối chiếu theo **item ID gốc** chứ không so tên. Hai chi tiết quan trọng:
  - Affinity nằm **giữa** tên: `Bloodfiend's Blood Fork` (16541100) chính là bản Blood của `Bloodfiend's Fork` (16540000), so tên thuần sẽ báo thiếu nhầm.
  - `list-items` **chỉ đọc túi đồ**, bỏ sót đồ trong rương và Ash of War đang gắn trên vũ khí. Bản audit đầu tiên dùng nó nên báo thiếu nhầm `Ash of War: Spinning Strikes` và `Staff of the Guilty`.
- Dòng control chứng minh gaitem map đọc được rương: `Ronin's Set` (Iron Kasa + Armor + Gauntlets + Greaves) hiện đầy đủ trong gaitem map với cờ `held: False`, đúng như anh nói là đã lấy. Nhờ control này mà kết luận "không có Bloodfiend's Arm" mới đáng tin - quét cả dải 12530000-12531299 (13 biến thể affinity) không ra entry nào.
- Vũ khí lõi của cả 32 build: lấy từ **mô tả chính video**, không phải suy đoán.
- Mọi tên item trong tài liệu này đã đối chiếu với `elden_ring_items_full_reference.json` để chắc chắn tồn tại trong game.

**Chưa chắc, đừng tin tuyệt đối:**
- Talisman/tear của các build mà mô tả video không liệt kê (phần lớn build từ #13 trở đi) là **meta build tra từ wiki**, không phải nội dung chính xác trong video. Muốn chuẩn 100% thì phải xem đoạn "Hướng dẫn Build" trong video.
- Ash of War của #1, #6, #18, #19, #20, #22 là **suy đoán từ cách mô tả lối chơi**, chưa xác nhận.
- `Terra Magica` (#23) không tìm thấy trong file item reference của repo. Có thể file thiếu, có thể tên khác - cần kiểm lại trước khi đi tìm.
- Playlist có **5 video bị ẩn/không khả dụng** (YouTube báo), nên có thể playlist gốc nhiều hơn 32 build.
- Quét gaitem map bỏ qua entry mang tiền tố `[NPC]` (đồ của NPC triệu hồi, người chơi không nhặt được). Còn **4414 entry không tra được tên** trong bảng item của repo - phần lớn là entry rỗng, nhưng nếu một món nào đó nằm trong nhóm này thì tài liệu sẽ báo thiếu nhầm. Riêng các món trong danh sách trên đều dò theo dải ID nên không dính lỗi này.
