
# Define network segments and their trust levels
segments = {
    "Guest": 1,
    "Employee": 2,
    "Server": 3,
    "Sensitive": 4
}

# Define permitted source-destination pairs
allowed_access = {
    ("Guest", "Guest"),
    ("Employee", "Server"),
    ("Server", "Sensitive")
}

def check_access(source, destination):
    print(f"\nAccess request: {source} -> {destination}")

    if source not in segments or destination not in segments:
        print("BLOCKED: Unknown network segment")
    elif (source, destination) in allowed_access:
        print("ALLOWED: Policy permits access")
    else:
        print("BLOCKED: Network segmentation policy")

# Simulate access attempts
check_access("Guest", "Sensitive")
check_access("Guest", "Server")
check_access("Employee", "Server")
check_access("Server", "Sensitive")
