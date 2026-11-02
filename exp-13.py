data = input("Enter collected data: ").lower()

context = "attack" in data or "malware" in data
confidence = "verified" in data or "confirmed" in data
action = "block" in data or "mitigate" in data

print("Context:", context)
print("Confidence:", confidence)
print("Actionability:", action)

if context and confidence and action:
    print("Result: Genuine Threat Intelligence")
else:
    print("Result: Raw Data")
