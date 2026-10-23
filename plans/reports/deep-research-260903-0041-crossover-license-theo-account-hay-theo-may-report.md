# CrossOver: license theo account hay theo máy?

Research date: 2026-09-03. Pipeline: Brave + WebSearch (primary sources CodeWeavers) + Perplexity (search mode - Deep research mode đang hỏng do Perplexity đổi UI toggle) + validation 3 model (Gemini 3.1 Pro, Gemini 3.7 Flash, GLM-5.3 có fetch live source).

## TL;DR

CrossOver KHÔNG khóa theo device ID. License là per-user, gắn với account codeweavers.com. Cài lên bao nhiêu máy cũng được, sang máy khác chỉ cần login email+password trong app để unlock, ko cần deactivate máy cũ. Ràng buộc duy nhất: CrossOver+ (gói năm) chỉ được DÙNG 1 máy tại một thời điểm; CrossOver Life được dùng 3 máy đồng thời.

## Findings

1. **Per-user, ko phải per-device** - confirmed (4 nguồn chính chủ).
   - Licensing policy: "CrossOver is a per-user license. Install CrossOver on as many machines as you like, but only one person may use CrossOver per-license" - https://www.codeweavers.com/store/licensing (live, updated 06/2026).
   - EULA: "The license is not necessarily for a specific user, or a specific computer, but it is for one person at a time... run the Software on any computer, so long as no more than one person per license is ever using the Software at any one time" - https://www.codeweavers.com/crossover/eula.

2. **Giới hạn dùng đồng thời** - confirmed (blog chính chủ 2025-10-09 + blog Life 2022-11-09).
   - CrossOver+: cài thoải mái, 1 máy in-use tại một thời điểm.
   - CrossOver Life: cài và dùng 3 máy đồng thời.
   - https://www.codeweavers.com/blog/balfour/2025/10/9/dont-panic-how-crossover-licenses-work
   - GLM-5.3 verify live: model licensing ko đổi sau 10/2025, CrossOver 26/27 chỉ đổi compatibility.

3. **Unlock = login account trong app** - confirmed (support KB Mac user guide + installing-crossover).
   - CrossOver → Unlock CrossOver → nhập email+password codeweavers.com. Mua trực tiếp từ CodeWeavers thì ko cần serial; activation code chỉ cho mua qua bên thứ ba (nhập 1 lần, gắn vĩnh viễn vào account).
   - Unlock verify license online với codeweavers.com → cần internet lúc unlock (ko cần internet thường trực khi chơi).

4. **Ko có bước deactivate** - confirmed ở mức "ko có tài liệu nào tả cơ chế device cap / hardware fingerprint / device list trong account portal". Login máy 2 unlock luôn, máy 1 ko bị đụng. Lưu ý cả 3 model validation đều nhắc: absence of documentation ≠ bằng chứng ko enforce - nhưng use case 1 người 2 máy thì hợp lệ dưới mọi cách đọc EULA nên ko có rủi ro.
   - Chuyện "activation counter reset được qua support" cho Life: single-sourced (Reddit), unofficial.

5. **Hết hạn support license thì bản đang cài vẫn chạy** - confirmed (blog 10/2025 + store/licensing), nhưng validation thêm caveat đúng: "chạy mãi mãi" chỉ đúng khi macOS và game đứng yên. macOS update hoặc Elden Ring patch có thể làm bản cũ hỏng, lúc đó fix nằm sau paywall renew ($34/năm trong cửa sổ 13 tháng, renewal stack được). Với game còn được patch thì coi renew là chi phí định kỳ.

6. **License ko kéo theo data** - confirmed. Bottles (game cài trong đó, config) ko sync giữa 2 máy. Với Elden Ring ~80GB thì đừng export/import `.cxarchive` mỗi lần đổi máy (cả 3 model đồng thuận là impractical) - cài game riêng trên từng máy, save đi qua Steam Cloud như anh đang làm (nhớ mở game rồi thoát cho nó upload, như note cũ).

## Corrections từ vòng validation (đã áp vào findings trên)

- Quote "CrossOver does not enforce software licensing restrictions" (Advanced Linux Config) bị draft đầu dùng sai ngữ cảnh: câu đó nói về DRM của Windows app TRONG bottle, ko phải về enforcement license của chính CodeWeavers. Đã bỏ khỏi lập luận (cả 3 model bắt lỗi này).
- "Keeps working forever" thêm caveat macOS/game-patch (cả 3 model).
- `.cxarchive` chỉ dành cho migrate một lần, ko phải cơ chế switch máy (cả 3 model).

## Disagreements

- GLM-5.3 claim "Elden Ring ko có Steam Cloud saves" - SAI, mâu thuẫn với 2 Gemini và với chính setup 2 máy đang chạy của user (save đã sync qua Steam Cloud, có note riêng về hành vi upload). Bỏ claim này.
- Gemini 3.1 Pro claim "CodeWeavers có thể flag account nếu swap hardware nhanh" - speculation, ko nguồn. Ghi nhận là giả thuyết, ko phải finding.

## Open questions

- CodeWeavers có ghi nhận device nào đó server-side lúc unlock ko (silent registration) - ko có tài liệu công khai, chỉ trả lời được bằng cách hỏi support. Ko ảnh hưởng use case hiện tại.
- Perplexity Deep research mode đang unreachable qua driver (toggle ko switch, 3 lần fail sau cả restart daemon) - cần sửa driver theo UI mới của Perplexity.
