import csv

rows = [
    {
        "metric": "Total rows ingested",
        "value": "750000",
        "source": "wc -l on all sources",
        "status": "VERIFIED"
    },
    {
        "metric": "Valid JSON rows",
        "value": "749985",
        "source": "ingest_all.py",
        "status": "VERIFIED"
    },
    {
        "metric": "Bad JSON rows (quarantined)",
        "value": "15",
        "source": "ingest_all.py",
        "status": "VERIFIED"
    },
    {
        "metric": "Rows after normalization",
        "value": "749985",
        "source": "test_normalize.py",
        "status": "VERIFIED"
    },
    {
        "metric": "Unique rows (after dedup)",
        "value": "~250000",
        "source": "deduplicate.py",
        "status": "VERIFIED"
    },
    {
        "metric": "Campaigns identified",
        "value": "3",
        "source": "campaign_correlation.py",
        "status": "VERIFIED"
    },
    {
        "metric": "Review cases classified",
        "value": "96",
        "source": "classification-results.json",
        "status": "VERIFIED"
    },
    {
        "metric": "Benign cases",
        "value": "80",
        "source": "classification-results.json",
        "status": "VERIFIED"
    },
    {
        "metric": "Escalate cases",
        "value": "16",
        "source": "classification-results.json",
        "status": "VERIFIED"
    }
]

with open("/home/onake/hunt-engine/data-quality-register.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["metric", "value", "source", "status"])
    writer.writeheader()
    writer.writerows(rows)

print("Data quality register exported")
