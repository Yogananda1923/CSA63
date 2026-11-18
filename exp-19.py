
from collections import Counter

# Simulated security event dataset
events = [
    {"user": "admin", "status": "failed", "source": "192.168.1.1"},
    {"user": "john", "status": "success", "source": "192.168.1.2"},
    {"user": "admin", "status": "failed", "source": "192.168.1.1"},
    {"user": "alice", "status": "success", "source": "192.168.1.3"},
    {"user": "john", "status": "failed", "source": "192.168.1.2"}
]

# Operation 1: Search and filter events
print("Search Results: Failed Logins")
print("--------------------------------")

filtered = [
    event for event in events
    if event["status"] == "failed"
]

for event in filtered:
    print(event)

# Operation 2: Stats count by field
print("\nStats Count by User")
print("--------------------------------")

counts = Counter(
    event["user"] for event in events
)

for user, count in sorted(counts.items()):
    print(user, ":", count)

print("\nTotal Events:", len(events))
