
def identify_threat_area(scenario):
    scenario = scenario.lower()

    threat_areas = {
        "Banking Fraud Prevention": [
            "bank", "banking", "fraud", "transaction",
            "credit card", "financial"
        ],
        "Healthcare Data Protection": [
            "hospital", "healthcare", "patient",
            "medical", "health data", "clinical"
        ],
        "E-commerce Fraud Prevention": [
            "e-commerce", "online shopping", "retail",
            "online store", "payment gateway", "customer orders"
        ],
        "Network Security": [
            "network", "firewall", "intrusion",
            "malware", "server", "cyberattack"
        ],
        "Cloud Security": [
            "cloud", "aws", "azure", "cloud storage",
            "cloud server", "data breach"
        ]
    }

    scores = {}

    for area, keywords in threat_areas.items():
        scores[area] = sum(
            1 for keyword in keywords if keyword in scenario
        )

    best_area = max(scores, key=scores.get)

    if scores[best_area] == 0:
        return "No matching threat-intelligence area identified."

    return best_area


scenario = input("Enter a business scenario: ")

result = identify_threat_area(scenario)

print("Business Scenario:", scenario)
print("Relevant Threat-Intelligence Area:", result)
