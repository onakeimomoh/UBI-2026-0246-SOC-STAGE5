import json
import csv

base = "/home/onake/hunt-engine/evidence/source"
sources = ["auth", "dns", "endpoint", "firewall", "web"]

# Import from normalize.py
from normalize import normalize_row

rows = []

for source in sources:
    with open(f"{base}/{source}.jsonl") as f:
        for line in f:
            try:
                raw = json.loads(line)
                norm = normalize_row(source, raw)
                if norm:
                    rows.append(norm)
            except:
                pass

# Sort by timestamp
rows.sort(key=lambda x: x.get("timestamp", ""))

# Export to CSV
with open("/home/onake/hunt-engine/normalized-timeline.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["timestamp", "source_type", "user", "host", "action", "status"])
    writer.writeheader()
    writer.writerows(rows)

print(f"Exported {len(rows)} normalized events to normalized-timeline.csv")
