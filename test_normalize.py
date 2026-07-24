import json
from normalize import normalize_row
from pathlib import Path

base = "/home/onake/hunt-engine/evidence/source"
sources = ["auth", "dns", "endpoint", "firewall", "web"]

for source in sources:
    normalized_count = 0
    failed_count = 0
    
    with open(f"{base}/{source}.jsonl") as f:
        for i, line in enumerate(f):
            if i >= 100:
                break
            try:
                row = json.loads(line)
                norm = normalize_row(source, row)
                if norm:
                    normalized_count += 1
            except:
                failed_count += 1
    
    print(f"{source:12} - Normalized: {normalized_count}/100 | Failed: {failed_count}")
