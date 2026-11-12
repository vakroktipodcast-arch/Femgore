#!/usr/bin/env python3
"""Mechanical checks for manuscript files. Errors fail the run; warnings do not.
Usage: python3 scripts/lint.py [files...]   (default: every file in manuscript/)"""
import re, sys, glob, os

BANNED = [  # (regex, message)
    (r"\bice in (her|my) veins\b", "banned phrase: ice in her veins"),
    (r"\b(trained|professional) killer\b", "banned phrase: trained/professional killer"),
    (r"\bcalculating eyes\b", "banned phrase: calculating eyes"),
    (r"\bfemme fatale\b", "banned phrase: femme fatale"),
    (r"\bperfect (cut|kill|strike|incision|blow)\b", "banned: 'perfect' as a violence descriptor"),
    (r"\b(smirked|chuckled|growled|hissed|snarled)\b", "banned dialogue tag"),
    (r"[,’”\"'] (she|he|I) breathed\b", "banned: 'breathed' as a dialogue tag"),
    (r"\b(lucky|luckily|fortunately)\b", "banned: luck (Dent's hero rule)"),
    (r"\bI shouldn[’']t have enjoyed\b|\bI[’']m not proud\b", "banned: Iris never apologises for appetite"),
]
WARN = [
    (r"\bdanc(e|ed|ing)\b", "check: 'dance' must not describe combat"),
    (r"\b(demon|monster|beast)\b", "check: not for Iris, the targets, or the violence"),
    (r"\b(empty|hollow|numb)\b", "check: do not name her state; show it through the body"),
]

def words(text): return len(re.findall(r"[A-Za-z0-9’'\-]+", text))

def check(path):
    errs, warns = [], []
    name = os.path.basename(path)
    text = open(path, encoding="utf-8").read()
    lines = text.splitlines()
    body = "\n".join(l for l in lines if not l.startswith("#") and l.strip() != "* * *")
    n = words(body)
    breaks = sum(1 for l in lines if l.strip() == "* * *")
    m = re.match(r"ch(\d\d)\.md$", name)
    if m:
        ch = int(m.group(1))
        lo, hi = (3000, 6000) if ch == 17 else (2800, 3500)
        if not lines or not re.match(r"# Chapter \d+", lines[0]): errs.append("first line must be '# Chapter N'")
        if breaks != 2: errs.append(f"expected 3 scenes (2 '* * *' breaks), found {breaks + 1}")
        if not lo <= n <= hi: errs.append(f"word count {n} outside {lo}-{hi}")
        count = len(re.findall(r"\bbeautiful\b", body, re.I))
        if ch == 17 and count != 1: errs.append(f"'beautiful' must appear exactly once in Chapter 17 (found {count})")
        if ch != 17 and count: errs.append(f"'beautiful' is banned outside Chapter 17 (found {count})")
        if ch != 24 and re.search(r"—[’”\"']", body): errs.append("em-dash interruption in dialogue (allowed only in Chapter 24)")
        if len(re.findall(r"\bI\b", body)) < 20: warns.append("very few 'I' — is this first person?")
    elif name.startswith("interlude-"):
        if not lines or not lines[0].startswith("# Interlude"): errs.append("first line must be '# Interlude — Name'")
        if breaks: errs.append("interludes are a single scene (no '* * *')")
        if not 600 <= n <= 900: errs.append(f"word count {n} outside 600-900")
        if re.search(r"\bbeautiful\b", body, re.I): errs.append("'beautiful' is banned outside Chapter 17")
    else:
        return None
    for rx, msg in BANNED:
        for hit in re.finditer(rx, body, re.I): errs.append(f"{msg}: “…{body[max(0,hit.start()-30):hit.end()+20].strip()}…”".replace("\n", " "))
    for rx, msg in WARN:
        k = len(re.findall(rx, body, re.I))
        if k: warns.append(f"{msg} ({k}x)")
    return n, errs, warns

def main():
    files = sys.argv[1:] or sorted(glob.glob("manuscript/*.md"))
    failed = 0; total = 0
    for f in files:
        r = check(f)
        if r is None: continue
        n, errs, warns = r; total += n
        status = "FAIL" if errs else "ok"
        print(f"{status:4} {f}  ({n} words)")
        for e in errs: print(f"     ERROR  {e}")
        for w in warns: print(f"     warn   {w}")
        failed += bool(errs)
    print(f"\n{total} words across {len(files)} file(s); {failed} failing")
    sys.exit(1 if failed else 0)

if __name__ == "__main__": main()
