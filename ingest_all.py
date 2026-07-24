import json
from pathlib import Path
from collections import defaultdict

def ingest_source(filepath):
    good = []
    bad = defaultdict(list)
    
    with open(filepath) as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                bad["empty_line"].append(line_num)
                continue
            
            try:
                row = json.loads(line)
                good.append(row)
            except json.JSONDecodeError:
                bad["invalid_json"].append(line_num)
    
    return good, dict(bad)

# Test on all 5
sources = ["auth", "dns", "endpoint", "firewall", "web"]
base = "/home/onake/hunt-engine/evidence/source"

for source in sources:
    path = Path(f"{base}/{source}.jsonl")
    good, bad = ingest_source(path)
    total_bad = sum(len(v) for v in bad.values())
    print(f"{source:12} - Good: {len(good):6} | Bad: {total_bad:4}")
