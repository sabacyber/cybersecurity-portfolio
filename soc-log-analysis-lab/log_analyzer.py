import re
from collections import defaultdict

log_file = "logs/auth.log"

failed_attempts = defaultdict(int)

pattern = r"Failed password .* from ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)"

with open(log_file, "r") as file:
    for line in file:
        match = re.search(pattern, line)
        if match:
            ip = match.group(1)
            failed_attempts[ip] += 1

print("\nSuspicious Login Activity Detected:\n")

for ip, attempts in failed_attempts.items():
    if attempts >= 3:
        print(f"⚠️ Possible brute-force attack from {ip} ({attempts} failed attempts)")
