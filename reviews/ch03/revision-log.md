# Revision log — ch03

## Stitch pass 2 (author.md, line-level)

Scope: only the item listed under "Stitch pass 2" in `reviews/ch03/author.md`. The five reviewer reports (continuity, dent, forensic, genre, voice) were handled in an earlier wave and were not re-applied.

1. **Scene 1 repeats Chapter 2's "the donor beaming as if he had been promoted"** — FIXED. Checked against `manuscript/ch02.md` (para. at line 49, "the donor beamed as if he had been promoted"). Kept the fact (first ring, mid-sentence) and cut the image, with no new simile in its place.
   - Before: "...the phone going in the middle of a donor's sentence and Diane answering on the first ring, and the donor beaming as if he had been promoted. I wrote it across the weekday block..."
   - After: "...the phone going in the middle of a donor's sentence and Diane answering on the first ring. I wrote it across the weekday block..."

Lint: `python3 scripts/lint.py manuscript/ch03.md` passes (ok, 0 failing). Word count 3,480 (lint), down from 3,490.
