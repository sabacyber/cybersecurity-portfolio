import re
from collections import defaultdict

log_file = "logs/auth.log"

failed_attempts = defaultdict(int)
successful_logins = []
suspicious_ips = []

failed_pattern = r"Failed password .* from ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)"
success_pattern = r"Accepted password .* from ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)"

with open(log_file, "r") as file:
    for line in file:

        failed_match = re.search(failed_pattern, line)
        success_match = re.search(success_pattern, line)

        if failed_match:
            ip = failed_match.group(1)
            failed_attempts[ip] += 1

        if success_match:
            ip = success_match.group(1)
            successful_logins.append(ip)

print("\n===== SECURITY LOG ANALYSIS REPORT =====\n")

print("Failed Login Attempts by IP:\n")
for ip, count in failed_attempts.items():
    print(f"{ip} → {count} failed attempts")

print("\nSuccessful Logins:\n")
for ip in successful_logins:
    print(f"Successful login from {ip}")

print("\nPotential Brute Force Attacks:\n")
for ip, count in failed_attempts.items():
    if count >= 3:
        suspicious_ips.append(ip)
        print(f"⚠️ ALERT: Possible brute-force attack from {ip} ({count} failed attempts)")

if not suspicious_ips:
    print("No brute-force attacks detected.")

print("\n===== END OF REPORT =====\n")
