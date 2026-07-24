-- Hunt 1: Find user232 lateral movement
SELECT 
  timestamp,
  source_type,
  user,
  host,
  action
FROM normalized_timeline
WHERE user = 'user232'
ORDER BY timestamp;

-- Hunt 2: Find user314 lateral movement
SELECT 
  timestamp,
  source_type,
  user,
  host,
  action
FROM normalized_timeline
WHERE user = 'user314'
ORDER BY timestamp;

-- Hunt 3: Find user178 lateral movement
SELECT 
  timestamp,
  source_type,
  user,
  host,
  action
FROM normalized_timeline
WHERE user = 'user178'
ORDER BY timestamp;

-- Hunt 4: Find multi-source users (potential campaigns)
SELECT 
  user,
  COUNT(DISTINCT source_type) as source_count,
  COUNT(*) as event_count
FROM normalized_timeline
WHERE user != 'unknown'
GROUP BY user
HAVING COUNT(DISTINCT source_type) >= 2
ORDER BY event_count DESC;
