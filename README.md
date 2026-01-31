# SSH Log Analysis & Brute-Force Detection using Python

## Overview
This project demonstrates how Python can be used in cybersecurity to analyze Linux SSH authentication logs, detect failed login attempts**, identify potential brute-force attacks**, and generate a structured security report.

The project simulates a SOC (Security Operations Center) style workflow where authentication logs are monitored and analyzed automatically instead of manual review.

---

## Objectives
- Detect failed SSH login attempts from Linux authentication logs  
- Aggregate failed login attempts per IP address  
- Identify potential brute-force attacks using a configurable threshold  
- Generate a structured security report for investigation and review  

---

## Tools & Technologies
- Python 3  
- Linux authentication logs (sanitized sample)  
- Regular Expressions (Regex)  
- File handling & automation  

---

## Project Structure
ssh-log-analysis/
├── ssh_log_analysis.py
├── ssh_log_report.txt
├── README.md
└── screenshots/


> **Note:**  
> The original authentication log file is not included to avoid sharing sensitive system data.  
> A sanitized sample log was used during development and testing.

---

## How It Works
1. The script scans Linux SSH authentication logs for `"Failed password"` events  
2. Extracts attacker IP addresses using regex  
3. Counts failed login attempts per IP  
4. Applies a threshold to detect possible brute-force attacks  
5. Exports results into a structured security report

## How to Run
```bash
python3 ssh_log_analysis.py

## Output
After execution, the script generates a report file: ssh_log_report.txt

## Key Features

Automated log analysis (no manual inspection)

IP-based attack pattern detection

Configurable brute-force detection threshold

Security-focused reporting output

Author

ANMOL BHONSLE
