# Đối chiếu bảng cờ boss với GameAreaParam - đã sửa gì, còn hở gì

2026-09-13 · `boss-flag-ids.tsv` 199 → 206 dòng · save `dyu` slot 1 đọc lúc `--base 0x3850d`

Bảng cờ boss được dựng tay từ Smithbox nên thiếu và sai lẫn nhau. Nguồn chuẩn có sẵn trong máy:
`GameAreaParam` trong `regulation.bin` mang thẳng `defeatBossFlagId` + map id của từng đấu trường,
nên không cần đoán quy ước `{area}{block}0800` nữa.

---

## Đường lấy ground truth

`regulation.bin` → AES → DCX(zstd) → BND4 → `GameAreaParam.param`, dùng lại `elden_ring_regulation.py`.
Offset field suy từ `soulsmods/Paramdex` `ER/Defs/GameAreaParam.xml`: `defeatBossFlagId` ở **68**,
`bossMapAreaNo/BlockNo/MapNo` ở **84**. Bẫy giống lần đọc `BonfireWarpParam`: hai bitfield đầu file
(`u8 disableParam_NT:1` + `dummy8 :7`) **dùng chung một byte**, tách ra là mọi offset lệch 4.

Ra 216 row, 212 row thật. Đối chiếu với 199 dòng của bảng: **185 khớp**, 22 cờ có trong param mà
bảng không có, 11 dòng của bảng không phải row `GameArea` nào.

Ba lệnh dump đã đóng gói lại thành `elden_ring_param_dump.py {bosses|graces|maps}` để lần sau
không phải viết lại parser trong scratchpad rồi mất.

Hai param phụ dùng để định danh map:
- `BonfireWarpParam` → grace nào nằm trong map nào (`m30_15_00` có grace `Caelid Catacombs`).
- `WorldMapLegacyConvParam` → map hầm ứng với ô overworld nào. Đây là thứ gỡ được chỗ mập mờ cuối:
  `m32_11 → m60_47_55` = ô của grace `Yelough Anix Tunnel`, còn `m34_12 → m60_43_50` = ô của grace
  `Sealed Tunnel`. Nghĩa là Sealed Tunnel **không** nằm trong dãy `m32` như tên gọi gợi ý.

## Đã thêm 7 dòng

| Cờ | Boss | Trạng thái trong save |
|---|---|---|
| `30150800` | Cemetery Shade (Caelid Catacombs) | còn sống |
| `30160800` | Putrid Tree Spirit (War-Dead Catacombs) | còn sống |
| `31200800` | Cleanrot Knights (Abandoned Cave) | đã hạ |
| `32000800` | Scaly Misbegotten (Morne Tunnel) | đã hạ |
| `34120800` | Onyx Lord (Sealed Tunnel) | đã hạ |
| `35000850` | Esgar, Priest of Blood (Leyndell Catacombs) | còn sống |
| `1252380800` | **Starscourge Radahn** | đã hạ |

Radahn là phát hiện đáng kể nhất: một Shardbearer vắng mặt hoàn toàn khỏi bảng, không phải boss hầm.

## Đã sửa 3 cờ sai

Cả ba đều là cùng một lỗi: bảng chép **row ID** của `GameAreaParam` thay vì `defeatBossFlagId`.
Hai giá trị này trùng nhau ở 198/212 row nên lỗi không lộ ra.

| Boss | Cũ | Mới | Ảnh hưởng thật |
|---|---|---|---|
| Borealis the Freezing Fog | `1054560800` | `1254560800` | báo còn sống, thật ra **đã hạ** |
| Stray Mimic Tear (Hidden Path) | `30200800` | `30200810` | báo đã hạ, thật ra **còn sống** |
| Crucible Knight Siluria | `12030390` | `12020390` | không đổi, cả hai đều đọc ra còn sống |

Sau khi sửa: **119/206 đã hạ**, base 103/164, DLC 16/42.

## Còn hở - chưa sửa

**Ba cặp dòng trùng cờ.** Hai dòng khác tên đọc cùng một bit, nên tổng bị đếm hai lần:

| Cờ | Hai dòng đang dùng | Đã biết gì |
|---|---|---|
| `1036500800` | Alabaster Lord (Evergaol) · Onyx Lord (Royal Grave Evergaol) | map là `m60_36_50`, ô z=50 là Altus. Wiki ghi Royal Grave Evergaol nằm ở **Liurnia**, nên cờ này thuộc Alabaster Lord, còn Onyx Lord cần cờ khác |
| `1042380850` | Bell Bearing Hunter (Warmaster's Shack) · Deathbird (Warmaster's Shack) | map `m60_42_38` có đúng hai cờ `...0800` và `...0850`; `...0800` bảng đang gán cho "Deathbird (Limgrave)". Wiki ghi Deathbird ở "east of Warmaster's Shack", tức nhiều khả năng hai dòng Deathbird là **một con** |
| `1050570800` | Death Rite Bird (Mountaintops) · Erdtree Avatar (Mountaintops) | map `m60_50_57` có `...0800` và `...0850`; `...0850` bảng đang gán cho "Putrid Avatar" |

Chưa sửa vì gỡ đúng tên cần soát từng con trên wiki, không phải suy từ param.

**16 cờ trong param vẫn chưa có tên.** Đáng chú ý:

- `20010850` - `m20_01` Enir-Ilim, đấu trường thứ hai của map. Nhiều khả năng là màn gank Leda.
- `19000800` - `m19_00` phòng Fractured Marika. Bảng đang dùng `19000810` cho "Radagon / Elden Beast",
  nên đây là con còn lại trong cặp.
- `18000800` - `m18_00` Stranded Graveyard. Cặp với `18000850` (Soldier of Godrick), chưa rõ là gì.
- `34120800` đã dùng; còn `1034420800`, `1037510800`, `1039440800`, `1041530800`, `1051400800`,
  `1036450340`, `1036480340`, `1037420340`, `1039430340`, `1254560800`, `12030800`, `12030850`.

**11 dòng của bảng không phải row `GameArea`.** Gồm Elder Dragon Greyoll, Dryleaf Dane, và 5 con
field boss ở Liurnia/Altus. Không có nghĩa là sai - nhiều boss ngoài trời không có row `GameArea` -
nhưng cũng chưa có gì xác nhận chúng đúng.

**Ô map của vài dòng không khớp vùng ghi trong tên.** Rõ nhất: `1035500800` mang tên
"Royal Knight Loretta (Caria Manor)" nhưng map là `m60_35_50`, ô z=50 tức Altus, còn Caria Manor
ở bắc Liurnia. Chưa soát hết nhóm này.

**Evergaol thì không thiếu con nào.** `Category:Evergaols` trên wiki có đúng 10 evergaol
(Cuckoo's, Forlorn Hound, Golden Lineage, Lord Contender's, Malefactor's, Ringleader's, Royal Grave,
Sellia, Stormhill, Weeping) và bảng có đủ cả 10, tất cả đều là row `GameArea` thật. Vấn đề duy nhất
của nhóm này là cờ Royal Grave đang trùng với Alabaster Lord, đã ghi ở bảng trên.

## Sửa kèm: `boss-report` đã chạy được trở lại

Không liên quan bảng cờ nhưng chặn mọi thứ: sau khi Maliketh chết, `elden_ring_grace_unlock.py`
từ chối chạy trên save này. Oracle dò base đòi **cả 9 grace `LeyndellRoyalCapital` phải sáng**, mà
chúng tắt sạch khi thành hoá tro, nên `find_base` ra 0 nghiệm và `--base` tay cũng bị `check_base`
chặn (14/23). Đã bỏ `LeyndellRoyalCapital` khỏi cả hai set. 14 grace còn lại vẫn cho **đúng một
nghiệm** trên cả save hiện tại (`0x3850d`) lẫn backup 06/09 (`0x386db`), nên độ chặt không mất.

Base vẫn đổi sau mỗi phiên chơi (`0x373a1` → `0x37551` → `0x3850d`) vì gaitem map phía trước nó dài
ra, nhưng giờ tự dò lại được nên không phải truyền tay.

## Muốn đóng hẳn thì làm gì

Dựng lại bảng từ `GameAreaParam` làm gốc thay vì vá: 212 row, mỗi row đã có sẵn cờ và map id, chỉ
thiếu tên. Tên lấy từ `WorldMapLegacyConvParam` + `BonfireWarpParam` để ra vùng, rồi đối chiếu wiki
theo vùng. Làm xong thì hết trùng, hết lẫn row ID với cờ, và biết chắc con số tổng.

## Câu hỏi chưa giải quyết

- `30200800` đang bật trong save dù `30200810` (cờ hạ thật của Stray Mimic Tear) tắt. Chưa rõ
  `...0800` ở map đó đại diện cho cái gì - có thể là cờ "đã vào đấu trường".
- `1043530800` là `defeatBossFlagId` của **ba** row khác map (`m60_39_51`, `m60_43_53`, `m60_44_53`).
  Chưa rõ là một boss trải nhiều ô hay param có lỗi.
- Có bao nhiêu Deathbird thật: bảng đang liệt kê 4, wiki infobox chỉ liệt kê 2 vùng.
