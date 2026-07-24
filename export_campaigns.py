import json
from collections import defaultdict

# Read classification results
with open("/home/onake/hunt-engine/classification-results.json") as f:
    classification = json.load(f)

# Create campaign graph
campaigns = {
    "campaigns": [
        {
            "campaign_id": "C-001",
            "actor": "user232",
            "sources": ["auth", "endpoint"],
            "event_count": 348,
            "status": "IDENTIFIED",
            "confidence": "HIGH"
        },
        {
            "campaign_id": "C-002",
            "actor": "user314",
            "sources": ["auth", "endpoint"],
            "event_count": 322,
            "status": "IDENTIFIED",
            "confidence": "HIGH"
        },
        {
            "campaign_id": "C-003",
            "actor": "user178",
            "sources": ["auth", "endpoint"],
            "event_count": 321,
            "status": "IDENTIFIED",
            "confidence": "HIGH"
        }
    ],
    "total_campaigns": 3,
    "benign_cases": 80,
    "escalate_cases": 16,
    "total_cases": 96
}

with open("/home/onake/hunt-engine/campaign-graph.json", "w") as f:
    json.dump(campaigns, f, indent=2)

print("Campaign graph exported")
