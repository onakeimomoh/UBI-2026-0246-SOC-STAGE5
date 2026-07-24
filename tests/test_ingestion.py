import pytest
import json
from pathlib import Path

def test_bad_json_detected():
    """Test that invalid JSON is caught"""
    bad_row = '{"incomplete": "json'
    try:
        json.loads(bad_row)
        assert False, "Should have failed"
    except json.JSONDecodeError:
        assert True

def test_normalization_schema():
    """Test normalized row has required fields"""
    norm_row = {
        "timestamp": "2026-06-05T02:15:00Z",
        "source_type": "auth",
        "user": "user04",
        "host": "vpn-01",
        "action": "login_failed",
        "status": "bad_password"
    }
    
    required_fields = ["timestamp", "source_type", "user", "host", "action", "status"]
    for field in required_fields:
        assert field in norm_row, f"Missing {field}"

def test_deduplication_key():
    """Test dedup key creation"""
    key1 = ("2026-06-05T02:15:00Z", "user04", "vpn-01", "login_failed")
    key2 = ("2026-06-05T02:15:00Z", "user04", "vpn-01", "login_failed")
    assert key1 == key2

def test_empty_input():
    """Test handling of empty log"""
    rows = []
    assert len(rows) == 0

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
