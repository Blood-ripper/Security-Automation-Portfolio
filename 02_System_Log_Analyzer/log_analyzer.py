import re
from collections import defaultdict

# Configuration
LOG_FILE = "dummy_auth.log"
FAILED_LOGIN_THRESHOLD = 3 # Triggers alert if an IP fails 3 or more times

def analyze_logs(file_path):
    print(f"[*] Analyzing log file: {file_path}")
    failed_attempts = defaultdict(int)
    
    # Regex to extract the IP address from standard SSH "Failed password" logs
    regex_pattern = re.compile(r"Failed password for (?:invalid user )?\w+ from (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})")
    
    try:
        with open(file_path, "r") as file:
            for line in file:
                match = regex_pattern.search(line)
                if match:
                    ip_address = match.group(1)
                    failed_attempts[ip_address] += 1
                    
        print("\n=== Security Alert Audit ===")
        alert_triggered = False
        
        for ip, count in failed_attempts.items():
            if count >= FAILED_LOGIN_THRESHOLD:
                print(f"[CRITICAL ALERT] SSH Brute-Force detected from IP: {ip} ({count} failed attempts)")
                alert_triggered = True
            else:
                print(f"[INFO] Normal login failure from IP: {ip} ({count} attempts)")
        
        if not alert_triggered:
            print("[+] No brute-force activity detected across the threshold.")
            
    except FileNotFoundError:
        print(f"[-] Error: Log file '{file_path}' not found.")

if __name__ == "__main__":
    analyze_logs(LOG_FILE)