
import re
from collections import Counter

# Sample raw server logs
raw_logs = [
    '2026-10-22 10:00:00 INFO User login successful',
    '2026-10-22 10:01:00 ERROR Database connection failed',
    '2026-10-22 10:02:00 WARNING High CPU usage',
    '2026-10-22 10:03:00 ERROR Authentication failed',
    '2026-10-22 10:04:00 INFO File uploaded successfully'
]

# Logstash-style parsing
def parse_log(line):
    pattern = r"(\S+ \S+) (INFO|WARNING|ERROR) (.*)"
    match = re.match(pattern, line)

    if match:
        return {
            "timestamp": match.group(1),
            "level": match.group(2),
            "message": match.group(3)
        }
    return None


# Elasticsearch-style in-memory indexing
index = []

for line in raw_logs:
    event = parse_log(line)
    if event:
        index.append(event)

print("Indexed Events:")
for event in index:
    print(event)

# Kibana-style aggregation
counts = Counter(event["level"] for event in index)

print("\nLog Level Summary:")
for level, count in sorted(counts.items()):
    print(f"{level}: {count}")
