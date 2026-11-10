# Bảng Boss "Đã Xác Minh" Nhưng Thiếu 6 Dungeon Boss, Radahn Biến Mất

**Date**: 2026-09-13 20:30
**Severity**: Critical
**Component**: Boss audit, `boss-flag-ids.tsv`, flag-to-name mapping
**Status**: Resolved

## What Happened

`boss-flag-ids.tsv` (199 rows, từ Smithbox IDs + convention `{areaNo}{blockNo}0800`) được dùng hàng tháng như source of truth. Đôm ngó lại thì sai hoàn toàn: 6 dungeon bosses bị thiếu, **Starscourge Radahn (một Shardbearer) không có**, và 3 hàng chứa GameAreaParam row ID thay vì `defeatBossFlagId` (trùng nhau ở 198/212 rows nên bug chả hiện).

Kết quả: Borealis báo "still alive" khi đã kill, Stray Mimic Tear báo "killed" khi chưa. Tôi nói user "84 bosses still alive" trước khi verify, số thật là 87.

## Nguyên Nhân

Bảng được verify một lần bằng method không thể thấy được cái bị thiếu. Sau đó nó cứ đứng yên ở trạng thái "đã check"—không ai xoay lại đối chiếu với source thật vì nó trông hoàn chỉnh (199 rows gọn gàng, nhóm theo vùng, có ghi chú verify cũ). Xem bên trong nó thì nó consistent—không contradiction nào—nên confidence cao.

User hỏi casual: "danh sách cây cavern và catacombs bạn có ko?" Đó mới bắt buộc đối chiếu.

## Fix

Đọc `regulation.bin` thay vì đoán: AES → DCX(zstd) → BND4 → `GameAreaParam.param`. File này chứa `defeatBossFlagId` + map id trực tiếp. Dùng kèm `BonfireWarpParam` (grace→map) và `WorldMapLegacyConvParam` (dungeon-map→overworld-tile) để gán tên. Convention guide sai Sealed Tunnel (là `m34_12`, ko phải `m32` range).

Kèm theo: `elden_ring_grace_unlock.py` toàn hỏng vì oracle dựa vào 9 grace Leyndell Royal Capital bật sáng—nhưng kill Maliketh làm capital thành tro, clear tất cả permanent. Fixed bằng drop Leyndell khỏi oracle.

## Lesson

Bảng verify một lần bằng method **có điểm mù** cứ đứng yên như "sạch". Internal consistency (ko contradiction trong 199 rows) != completeness (có phải tất cả 212 bosses ko). Ghi verify cũ làm confidence quá cao.

Cross-check completeness vs authoritative source (regulation.bin), ko phải self-consistency. Và user's offhand question hơn bất cứ audit nào của tôi.

## Next Steps

1. Boss audit drop handmade table, read trực tiếp `regulation.bin` + params
2. Setup control probes: chạy code trên fresh save để verify method trước khi apply lên save thật
3. Mỗi lần suggest số boss, trace nó từ regulation.bin, ko từ table
