attack = input("Enter attack type: ").lower()

layers = ["Firewall", "IDS", "Antivirus", "Authentication"]

print("\nDefense-in-Depth Simulation")

for layer in layers:
    print(layer, "checking...")

    if layer == "Firewall" and "malicious" in attack:
        print("Attack blocked by Firewall")
        break

    elif layer == "IDS" and "suspicious" in attack:
        print("Attack blocked by IDS")
        break

else:
    print("All layers checked. No attack blocked.")
