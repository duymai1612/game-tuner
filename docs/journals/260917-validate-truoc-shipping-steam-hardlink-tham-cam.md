# Validate Trước Khi Ship: Steam Hardlink Break Thầm Lặng, Comment Nói Dối

**Date**: phát hiện + sửa 2026-09-14, viết lại 2026-09-17
**Severity**: High
**Component**: Game patching, executable integrity, deep research validation
**Status**: Resolved

## What Happened

Deep-research session on "nên mua DLC ko" wrap up rồi report done. Adversarial multi-model validation (4 models, một cái read repo) catch defect mà nobody look: `warp.command:18` launch `Game\Warp`, comment claim "hardlink, same inode as eldenring.exe". Thực tế `ls -li` show: inode 104598139 (86,998,096 bytes, 20 Jul) for `Warp` vs 134916549 (87,042,128 bytes, 9 Sep) for `eldenring.exe`. Khác inode, khác size, khác ngày.

Steam patch bằng cách rewrite file mới, không modify in place. 1.17 update ra, nó tạo eldenring.exe mới, `Warp` thành orphaned copy của pre-patch binary. Comment assert invariant nhưng không ai enforce nó, nên Steam break nó thầm lặng. Game vẫn launch bình thường—nhưng chạy old code với new data. Vietnamese launcher không nhận 1.17 balance patch, DLC mới sẽ không có.

Session cũng catch: gọi 46% Steam score "review-bombing" là dodge vấn đề. Comments là price-versus-content, chính xác cái question đang hỏi.

Và nữa: "doc says Maliketh unkilled, save says khác, doc stale"—frame sai. Save break tie giữa hai docs, không contradict repo. Một doc đã đúng rồi, chỉ một stale. Undersell cái evidence riêng.

## The Brutal Truth

Cái này tiếp theo theo pattern 260906. Flow bình thường đã ship "go ahead, DLC ok" và user mua rồi phát hiện launcher hỏng. Adversarial pass là cái catch nó.

Cái tệ: comment `# cung inode voi eldenring.exe` trông đúng. Không có lỗi syntax, chỉ là nó không còn reflect reality khi Steam modify file. Không monitoring, không re-check trước launch, nó thầm lặng break.

## Technical Details

```
ls -li Game/
104598139  86998096  Warp            (20 Jul)
134916549  87042128  eldenring.exe   (9 Sep)
```

Different inodes = different files. Steam 1.17 patch tạo file mới, hardlink đã break. `Warp` point old inode (pre-1.17).

## Root Cause Analysis

Comment assert invariant nhưng zero validation code. Statement về system state mà không enforce = future bug waiting. External process (Steam) modify file system, comment become wrong thầm lặng.

Assertion without monitoring không phải invariant—nó chỉ belief bạn trust tới khi nó sai.

## Lessons Learned

1. **System state assertions need active checks.** Fix: re-link on startup, hoặc hard-fail nếu inode mismatch.

2. **Quiet failures worse than loud errors.** Game still run, chỉ absence symptoms. Absence harder spot than error.

3. **Adversarial validation works.** Model flag "unverified", inode check reveal bug. Ordinary session miss nó.

4. **Docs conflict: don't dismiss to older.** Save resolve tie = legit evidence, call out explicitly. Frame: "docs conflicted, save show B correct"—không "A stale".

## Next Steps

1. Re-link `Warp` → current inode
2. Patch `warp.command` check/re-link on startup, hoặc hard-fail
3. Update comment → "verified at startup: [current-inode]" hoặc similar

Adversarial cost vài model call. Ship wrong answer cost user time + trust. Không trade-off, mandatory.
