# Confident Wrong Answer: Model Summaries Are Not Raw Source

**Date**: 2026-09-06 21:05
**Severity**: High
**Component**: Save audit, questline branch validation, item probing
**Status**: Resolved

## What Happened

I recommended "gold" summon sign in the Hornsent questline to resolve a branch question. Gave it confidently. Two Codex models running adversarial validation both rejected the recommendation. I checked raw wikitext from the eldenring.wiki.gg MediaWiki API and they were right: gold branch ends Leda's questline until Enir-Ilim, mutually exclusive with Ansbach's Longbow. Correct answer was "neither".

Root: I built that recommendation on WebFetch summaries of guide sites. Game8's summary had silently inverted which branch gives which reward. I treated the fetched summary as equivalent to reading the wiki page itself. It was not.

Same session, three separate probe failures with identical failure mode. Bell bearings: read 2/63 "missing" (they are consumed when handed to an NPC, so holding 61 of them means 61 consumed, not 61 missing). Map fragments: read 4 missing (event flags were edited to unlock maps instead of collecting them physically, so the "unacquired" count was wrong). Talisman Pouch and Memory Stone: read as "unspent" (both are Key Items with max_held=3 and max_held=8 respectively; holding all of them means inventory full, not upgrades left unused).

Each would have produced a confident wrong statement to the user. Control lines caught all three.

## The Brutal Truth

This is infuriating because the wrong answer FELT right. "Gold" was a plausible recommendation, Game8 had numbers that looked authoritative, and I had no reason to distrust a Codex fetch-and-summarize workflow. That's exactly why this hurt: the wrong answer was textbook-confident, not obviously broken.

The talisman and map fragment probes are worse because they are silent failures. The code doesn't error. The returned numbers are mathematically sensible. They just measure the wrong thing. If I had not injected control lines on items I already knew the answer to (Nomadic Warrior's Cookbook [1] in inventory at game start), I would have shipped statements about "4 missing map fragments" and "unspent Talisman Pouches" as fact. The user would have trusted them until they manually verified. Then they would have lost trust in the entire audit.

What makes this particularly painful is that validation WORKED. Two models independently saw the inconsistency. I could have ignored it; I did not. But a user running this without that adversarial layer would have gotten the wrong answer, confidently stated.

## Technical Details

**Game8 inversion example:**
- Gold summon: gives Ansbach's Longbow, ends Leda's quest line
- Red summon: gives something else, progression differs
- Game8 summary inverted the correspondence (without visible signal that it was a summary error)

**MediaWiki API that settled it:**
```
https://eldenring.wiki.gg/api.php?action=parse&page=Hornsent&prop=wikitext&format=json
```
Raw wikitext has explicit branch tracking with no room for inversion. One call, problem gone.

**Three probe failures with the same pattern:**

1. **Bell bearings (2/63 "missing"):** Bell Bearing [1], [2], [3]... are all in the player's inventory. The system tracks "how many times did you hand this to the Merchant"—that is consumption, not crafting. Code read the consumption count, not the collection count. Consumed bell bearings are no longer spendable but they are spent, not missing.

2. **Map fragments (4 "unacquired"):** MapPiece_* entries have a flag set_event_flag that gets edited when the map is unlocked. Instead of checking if the item was collected from the world, code checked if that flag existed. Two maps had their flags set via save-editor without the item ever being in inventory. Measurement returned "4 unacquired" when the right question is "did you pick up the physical object." Event flags answered the wrong question.

3. **Talisman Pouch (3 "unspent") and Memory Stone (8 "unspent"):** Both are Key Items with finite counts. Talisman Pouch max_held=3, Memory Stone max_held=8. When you hold all 3 pouches, inventory constraint is hit. Code interpreted "at max inventory" as "all upgrades obtained" which is correct for upgrade items like Great Runes, but dead wrong for these—they are not spendings, they are bound collectibles.

All three numbers looked reasonable. All three would have been wrong in a user-facing statement.

## What We Tried

1. WebFetch → summarize guide sites → trust the summary → failed
2. Codex model A → agrees with summary → correct by coincidence, not by verification
3. Codex model B (adversarial) → rejects recommendation → forces re-check
4. Raw MediaWiki API → wikitext, no summarisation layer → reveals the truth

## Root Cause Analysis

**Immediate cause:** Game8 inverted the branch outcomes in their summary. The fetch didn't reveal that inversion because I never read the raw page.

**Systemic cause:** I treated a model-summarized fetch as a first-class source equivalent to reading the raw data. It is not. Summarization is an interpretation layer. If the summarizer has an error, that error is invisible to downstream code—it looks like the source said X when the source said not-X.

**Why the probes failed:** Plausible numbers are the most dangerous kind of wrong. A probe that returns `null` or an error is obvious. A probe that returns 2, 4, 3, 8—integers that fit the expected range and pass sanity checks—looks correct until you verify it against a control case. I was trusting the measurement because the output looked reasonable, not because I had verified the measurement against reality.

The three probe failures happened because I did not have a control line for each category:
- Bell bearings: no control on "how many should be consumed if you've never handed any to an NPC"
- Map fragments: no control on "what does a map fragment look like when it's been unlocked but not collected"
- Talisman Pouch / Memory Stone: no control on "if I start the game with 1 Pouch and 0 Stones, what should the counts be"

## Lessons Learned

1. **Never treat a model-summarized fetch as equivalent to raw source.** A summary is an interpretation. Fetch raw source (wikitext, JSON dump, API struct) and parse it yourself. Remove the interpretation layer.

2. **A plausible number is the most dangerous kind of wrong.** A probe returning null or an error is safe—it fails loudly. A probe returning a number that fits the expected range and passes sanity checks is hiding a measurement error. The fix is a control line: something you know the answer to (a cookbook you bought at game start, a map you unlocked on day 1, a stat you hardcoded) that proves the measurement works.

3. **Adversarial validation works.** Two independent models running on the same question caught the branch recommendation error when one model alone would not have. That was not a fluke—it was the system working. The user should run multi-model validation before trusting any summary-based recommendation.

4. **Event flags are not source of truth for collection.** A flag can be edited independently of the corresponding item. Item inventory is the source of truth for "did you collect this." Flags are ephemeral state, not history.

## Next Steps

1. **Questline recommendation:** Provide corrected answer ("neither") and store raw wikitext fetch for that section so if the question comes up again, it's on-file. No more Game8 summaries for branch outcomes.

2. **Probe architecture:** Every measurement category needs at least one control line—an item or stat where the answer is known in advance, injected into a fresh save, measured, then verified against expectation. Store those control lines as test fixtures.
   - Bell bearings: start with 0 consumption, inject 1 bell bearing, verify consumption count = 0
   - Map fragments: verify that Map Piece [1] collected from starting zone gives the item AND sets the event flag
   - Talisman Pouch / Memory Stone: verify by counting from a fresh game, not by trusting max_held

3. **Fetch strategy:** For any wiki-based question, use MediaWiki API directly (action=parse, prop=wikitext) instead of WebFetch + summarization. Raw wikitext is reproducible and auditable.

4. **Validation flow:** Before shipping any confident recommendation, run Codex validation pass with disagreement mode enabled (two models, asked to find flaws). If either model flags a concern, fetch raw source before responding.

The hard part is that reasonable-looking wrong answers are invisible until you check. The fix costs nothing—just remember to ask "what would prove this measurement is correct?" and answer it with a control case you already know.
