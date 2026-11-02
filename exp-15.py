text = input("Enter incident description: ").lower()

if "phishing" in text or "fake email" in text:
    print("Root Cause: Phishing")
elif "unpatched" in text or "outdated software" in text:
    print("Root Cause: Unpatched Vulnerability")
elif "misconfiguration" in text or "open port" in text:
    print("Root Cause: Misconfiguration")
elif "employee" in text or "insider" in text:
    print("Root Cause: Insider Threat")
elif "vendor" in text or "third-party" in text:
    print("Root Cause: Supply-Chain Compromise")
else:
    print("Root Cause: Unknown")
