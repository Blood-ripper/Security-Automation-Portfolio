import os
import sys
import time
import datetime

# Simulated Incident Response Playbook: Host Isolation & Evidence Gathering

def log_incident(action, details):
    """Logs IR actions with a strict timestamp for compliance and chain-of-custody."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] [{action.upper()}] {details}\n"
    
    print(log_entry.strip())
    
    # Write to a local incident log file for audit trails
    with open("incident_audit.log", "a") as log_file:
        log_file.write(log_entry)

def simulate_containment(target_ip):
    """Simulates network isolation and firewall block rule creation for a compromised host/IP."""
    print(f"\n[!] ALERT: Malicious activity detected originating from / communicating with: {target_ip}")
    print("[*] Initiating Automated Incident Response Playbook: 'CONTAIN_HOST'...")
    time.sleep(1)
    
    # Step 1: Evidence collection simulation
    log_incident("COLLECT", "Dumping active network socket states and process memory footprint...")
    time.sleep(1)
    
    # Step 2: Simulated Firewall Rule Application (Windows Firewall / iptables simulation)
    log_incident("CONTAINMENT", f"Executing system command to block all inbound/outbound traffic to {target_ip}")
    
    # In a real enterprise script, this would execute os.system(f"netsh advfirewall firewall add rule name='IR_Block_{target_ip}' dir=in action=block remoteip={target_ip}")
    print(f"[+] SUCCESS: Firewall rule applied. Traffic isolated for {target_ip}.")
    
    # Step 3: Alert escalation
    log_incident("ESCALATION", "PagerDuty / SIEM ticket updated with containment status and artifact logs.")
    print("==================================================")
    print("[*] Incident containment complete. System secured for forensic analysis.")

if __name__ == "__main__":
    print("--- Security Operations: Automated IR Playbook ---")
    
    # Simulate a rogue C2 (Command and Control) IP address caught by telemetry
    suspicious_ip = input("Enter rogue IP/Host to isolate (or press Enter to use default '192.168.1.105'): ")
    if not suspicious_ip.strip():
        suspicious_ip = "192.168.1.105"
        
    simulate_containment(suspicious_ip)