# Dent review: ch09

- **Verdict:** REVISE

## Turn map

- **Scene 1:** the Turn lands at "He had read the syllabus. He knew that Lesson One…", closing on "Mine was a name to him now." It is an admission, not a summary, and it is the last line of the scene.
- **Scene 2:** the Turn lands at "He was going to come for me himself. Not with the police's permission…", with "We were the same kind of alone." The scene then runs one more paragraph and ends on "I put it down to the tea." That warmth is in the beat sheet, so it is acceptable. The Turn is still not the final line of the scene.
- **Scene 3:** the Turn lands at "*Excellent.*", on its own line. About 150 words follow before the Snapper (capping the pen, the quarter-inch, the tiredness). The scene ends on the Snapper, which is the correct close for the chapter.

## Findings

1. **Over length.** By my paragraph-by-paragraph estimate (no word counter was available), the chapter is about 3,500–3,600 words against a target of about 3,150. Scene 1 is about 1,350 words against about 1,050. Scene 2 is about 1,250. Scene 3 is about 1,000. The rule broken is style/10 point 1: "Chapter 17 may run long; nothing else may." strategy/03 asks for 1,000–1,100 per scene. Fix: run `python3 scripts/lint.py` to get the exact count, then cut Scene 1 by about 300 words and Scene 2 by about 150. Candidate cuts:
   - The knife-block, butter, milk and kettle inventory ("The butter in its paper, the paper folded back…") can be halved.
   - The back-compartment sentences, "A man who had found that panel would have put it back exactly as it was. So would a man who hadn't." The point is already made.
   - The second pass at the tell ("I said I would tell you which was the tell…").
   - "I can do my flat, at a careful walk, in two hours and eight minutes…" in Scene 2. It reads as an inserted aside.

2. **The first sentence is not load-bearing.** The opening ("The deadbolt turned with the weight it always turns with…") is a single sentence of about 130 words. The hook is buried in its middle and end ("the flat smelled of itself"). This breaks style/10 point 8, which says first and last sentences are load-bearing. Fix: split it. Let the first sentence stop at the deadbolt's give or at "the flat smelled of itself". Move the grocery bag, the morgue and the chest-height smell into the sentences after it. The trouble is still on page one, so point 2 is met.

3. **Scene 1 is overloaded before the Turn.** Between the entry and "He had read the syllabus", the scene runs the fridge check, the lock check, the compartment, the knot, the hovering hand, the "tell" explanation, whose file was on top, the reconstruction, the grade and the hunger. These are eleven separate beats. The Turn is strong, but the reader waits about 1,300 words for it. This is the Dent quarter-turn rule in strategy/03: Scene 1 "grabs". Fix: keep the smell, the kitchen-first tell and the quarter-inch. Merge "whose file was moved" and "worked his visit backwards" into one paragraph. Cut the rest as in finding 1.

4. **Scene 2 pressure is reported rather than staged, and the Turn is argued rather than evented.** All three "walls" are Iris's inference from silence: a slip pocketed, "No, sir.", a thumb that stops. Nothing on the feed shows Brandt choosing to come himself. "He was going to come for me himself" is her extrapolation, closed with "Full marks." and "Correct again." The Turn is a conclusion she reasons to, not something that happens. This is within the outline, since the outline says "I narrate his reasoning", but it is the thinnest of the three Turns. Fix: give wall three one physical event. For example, Brandt takes the folded sheriff's slip out again and tears it in half. Or his hand goes to the left inside pocket and stays there. Let her read that, then state the Turn.

5. **Iris's competence is all inference; she takes no protective action.** Strategy/03 says "Iris gets out of everything by her own competence". She is in no physical danger this chapter, so nothing is rescued, and I found no luck or convenient door. The lock was already picked, and the feed is her own set-up from Ch 8. But her safety rests entirely on Brandt's restraint. After finding the flat entered, she changes nothing: no lock, no relocation of the pages, no fallback. She sleeps in the flat. Fix: one line in Scene 3 showing that she chose this. For example: "I thought about the lock and the sleeve, and about moving both, and I left both where they were." It turns passivity into a decision and keeps the Snapper an answer to him.

6. **Minor: the Snapper is echoed twice.** In the last paragraph of Scene 3, "A quarter of an inch to the left" already states the act. The Snapper then restates it ("a quarter-inch to the left, where he had put it"). The Snapper is correct and should stay, so trim the earlier statement. Fix: cut "A quarter of an inch to the left." so that "where he had put it" is the first time the reader hears the offset restored as her choice.

## What works

- The closing sequence: "*Excellent.*" alone on its line, then the quiet Snapper ("…and slept nine hours."). It is an admission, not a cliffhanger, and the chapter ends on it.
- The kitchen-before-files tell and "Not today." give Scene 1 its menace and its reveal of her appetite and fear in the same move.
- "Mine was a name to him now." is the one-line Turn ending of Scene 1. Keep it as the last line of the scene.
