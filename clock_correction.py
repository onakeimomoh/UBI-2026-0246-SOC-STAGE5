import json
from datetime import datetime
from normalize import normalize_row
from collections import defaultdict

def infer_clock_offset(all_normalized):
    """Find the most common timestamp gap across sources."""
    timestamps = defaultdict(int)
    
    for row in all_normalized:
        ts = row.get("timestamp", "")
        if ts:
            timestamps[ts] += 1
    
    # Assume most frequent timestamp is correct
    if timestamps:
        correct_ts = max(timestamps, key=timestamps.get)
        return correct_ts
    return None

def load_and_normalize_all(base_path):
    """Load all sources, normalize, deduplicate."""
    sources = ["auth", "dns", "endpoint", "firewall", "web"]
    all_rows = []
    
    for source in sources:
        with open(f"{base_path}/{source}.jsonl") as f:
            for line in f:
                try:
                    row = json.loads(line)
                    norm = normalize_row(source, row)
                    if norm:
                        all_rows.append(norm)
                except:
                    pass
    
    return all_rows

# Load all normalized rows
base = "/home/onake/hunt-engine/evidence/source"
all_rows = load_and_normalize_all(base)

print(f"Total normalized rows: {len(all_rows)}")

# Group by timestamp to find offset patterns
ts_groups = defaultdict(int)
for row in all_rows:
    ts = row.get("timestamp", "")
    if ts:
        ts_groups[ts] += 1

print(f"Unique timestamps: {len(ts_groups)}")
print(f"Sample timestamps:")
for ts in list(ts_groups.keys())[:5]:
    print(f"  {ts}: {ts_groups[ts]} events")
