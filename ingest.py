import json
from pathlib import Path
from collections import defaultdict

def ingest_source(filepath):
    """Read one JSONL file. Count good, bad, and reasons."""
    good = []
    bad = defaultdict(list)  # reason -> list of rows
    
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

# Test on auth
auth_path = Path("/home/onake/hunt-engine/evidence/source/auth.jsonl")
good, bad = ingest_source(auth_path)

print(f"Auth results:")
print(f"  Good rows: {len(good)}")
print(f"  Bad rows: {sum(len(v) for v in bad.values())}")
for reason, lines in bad.items():
    print(f"    - {reason}: {len(lines)} rows")

if good:
    print(f"\nSample good row:")
    print(json.dumps(good[0], indent=2))
