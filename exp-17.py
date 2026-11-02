control = input("Enter security control: ").lower()

if "policy" in control or "management" in control:
    print("Domain: Organizational Control")
elif "employee" in control or "training" in control:
    print("Domain: People Control")
elif "door" in control or "camera" in control:
    print("Domain: Physical Control")
elif "firewall" in control or "encryption" in control:
    print("Domain: Technological Control")
else:
    print("Unknown Control")
