
from urllib.parse import urlparse
import ipaddress

def detect_phishing(url):
    suspicious_keywords = [
        "login", "verify", "update", "password",
        "secure", "banking", "account", "confirm"
    ]

    reasons = []
    parsed = urlparse(
        url if "://" in url else "http://" + url
    )

    hostname = (parsed.hostname or "").lower()

    if not hostname:
        return ["Invalid or missing hostname"]

    # Check for an IP address instead of a domain
    try:
        ipaddress.ip_address(hostname)
        reasons.append("Uses an IP address as the host")
    except ValueError:
        pass

    # Check suspicious keywords
    if any(word in url.lower() for word in suspicious_keywords):
        reasons.append("Contains suspicious keywords")

    # Check excessive subdomains
    if hostname.count(".") >= 3:
        reasons.append("Contains excessive subdomains")

    # Check for URL user-info tricks
    if "@" in parsed.netloc:
        reasons.append("Contains an @ symbol in the network location")

    if parsed.scheme != "https":
        reasons.append("Does not use HTTPS")

    return reasons


url = input("Enter a URL to check: ")
findings = detect_phishing(url)

if findings:
    print("\nWarning: URL has suspicious indicators.")
    for finding in findings:
        print("-", finding)
else:
    print("\nNo configured phishing indicators found.")
