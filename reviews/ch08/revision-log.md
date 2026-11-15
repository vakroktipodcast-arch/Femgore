# Revision log — ch08 (targeted pass: author ruling on stitch review, headline 9)

Scope: `reviews/ch08/author.md` only. The five reviewer reports (continuity, dent, forensic, genre, voice) were handled in an earlier revision wave and were not re-applied in this pass.

## Author rulings

1. **Scene 2: remove "I have never owned a record."** FIXED. I cut the one sentence and changed nothing else in the paragraph. That line is kept for the Chapter 17 anchor (`anchors/ch17.md`). The fact still holds (ledger; `bible/style/09`): nothing in ch08 says or implies that she owns a record. Kept as instructed: the Black Saint played through the clean laptop's speakers, and "It was like having a menu read to you when you're hungry."
   - Before: "*The Black Saint and the Sinner Lady* was on his list. I have never owned a record. I found it and played it through the clean laptop's speakers, ..."
   - After: "*The Black Saint and the Sinner Lady* was on his list. I found it and played it through the clean laptop's speakers, ..."
   - Rhythm: the short sentence about his list now leads straight into the long sentence that plays the album. "It" still clearly means the album.

## Reviewer reports (continuity, dent, forensic, genre, voice)

Not re-applied. They were dealt with in the earlier revision wave, and this pass changes only what the author note requires.

## Follow-up for the author

- `beats/ch08.md` (beat 5 and the Motifs line) still says "she has never owned a record" as beat-sheet description. That is true as a fact, and the beat sheet is outside this pass's one-file scope, so I left it alone. Update it if you want the beat sheet to match the prose.

## Lint

`python3 scripts/lint.py manuscript/ch08.md`: ok, 3399 words, 0 failing.

# Stitch pass 2 (line-level; `reviews/ch08/author.md`, "Stitch pass 2")

Scope: only the item listed under "Stitch pass 2". I did not re-apply the five reviewer reports or the earlier author item.

1. **Scene 3: cut the crackling simile.** FIXED. Chapter 7 ends on "I was saving it the way you save the last bite.", so this was the same joke one chapter later. I cut the simile and kept the fact that she had saved it.
   - Before: "... and the laptop had stayed shut on the desk. I had saved it the way you save the crackling."
   - After: "... and the laptop had stayed shut on the desk. I had saved it."
   - Rhythm: the long sentence that lists everything she did now ends on a short four-word close. That matches the short sentences that open the paragraph ("The recording was from Sunday night. I hadn't watched it."). The next paragraph, "So it was late on Monday...", still follows on naturally.

## Lint (stitch pass 2)

`python3 scripts/lint.py manuscript/ch08.md`: ok, 3393 words, 0 failing.

# Stitch pass 3 (`reviews/ch08/author.md`, "Stitch pass 3")

Scope: only the three items listed under "Stitch pass 3". I did not re-apply the five reviewer reports or the earlier author items. Everything from "He came in at 11:52" to the end is unchanged. The scene Turn (her thumb stopped on the trackpad) and the Snapper are unchanged.

1. **Scene 3: compress the camera explanation.** FIXED. Chapters 2 and 4 already place the units, and the ledger keeps the full fact (Objects: two button units, bezel facing the table, credenza by the urn). This scene keeps only what it needs: the bezel faces the table, so she sees faces and never the screen. The later switch to "the unit under the credenza lip by the urn" (after 11:52, untouched) still reads clearly against Chapters 2 and 4.
   - Before: "There are two units in that room, bought for cash and fixed with the same black vinyl. The one I like best sits in the bezel of the wall screen, wide on the glass-walled suite on the thirty-first floor and facing the table. Whenever anybody looks at the screen, they look into my lens. The cost of that is that the screen itself is behind me. I can never see what is on it. I can only watch faces turn to it."
   - After: "The bezel unit faces the table. Whenever anybody looks at the screen, they look into my lens, and the screen itself is behind me. I see the faces turn to it. I never see what is on it."
2. **Scene 3: trim the who-said-what before Brandt enters to one line.** FIXED. Interlude 2 gives this room from inside right afterwards (comms by six, counsel, *activist*/*lunatic*), so here the reportage is one sentence. I kept it in so that two ledger facts survive: counsel says "nobody say anything" four times in twelve minutes (11:40–11:52), and *activist*/*lunatic* are said before 11:52 (the Interlude 2 note). Iris's reading of the room as a body, the photograph read off the faces, the phones photographing her page and the femoral-leak line are unchanged. "Somebody said his name into a phone. After that the room held itself..." stays, as part of her body reading.
   - Before (11:40 paragraph): "... voices over the hum of the air system. Comms asked for a statement by six, which is a deadline and not a position. Counsel said that nobody should say anything, and then said it again, and by the end of the twelve minutes had said it four times, which is three more times than counsel says anything without billing for it."
   - After: "... voices over the hum of the air system. In twelve minutes comms asked for a statement by six, counsel said four times that nobody should say anything, and somebody offered *activist* and somebody *lunatic*, without the anatomy to back either."
   - Before (paragraph before 11:52): "Somebody said his name into a phone. After that the room held itself the way a room does when the person who decides is on his way. One of them offered *activist*. Another offered *lunatic*. Neither had the anatomy to back it up."
   - After: "Somebody said his name into a phone. After that the room held itself the way a room does when the person who decides is on his way."
3. **Word count within 2,800–3,500.** DONE: 3,393 down to 3,312.

## Lint (stitch pass 3)

`python3 scripts/lint.py manuscript/ch08.md`: ok, 3312 words, 0 failing.
