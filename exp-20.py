
def classify_threat(description):

    description = description.lower()

    threats = {
        "Phishing": [
            "fake website", "phishing email",
            "steal password", "suspicious link",
            "email scam", "credential theft"
        ],

        "DoS/DDoS": [
            "denial of service", "ddos",
            "dos attack", "server overload",
            "traffic flooding", "service unavailable"
        ],

        "Malware": [
            "virus", "ransomware", "trojan",
            "malicious software", "spyware",
            "worm", "infected file"
        ],

        "Man-in-the-Middle": [
            "man in the middle", "mitm",
            "intercept communication",
            "data interception", "session hijacking",
            "packet interception"
        ]
    }

    scores = {}

    for category, keywords in threats.items():
        scores[category] = sum(
            1 for keyword in keywords
            if keyword in description
        )

    highest = max(scores.values())

    if highest == 0:
        return "Unknown Threat Category"

    for category, score in scores.items():
        if score == highest:
            return category


description = input("Enter incident description: ")

result = classify_threat(description)

print("\nIncident Description:", description)
print("Identified Threat Category:", result)
