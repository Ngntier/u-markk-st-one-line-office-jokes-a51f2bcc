import os
line = "Our office printer only jams on documents marked urgent — it's the one coworker who actually reads the subject line."
assert 1 <= len(line) <= 199 and len(line.encode("utf-8")) <= 199 and "\n" not in line and line.strip()
out = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")
os.makedirs(os.path.dirname(out), exist_ok=True)
with open(out, "w", encoding="utf-8") as f:
    f.write(line)
