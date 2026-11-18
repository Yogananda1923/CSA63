
# Signature-based Intrusion Prevention System

# Known malicious traffic signatures
signatures = [
    "malware",
    "sql injection",
    "port scan",
    "brute force",
    "dos attack"
]

# Trusted source IP addresses
whitelist = [
    "192.168.1.10",
    "192.168.1.20"
]


def inspect_traffic(source_ip, packet_data):

    print("\nSource IP:", source_ip)
    print("Packet Data:", packet_data)

    # Check trusted sources first
    if source_ip in whitelist:
        print("ALLOWED: Trusted source (Whitelisted)")
        return

    # Check malicious signatures
    for signature in signatures:

        if signature in packet_data.lower():
            print("BLOCKED: Malicious traffic detected!")
            print("Matched Signature:", signature)
            return

    print("ALLOWED: No malicious signature detected.")


# Simulated incoming traffic
inspect_traffic(
    "192.168.1.10",
    "malware detected in packet"
)

inspect_traffic(
    "192.168.1.50",
    "SQL Injection attack detected"
)

inspect_traffic(
    "192.168.1.60",
    "Normal web request"
)
