# Dragonbolt Blessing: Stat Inversion + Bonus Recommendation Trap

**Date**: 2026-09-17 02:30
**Severity**: High
**Component**: Spell recommendation, wiki verification boundary
**Status**: Resolved

## What Happened

User hỏi về Lightning Strike incantation, tôi kéo wikitext thô từ eldenring.wiki.gg cho 2 trang (Lightning Strike + Ancient Dragons' Lightning Strike), trả lời chuẩn. Rồi tôi tự thêm gợi ý 7 spell Dragon Cult còn thiếu, gồi mô tả theo trí nhớ, không kéo wiki. Trong đó tôi khẳng định Dragonbolt Blessing "tăng lightning defence và cho poise trong lúc buff, dùng khi vào boss phun sét".

User sau đó hỏi giải thích cả 11 spell. Lần này tôi kéo wikitext đầy đủ cho tất cả trang. Wiki ghi rõ ràng: Dragonbolt Blessing GIẢM lightning negation 35% (tức mạng nhân vật dễ bị sét thương hại hơn), không cho poise, thứ nó cho là deflect khiên cho đòn light attack + 30 kháng tất cả status (bleeding, frost, etc).

Lời khuyên "dùng khi vào boss phun sét" là lời khuyên tệ nhất có thể cho spell này. Đúng ngược lại.

## The Brutal Truth

Cái này là lặp lại 260906 nhưng ở ranh giới khác. Phần được user HỎI (Lightning Strike) tôi verify kỹ bằng wiki thô, nó đúng. Phần tôi TỰ THÊM VÀO (Dragon Cult stack + Dragonbolt boost) tôi dựa vào "kinh nghiệm" từ trí nhớ, nó sai.

Ranh giới giữa "phần bắt buộc verify" và "phần bonus recommend" là chỗ tôi bơi trong. Tôi verify phần 1, rồi bỏ qua phần 2 vì nó "chỉ là gợi ý thêm". Nhưng nó vẫn là lời khuyên, vẫn sẽ ảnh hưởng tới gameplay của user.

Đau hơn ở chỗ: user tin tôi với phần 1, nên khi tôi nói "Dragonbolt Blessing tăng def", họ cũng tin. Không nghi ngờ. Chỉ phát hiện khi fetch wiki lần 2.

## Technical Details

**Wiki Dragonbolt Blessing (từ eldenring.wiki.gg):**
```
Effect: Decreases lightning negation by 35% for user
        + Grants Deflect for light attacks (single-hand)
        + Grants +30 immunity to all status (bleed, frost, poison, scarlet rot, madness)

Duration: 20 seconds
```

**Tôi nói:**
```
"Tăng lightning defence và cho poise trong lúc buff, 
 dùng khi vào boss phun sét"
```

Ngược hẳn. GIẢM kháng sét, không cho poise.

## What We Tried

1. Fetch wiki thô + phân tích → trả lời Lightning Strike, chuẩn
2. Thêm bonus 7 spell từ trí nhớ → không verify, ghi sai
3. User hỏi rõ 11 spell, kéo wiki lần 2 → lỗi bị phát hiện

## Root Cause Analysis

Tôi phân biệt không rõ "phần được verify" vs "phần tôi thêm thùng". Khi user hỏi Lightning Strike, đó là nhiệm vụ rõ ràng, tôi verify. Khi tôi tự gợi ý Dragon Cult spells, đó là bonus, tôi bỏ qua verify thinking nó chỉ là "thêm context tốt". Nhưng user sẽ paraphrase lại lời khuyên ấy: "tôi pick Dragonbolt vì tôi vào boss phun sét". Nó thành statement, không phải gossip.

Lesson từ 260906 là "đừng trust summarized fetch", nhưng bài học lớn hơn là "recommendation không kèm source thì không phải recommendation, đó là guess".

## Lessons Learned

1. **Bonus recommendation cũng là statement.** Phần tôi tự thêm vào câu trả lời không khác phần được hỏi—nó đều sẽ ảnh hưởng tới quyết định của user. Verify requirement phải đồng nhất.

2. **Ranh giới "bắt buộc" vs "bonus" là vô nghĩa khi cả hai đều public.** Tôi định: phần được hỏi = phải verify, phần thêm = ok không verify. Nhưng user không biết ranh giới ấy. Chỉ thấy "tôi nói spell X có tác dụng Y".

3. **Trí nhớ không phải source.** "Tôi nhớ Dragonbolt Blessing tăng def" không phải argument. Tôi phải nói: "wiki says ...", hoặc không nói cả.

## Next Steps

1. Khi recommend spell ngoài phạm vi user hỏi, phải fetch wiki trước. Nếu không fetch, không recommend.

2. Nếu copy recommendation từ trí nhớ vào câu trả lời, flag nó trong mind: "source?". Nếu trả lời không được "từ source X", xóa nó.

3. Recheck toàn bộ 7 spell Dragon Cult tôi recommend hôm trước, fetch wiki từng cái, ghi note cái nào nhớ sai. Không ghi từng detail lại, chỉ ghi "audit done, các stat này verify ok hoặc fix, ko pass".

Bài học 260906 là "đừng summarize", bài học 260917 là "đừng recommend mà không source", dù recommendation ấy "chỉ bonus thêm".
