import json
from collections import defaultdict
from normalize import normalize_row

def load_all_normalized(base_path):
    """Load and normalize all sources."""
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

def find_campaigns(all_rows):
    """Find users with activity across multiple sources (likely attacker)."""
    user_activities = defaultdict(lambda: {
        "sources": set(),
        "hosts": set(),
        "events": []
    })
    
    for row in all_rows:
        user = row.get("user", "unknown")
        source = row.get("source_type", "unknown")
        host = row.get("host", "unknown")
        
        user_activities[user]["sources"].add(source)
        user_activities[user]["hosts"].add(host)
        user_activities[user]["events"].append(row)
    
    # Find suspicious users (activity across 3+ sources)
    campaigns = []
    for user, data in user_activities.items():
        if len(data["sources"]) >= 3:  # Multi-source = suspicious
            campaigns.append({
                "user": user,
                "sources": sorted(list(data["sources"])),
                "hosts": sorted(list(data["hosts"])),
                "event_count": len(data["events"]),
                "events": data["events"][:10]  # First 10 events
            })
    
    # Sort by event count (most active first)
    campaigns.sort(key=lambda x: x["event_count"], reverse=True)
    return campaigns[:3]  # Top 3 campaigns

# Load and correlate
base = "/home/onake/hunt-engine/evidence/source"
all_rows = load_all_normalized(base)
campaigns = find_campaigns(all_rows)

print(f"Found {len(campaigns)} campaigns:\n")
for i, campaign in enumerate(campaigns, 1):
    print(f"Campaign {i}:")
    print(f"  User: {campaign['user']}")
    print(f"  Sources touched: {campaign['sources']}")
    print(f"  Hosts: {campaign['hosts']}")
    print(f"  Total events: {campaign['event_count']}")
    print()
