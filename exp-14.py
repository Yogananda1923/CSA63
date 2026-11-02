events = []

n = int(input("Enter number of events: "))

for i in range(n):
    ip = input("Enter IP address: ")
    status = input("Enter status: ")

    events.append({"IP": ip, "Status": status})

print("\nSIEM Pipeline")
print("1. Collecting Events")
print("2. Normalizing Events")
print("3. Correlating Events")

for event in events:
    if event["Status"].lower() == "failed":
        print("ALERT: Suspicious activity from", event["IP"])
