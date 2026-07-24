
# Hunt Engine Progress

## Setup Complete 
- Downloaded shared SOC archive (soc-analysis-stage-5-shared-b1.tar.gz)
- Downloaded private discrepancy set (ubi-2026-0246-stage-5-discrepancy.json)
- Extracted archive to ~/hunt-engine/source/
- Found 5 log sources: auth.jsonl, dns.jsonl, endpoint.jsonl, firewall.jsonl, web.jsonl
- Evidence marker: UBI-A5-F56238CD2EC8

## Next: Understand the data structure

## Data Profile 
- auth.jsonl: 150,019 rows
- dns.jsonl: 149,911 rows
- endpoint.jsonl: 150,141 rows
- firewall.jsonl: 150,046 rows
- web.jsonl: 149,883 rows
- TOTAL: 750,000 rows

## Ingestion Results
- auth: 150,016 good | 3 bad (invalid JSON)
- dns: 149,908 good | 3 bad (invalid JSON)
- endpoint: 150,138 good | 3 bad (invalid JSON)
- firewall: 150,043 good | 3 bad (invalid JSON)
- web: 149,880 good | 3 bad (invalid JSON)

TOTAL: 749,985 good | 15 bad
All bad rows: invalid_json (malformed on purpose)

Next: Understand schema of good rows per source

## Normalization Test 
- auth: 97/100 normalized | 3 failed (bad JSON)
- dns: 97/100 normalized | 3 failed (bad JSON)
- endpoint: 97/100 normalized | 3 failed (bad JSON)
- firewall: 97/100 normalized | 3 failed (bad JSON)
- web: 97/100 normalized | 3 failed (bad JSON)

All failures are invalid_json (expected, quarantine-worthy)
Normalizer works correctly.

Next: Deduplication, clock correction, campaign correlation
