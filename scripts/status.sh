#!/usr/bin/env bash
# Where is every unit? outline -> beats -> draft -> reviews -> revised
printf "%-22s %-6s %-7s %-8s %-8s\n" UNIT BEATS DRAFT REVIEWS REVISED
for f in outline/ch*.md outline/interlude-*.md; do
  u=$(basename "$f" .md)
  b=$([ -f "beats/$u.md" ] && echo yes || echo -)
  d=$([ -f "manuscript/$u.md" ] && wc -w < "manuscript/$u.md" | tr -d ' ' || echo -)
  r=$(ls reviews/$u/*.md 2>/dev/null | grep -v -e revision-log -e author | wc -l | tr -d ' ')
  v=$([ -f "reviews/$u/revision-log.md" ] && echo yes || echo -)
  printf "%-22s %-6s %-7s %-8s %-8s\n" "$u" "$b" "$d" "$r/5" "$v"
done
