import json

with open("/home/onake/hunt-engine/ubi-2026-0246-stage-5-discrepancy.json") as f:
    data = json.load(f)

changes = data.get("changes", [])

print(f"Classifying {len(changes)} changes:\n")

benign = 0
escalate = 0

for change in changes:
    change_id = change.get("changeId")
    status = change.get("status")
    purpose = change.get("purpose")
    
    # Rule: If APPROVED + has legitimate purpose = BENIGN
    if status == "APPROVED" and purpose and "Scheduled" in purpose:
        verdict = "BENIGN"
        benign += 1
        reason = "Approved scheduled activity"
    else:
        verdict = "ESCALATE"
        escalate += 1
        reason = "Status not approved or purpose unclear"
    
    print(f"{change_id}: {verdict} ({reason})")

print(f"\nSummary: {benign} benign, {escalate} escalate")
