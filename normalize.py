def normalize_auth(row):
    return {
        "timestamp": row.get("timestamp", ""),
        "source_type": "auth",
        "user": row.get("username", "unknown"),
        "host": row.get("host", "unknown"),
        "action": row.get("action", "unknown"),
        "status": row.get("reason", "unknown"),
    }

def normalize_dns(row):
    return {
        "timestamp": row.get("timestamp", ""),
        "source_type": "dns",
        "user": row.get("host", "unknown"),  # Use host as identifier
        "host": row.get("host", "unknown"),
        "action": row.get("query", "unknown"),
        "status": row.get("answer", "unknown"),
    }

def normalize_web(row):
    return {
        "timestamp": row.get("timestamp", ""),
        "source_type": "web",
        "user": row.get("actor", "unknown"),
        "host": row.get("host", "unknown"),
        "action": row.get("method", "unknown"),
        "status": row.get("status", "unknown"),
    }

def normalize_firewall(row):
    return {
        "timestamp": row.get("timestamp", ""),
        "source_type": "firewall",
        "user": row.get("src_ip", "unknown"),  # Use source IP as identifier
        "host": row.get("dst_ip", "unknown"),
        "action": row.get("action", "unknown"),
        "status": row.get("bytes_out", "unknown"),
    }

def normalize_endpoint(row):
    return {
        "timestamp": row.get("timestamp", ""),
        "source_type": "endpoint",
        "user": row.get("user", "unknown"),
        "host": row.get("host", "unknown"),
        "action": row.get("event", "unknown"),
        "status": row.get("destination", "unknown"),
    }

NORMALIZERS = {
    "auth": normalize_auth,
    "dns": normalize_dns,
    "web": normalize_web,
    "firewall": normalize_firewall,
    "endpoint": normalize_endpoint,
}

def normalize_row(source_type, row):
    if source_type not in NORMALIZERS:
        return None
    return NORMALIZERS[source_type](row)
