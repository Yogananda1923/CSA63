
class StatefulFirewall:
    def __init__(self):
        self.connections = set()

    def process_packet(self, source, destination, direction, port):
        print(
            f"{direction}: {source} -> {destination}, "
            f"Port {port}"
        )

        if direction == "OUTBOUND":
            # Track the outbound connection
            connection = (source, destination, port)
            self.connections.add(connection)
            print("ALLOWED: Outbound connection recorded")

        elif direction == "INBOUND":
            # Return traffic must match an existing connection
            connection = (destination, source, port)

            if connection in self.connections:
                print("ALLOWED: Return traffic matches connection")
            else:
                print("BLOCKED: Unsolicited inbound traffic")

        else:
            print("BLOCKED: Unknown traffic direction")


firewall = StatefulFirewall()

# Outbound request from internal host
firewall.process_packet(
    "192.168.1.10", "203.0.113.20", "OUTBOUND", 443
)

# Return traffic for the tracked connection
firewall.process_packet(
    "203.0.113.20", "192.168.1.10", "INBOUND", 443
)

# Unsolicited inbound connection
firewall.process_packet(
    "198.51.100.25", "192.168.1.10", "INBOUND", 22
)
