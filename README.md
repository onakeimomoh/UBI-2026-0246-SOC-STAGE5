# SOC Hunt Engine - Stage 5 Submission

## System & Tools
- OS: Kali Linux (Ubuntu-based)
- Python: 3.13.9
- DuckDB: latest
- Pytest: 25.1.1

## Assignment Details
- Variant: SOC-A1
- Evidence Marker: UBI-A5-F56238CD2EC8
- Intern: UBI-2026-0246

## Raw Evidence (Read-Only)
- `evidence/` folder contains immutable source artifacts:
  - `evidence/source/auth.jsonl` (150,019 rows)
  - `evidence/source/dns.jsonl` (149,911 rows)
  - `evidence/source/web.jsonl` (149,883 rows)
  - `evidence/source/firewall.jsonl` (150,046 rows)
  - `evidence/source/endpoint.jsonl` (150,141 rows)

## Derived Outputs (Separate Directory)
- `normalized-timeline.csv` (749,985 normalized events)
- `campaign-graph.json` (3 identified campaigns)
- `classification-results.json` (96 cases: 80 benign, 16 escalate)
- `tp-fp-table.csv` (true positive/false positive classifications)
- `data-quality-register.csv` (ingestion metrics)

## Clean-Build Commands (Exact Reproduction)

```bash
# 1. Extract evidence archive
cd ~/hunt-engine
tar -xzf soc-analysis-stage-5-shared-b1.tar.gz

# 2. Activate Python environment
source ~/hunt-engine-env/bin/activate

# 3. Run ingestion & normalization
python3 ingest_all.py
python3 test_normalize.py

# 4. Generate outputs
python3 export_timeline.py
python3 export_campaigns.py
python3 export_quality.py
python3 export_tp_fp.py

# 5. Run campaign correlation
python3 campaign_correlation.py
python3 classify_cases.py

# 6. Run tests
python3 -m pytest tests/ -v

# 7. Generate hashes
find . -type f ! -name manifest.sha256 -print0 | sort -z | xargs -0 sha256sum > manifest.sha256
```

## Results Summary
- 750,000 rows ingested
- 749,985 normalized (15 bad, quarantined)
- 3 campaigns identified (user232, user314, user178)
- 96 cases classified (80 benign, 16 escalate)
- Total runtime: ~145 seconds
- Peak memory: 512 MB

## Files
- `ingest.py` - Bad JSON detection
- `normalize.py` - Schema normalization per source
- `deduplicate.py` - Duplicate removal
- `campaign_correlation.py` - Multi-source campaign finding
- `classify_cases.py` - Case classification
- `tests/` - Automated test suite
- `queries/` - Hunt SQL queries
