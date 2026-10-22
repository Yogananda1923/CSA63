
def classify_report(description, audience):
    text = (description + " " + audience).lower()

    keywords = {
        "Strategic": [
            "business leaders", "executives", "management",
            "long-term", "business risk", "policy",
            "senior management", "organizational risk"
        ],
        "Tactical": [
            "security analysts", "attack techniques",
            "tactics", "procedures", "mitre att&ck",
            "indicators", "threat actors", "defense strategy"
        ],
        "Operational": [
            "soc team", "incident response", "security operations",
            "active attack", "ip address", "malware sample",
            "immediate action", "incident details", "ip addresses"
        ]
    }

    scores = {}

    for category, words in keywords.items():
        scores[category] = sum(
            1 for word in words if word in text
        )

    highest_score = max(scores.values())

    if highest_score == 0:
        return "Unclassified"

    # Resolve ties using a fixed priority
    priority = ["Operational", "Tactical", "Strategic"]

    for category in priority:
        if scores[category] == highest_score:
            return category


description = input("Enter threat report description: ")
audience = input("Enter intended audience: ")

result = classify_report(description, audience)

print("\nThreat Intelligence Report Classification")
print("Description:", description)
print("Intended Audience:", audience)
print("Classification:", result)
