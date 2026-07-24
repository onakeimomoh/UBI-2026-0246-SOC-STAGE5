import json
from normalize import normalize_row

def deduplicate_source(source_type, filepath):
    """Read source, normalize, deduplicate."""
    seen = set()
    good = []
    duplicates = 0
    
    with open(filepath) as f:
        for line in f:
            try:
                row = json.loads(line)
                norm = normalize_row(source_type, row)
                if not norm:
                    continue
                
                # Create a hashable key
                key = (norm.get("timestamp"), norm.get("user"), norm.get("host"), norm.get("action"))
                
                if key in seen:
                    duplicates += 1
                else:
                    seen.add(key)
                    good.append(norm)
            except:
                pass
    
    return good, duplicates

# Test on all sources
base = "/home/onake/hunt-engine/evidence/source"
sources = ["auth", "dns", "endpoint", "firewall", "web"]

for source in sources:
    good, dups = deduplicate_source(source, f"{base}/{source}.jsonl")
    print(f"{source:12} - Unique: {len(good):6} | Duplicates: {dups:4}")
