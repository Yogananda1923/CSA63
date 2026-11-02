alert = input("Enter SOC alert: ").lower()

if "ransomware" in alert or "data breach" in alert:
    print("Priority: P1 - Critical")
elif "malware" in alert or "unauthorized access" in alert:
    print("Priority: P2 - High")
elif "failed login" in alert:
    print("Priority: P3 - Medium")
else:
    print("Priority: P4 - Low")
