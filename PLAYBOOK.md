# Playbook — writing this book from a phone or tablet

No terminal, no commands. Claude Code runs in the cloud against the GitHub repo; you work from the Code tab of the Claude app or claude.ai/code in Chrome, and from the GitHub app.

**The rhythm of every phase is the same:**
1. Start a new session on the repo and paste the phase's prompt.
2. Claude works on its own branch. Steer it in the chat if needed.
3. Open the diff, choose **Create PR**.
4. Read the pull request on GitHub. Comment on any line. Merge when satisfied.
5. Start the next phase in a fresh session, so it begins from the merged `main`.

Every agent owns exactly one file, so agents running in parallel cannot collide.

## 0. One-time setup (about ten minutes, in Chrome)

1. On github.com, create a **private** repository named `butchers-syllabus`, with a README.
2. In the repo: **Add file → Upload files**, choose `butchers-syllabus-repo.zip`, commit to `main`.
3. Open claude.ai/code and connect GitHub. Install the Claude GitHub App on the new repository — a private repo will not appear in the list without it.
4. Start a session on the repo in **Accept edits** mode, choose your strongest model, and send:

**Kickoff prompt**
> This repository contains butchers-syllabus-repo.zip, a project kit for a novel. Unzip it into the repository root (its files go at the top level, not in a subfolder), then delete the zip. Make sure the hidden .claude/ and .github/ folders came through.
>
> Then read CLAUDE.md, PLAYBOOK.md, and outline/00-reading-order.md. Confirm that outline/ has 27 chapter briefs and 5 interlude briefs, that .claude/agents/ has ten agents, that bible/ has 25 files, and that `python3 scripts/lint.py` and `bash scripts/status.sh` both run.
>
> Commit and push with the message "Add project kit". If the push is rejected because of .github/workflows/lint.yml, leave that one file out, push the rest, and tell me.
>
> Then tell me in ten lines or fewer what the pipeline is and the rules you will hold every agent to. Do not write any prose or beat sheets in this session.

5. Check its summary against what you know of the book. Then **Create PR** and merge it on GitHub.

If the workflow file was left out: on github.com use **Add file → Create new file**, name it `.github/workflows/lint.yml`, and paste the contents Claude shows you. The linter still runs inside every session without it; the workflow only adds a check mark on pull requests.

## Phase 1 — Voice lock (one session; you approve every line)

**Prompt 1a**
> Use the beat-sheet subagent to write beat sheets for ch17, ch01, ch25 and interlude-2-cam, in parallel, one subagent per unit. Show me a short summary of each.

Read the four beat sheets in the diff. Then, in the same session:

**Prompt 1b**
> Now you, in this main conversation, not a subagent: read CLAUDE.md, bible/style/ in full, bible/strategy/02 and 10, bible/cast.md, ledger/continuity.md, outline/ch17.md and beats/ch17.md. Draft Chapter 17 to anchors/ch17.md following the drafter agent's requirements. This is the voice anchor for the whole book; take your time.

Read it. Push back in the chat. Iterate until it is the voice. Then ask for `ch01`, `ch25` and `interlude-2-cam` the same way, one at a time, each reading the anchors already approved. When all four are right:

**Prompt 1c**
> All four anchors are approved. Copy them into manuscript/, run the linter, fix anything it reports in both copies, then commit and push.

Create PR, merge.

## Phase 2 — Beat sheets and ledger (one session; 28 agents, then 1)

**Prompt 2a**
> Use the beat-sheet subagent to write a beat sheet for every unit in outline/00-reading-order.md that has no file in beats/ yet. One subagent per unit, as many in parallel as you can run, in batches until all 28 are done. Then use the continuity subagent to merge the New facts from all beat sheets into ledger/proposed.md, with clashes and a timeline check. Show me the clashes and the Open items that need my decision.

Settle each clash in the chat. Then:

**Prompt 2b**
> Those are my decisions. Have the continuity subagent fold the approved facts into ledger/continuity.md and delete ledger/proposed.md. Update any beat sheet whose facts lost a clash. Run `bash scripts/status.sh`, then commit and push.

Create PR, merge.

## Phases 3 + 4 — Draft, review, revise: five waves, one session each

| Wave | Units | Drafters at once |
|---|---|---|
| H — hinges | ch06 ch12 ch18 ch24 ch27 | 5 |
| I — interludes | interlude-1-diane interlude-3-cam interlude-4-reyes interlude-5-reyes | 4 |
| A — Act I | ch02 ch03 ch04 ch05 ch07 ch08 ch09 | 7 |
| B — Act II | ch10 ch11 ch13 ch14 ch15 ch16 | 6 |
| C — Act III | ch19 ch20 ch21 ch22 ch23 ch26 | 6 |

Run H first and read every chapter of it yourself; the rest lean on these. Wave I can run in a second session at the same time as H. Then A, B, C in order, each merged before the next begins so drafters can read their neighbours.

For each wave, start a new session and send the three prompts in turn. Example for Wave H — swap in the unit list for the others:

**Prompt 3 — draft**
> Wave H. Use the drafter subagent to draft ch06, ch12, ch18, ch24 and ch27, one subagent per chapter, all in parallel. When they finish, run the linter and show me each drafter's report.

(For Wave I, say "interlude-drafter subagent".)

**Prompt 4a — review**
> For each chapter in this wave, run all five reviewer subagents — reviewer-dent, reviewer-voice, reviewer-continuity, reviewer-genre, reviewer-forensic — one subagent per lens per chapter, in parallel. Reviewers must not see each other's reports. When done, give me a table of verdicts and the three most serious findings per chapter.

Read the drafts and the findings. Tell Claude your own notes per chapter in the chat and ask it to save them as `reviews/<unit>/author.md` — your notes outrank the reviewers. If a chapter should be thrown away, say "redraft chNN from scratch" before the next prompt.

**Prompt 4b — revise**
> Use the reviser subagent on every chapter in this wave, one per chapter, in parallel. Then run the linter, and have the continuity subagent sweep these chapters for new facts and show me what it proposes adding to the ledger. After I approve, update the ledger, commit and push.

Create PR. Read it on GitHub and comment on any line. To apply your comments, go back to the session:

**Prompt 4c**
> I have left review comments on this branch's pull request. Read them, save them into reviews/<unit>/author.md for each affected unit, run the reviser subagent on those units, run the linter, commit and push.

Merge when satisfied. Next wave, new session.

## Phase 5 — Stitch (one session)

**Prompt 5a**
> Read the whole manuscript in the order given in outline/00-reading-order.md. Do not edit. Write reviews/stitch.md covering: seams between units (where she is, what she carries, time of day); repeated images, jokes or sentence shapes across chapters; a count of each motif in bible/style/09 by chapter; the appetite arc chapter by chapter against bible/strategy/10; the joke rate by act; and the ten weakest pages in the book. Give me the headline findings.

Decide what to act on and direct the fixes chapter by chapter in the chat. Then:

**Prompt 5b**
> Concatenate the manuscript in reading order into build/the-butchers-syllabus.md, with the syllabus inserts at the heads of Chapters 1, 6 and 17, and report the total word count. Run the linter one last time, commit and push.

Create PR, merge. On GitHub, **Releases → Draft a new release**, tag it `draft-1`.

## How much runs at once

| Phase | Agent tasks | Peak in parallel |
|---|---|---|
| 1 Voice lock | 4 beat sheets | 4 |
| 2 Beats + ledger | 28 + 1 | as many as the session will run |
| 3 Drafting | 28 | 7 |
| 4 Review + revise | 140 reviews + 28 revisions | 35 |
| 5 Stitch | 1 | 1 |

Parallel agents multiply usage, and cloud sessions share your plan's limits. A comfortable pace is one wave a day. If you hit limits, split a wave in two, or tell Claude to set `model: sonnet` in the five `reviewer-*.md` files and keep the stronger model for drafting and revising.

## If something goes wrong
- **"I can't find that subagent":** say "Read .claude/agents/<name>.md and run general-purpose subagents with exactly those instructions."
- **A chapter sounds wrong:** do not patch it. Say why, have the reason saved to `reviews/<unit>/author.md`, and redraft. If two chapters go wrong the same way, the anchors or the bible need a line added — fix the source, not the symptom.
- **A fact changes:** have Claude change `ledger/continuity.md` first, then find every unit that states the old fact.
- **The bible needs to change:** do it in its own session and pull request, so the history shows when the rules moved.
- **A session stalls or loses the thread:** push what it has, create the PR, merge, and continue in a fresh session. Everything it needs is in the repo, not in the chat.
