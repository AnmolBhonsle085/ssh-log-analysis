import re
from collections import defaultdict

LOG_FILE = "auth.log"
REPORT_FILE = "ssh_log_report.txt"
BRUTE_FORCE_THRESHOLD = 3   # keep low for demo

ip_count = defaultdict(int)
failed_events = []

# Step 1: Read log and detect failed logins
with open(LOG_FILE) as f:
    for line in f:
        if "Failed password" in line:
            failed_events.append(line.strip())
            ip = re.search(r"\d+\.\d+\.\d+\.\d+", line)
            if ip:
                ip_count[ip.group()] += 1

# Step 2: Write report
with open(REPORT_FILE, "w") as report:
    report.write("SSH LOG ANALYSIS REPORT\n")
    report.write("=======================\n\n")

    report.write("1. Failed Login Events:\n")
    for event in failed_events:
        report.write(event + "\n")

    report.write("\n2. Failed Login Attempts per IP:\n")
    for ip, count in ip_count.items():
        report.write(f"{ip} : {count}\n")

    report.write("\n3. Brute-Force Detection:\n")
    for ip, count in ip_count.items():
        if count >= BRUTE_FORCE_THRESHOLD:
            report.write(f"ALERT: Brute-force suspected from {ip} ({count} attempts)\n")

print("Analysis complete.")
print(f"Report saved to {REPORT_FILE}")
