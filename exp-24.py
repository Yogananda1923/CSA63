
# Minimum required security baseline
baseline = {
    "password_length": 12,
    "firewall_enabled": True,
    "antivirus_enabled": True,
    "backup_enabled": True,
    "mfa_enabled": True
}

# Organization's current configuration
current_config = {
    "password_length": 8,
    "firewall_enabled": True,
    "antivirus_enabled": False,
    "backup_enabled": True,
    "mfa_enabled": False
}

def assess_security(baseline, current):

    print("\nSecurity Baseline Assessment")
    print("-----------------------------")

    failed = []

    for control, required in baseline.items():

        actual = current.get(control)

        if control == "password_length":

            if not isinstance(actual, int) or actual < required:
                failed.append(control)

        elif actual != required:
            failed.append(control)

    print("\nFailed Security Controls:")

    if failed:
        for control in failed:
            print("-", control)
    else:
        print("All security controls meet the baseline.")

    print("\nTotal Failed Controls:", len(failed))


assess_security(baseline, current_config)
