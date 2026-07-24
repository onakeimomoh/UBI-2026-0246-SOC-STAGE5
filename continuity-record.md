# Continuity Record - SOC Stage 5 to Stage 6

## Prior Stage Component Reused
- Normalization schema (from Stage 4 governance brief)
- Campaign correlation logic (from Stage 3 forensics)
- Risk register framework (ISO 27001:2022)

## Interface Preserved
**Input:** 5 JSONL sources (auth, dns, web, firewall, endpoint)

**Output:** 
- normalized-timeline.csv (749,985 events)
- campaign-graph.json (3 campaigns)
- classification-results.json (96 cases: 80 benign, 16 escalate)

**Schema:** timestamp, source_type, user, host, action, status

## Migrations
- Clock correction: inferred from timestamp frequency
- Deduplication key: (timestamp, user, host, action)
- Campaign detection: user activity across 3+ sources

## Preserved Provenance
- All source artifacts read-only in evidence/ folder
- Normalized outputs in separate files
- SHA-256 hashes computed before submission
- Test scripts verify data integrity

## Next-Stage Handoff
Stage 6 (Threat Hunting) will receive:

1. **Normalized Event Timeline** (749,985 events)
   - All sources standardized to common schema
   - Ready for SIEM import or further analysis

2. **Campaign Correlation Rules** 
   - user232, user314, user178
   - Multi-source detection pattern

3. **Classification Methodology**
   - 80 benign cases with approval evidence
   - 16 escalate cases with mismatches
   - Reproducible rules (not manual)

4. **Reusable Normalizers**
   - normalize.py functions per source
   - Drop-in for new data sources
