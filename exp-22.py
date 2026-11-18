
def detect_brute_force(logs, target_user):

    failed_count = 0
    threshold = 3
    attack_detected = False

    print("\nAuthentication Log Analysis")
    print("----------------------------")

    for line in logs:

        parts = line.strip().split()

        if len(parts) < 3:
            continue

        username = parts[1]
        status = parts[2].lower()

        if username != target_user:
            continue

        if status == "failed":
            failed_count += 1

            print("Failed login:", username)

        elif status == "success":

            print("Successful login:", username)

            if failed_count >= threshold:
                attack_detected = True
                print("\nALERT: Possible Brute-Force Attack!")
                print("Failed Attempts:", failed_count)

            failed_count = 0

    if not attack_detected:
        print("\nNo brute-force pattern detected.")


# Sample authentication logs
logs = [
    "10:00 admin failed",
    "10:01 admin failed",
    "10:02 admin failed",
    "10:03 admin success",
    "10:04 john success"
]

target_user = input("Enter username to monitor: ")

detect_brute_force(logs, target_user)
