
import socket

def port_scanner(target, start_port, end_port):
    print("\nTarget Host:", target)
    print("Scanning ports...")
    print("-" * 35)

    try:
        ip = socket.gethostbyname(target)
        print("Target IP:", ip)

        for port in range(start_port, end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)

            result = sock.connect_ex((ip, port))

            if result == 0:
                print(f"Port {port}: OPEN")

            sock.close()

        print("-" * 35)
        print("Scan completed.")

    except socket.gaierror:
        print("Error: Invalid hostname.")
    except OSError as e:
        print("Network error:", e)


target = input("Enter target host (e.g., 127.0.0.1): ")
start_port = int(input("Enter starting port: "))
end_port = int(input("Enter ending port: "))

if 1 <= start_port <= end_port <= 65535:
    port_scanner(target, start_port, end_port)
else:
    print("Invalid port range. Use ports 1 to 65535.")
