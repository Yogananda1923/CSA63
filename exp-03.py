
def check_security_policy(document):
    required_elements = {
        "Scope": ["scope", "purpose and scope", "applies to"],
        "Roles and Responsibilities": [
            "roles and responsibilities", "responsibilities",
            "roles"
        ],
        "Enforcement": ["enforcement", "disciplinary action", "violations"],
        "Review Cycle": [
            "review cycle", "review annually", "review every year",
            "review periodically"
        ],
        "Approval Authority": [
            "approval authority", "approved by",
            "authorized by", "approval"
        ]
    }

    document = document.lower()
    missing = []

    for element, keywords in required_elements.items():
        if not any(keyword in document for keyword in keywords):
            missing.append(element)

    print("\nSecurity Policy Assessment Report")
    print("-" * 40)

    if missing:
        print("Missing governance elements:")
        for element in missing:
            print("-", element)
    else:
        print("All required governance elements are present.")

    print("\nTotal missing elements:", len(missing))


# Read the draft security policy
print("Enter the draft security policy (type END on a new line to finish):")

lines = []
while True:
    line = input()
    if line.strip().upper() == "END":
        break
    lines.append(line)

document = "\n".join(lines)

check_security_policy(document)
