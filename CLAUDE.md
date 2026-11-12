# The Butcher's Syllabus — house rules

A femgore novel by Imogen Sallow. 85,000 words: 27 chapters (~3,150 words, three scenes each) narrated by Iris Vale in first person past tense, plus 5 close-third interludes (600–900 words).

## Where things live
- `bible/` — the drafting bible. Read-only. Never edit without the author's explicit instruction.
- `outline/` — one brief per chapter/interlude, with a Turn per scene and a Snapper. Read-only.
- `anchors/` — author-approved prose. The voice standard. Read-only once approved.
- `ledger/continuity.md` — every fixed fact. If a fact is not in the ledger, it is not yet true.
- `beats/` — beat sheets, one per unit.
- `manuscript/` — prose, one file per unit, named as in `outline/00-reading-order.md`.
- `reviews/<unit>/` — reviewer reports. Reports only, never prose.

## Rules
1. One agent, one file. An agent writes only the file it was assigned.
2. Drafters and revisers must read, before writing: `bible/style/` (all), `bible/strategy/10-*.md`, `bible/cast.md`, every file in `anchors/`, the unit's outline and beat sheet, `ledger/continuity.md`, and the beat sheets of the units immediately before and after.
3. Never invent a fact that contradicts the ledger. New facts go in a `## New facts` list at the end of the beat sheet, not silently into prose.
4. Every scene ends on its Turn; every chapter ends on its Snapper. The outline's Turn and Snapper are the minimum.
5. Reviewers never edit `manuscript/`. Drafters never grade their own chapter.
6. Manuscript files contain prose only: a `# Chapter N` heading, scene breaks as `* * *`, nothing else. No notes, no summaries, no commentary.
7. Run `python3 scripts/lint.py` before saying a chapter is done.
8. Work only on the session's own branch. Commit and push your work there when a phase prompt is complete. Never push to `main`; the author creates and merges the pull request.

## The test
Does this make the reader more or less able to look away from Iris?
