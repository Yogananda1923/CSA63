
def analyze_report(report):

    report = report.lower()

    improvement_areas = {
        "Patch Management": [
            "patch", "software update",
            "vulnerability", "outdated software"
        ],

        "Security Awareness": [
            "training", "awareness",
            "phishing education", "employee education"
        ],

        "Monitoring": [
            "monitoring", "logs",
            "alert", "detection"
        ],

        "Backup Strategy": [
            "backup", "recovery",
            "data restoration", "disaster recovery"
        ],

        "Access Control": [
            "access control", "password",
            "authentication", "authorization",
            "privilege"
        ]
    }

    found = []

    for area, keywords in improvement_areas.items():
        if any(word in report for word in keywords):
            found.append(area)

    print("\nIncident Report Analysis")
    print("-------------------------")

    if found:
        print("Identified Improvement Areas:")
        for area in found:
            print("-", area)
    else:
        print("No improvement areas identified.")

    print("Total Areas Found:", len(found))


report = input("Enter post-incident report: ")

analyze_report(report)
