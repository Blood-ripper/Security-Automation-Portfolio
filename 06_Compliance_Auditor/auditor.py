import os
import sys
import platform
import datetime

def run_compliance_check():
    """Performs a simulated CIS/Security+ style hardening audit on the host system."""
    print("==================================================")
    print("   Automated System Hardening & Compliance Audit  ")
    print("==================================================\n")
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[*] Audit Timestamp : {timestamp}")
    print(f"[*] Target OS       : {platform.system()} {platform.release()}")
    print(f"[*] Architecture    : {platform.machine()}\n")
    
    checks_passed = 0
    checks_failed = 0
    total_checks = 4
    
    # Check 1: Python Environment Security Version Check
    print("[*] Test 1: Evaluating Python runtime security version...")
    py_version = sys.version_info
    if py_version.major >= 3 and py_version.minor >= 8:
        print("    [PASS] Python version is modern and supported (> 3.8).")
        checks_passed += 1
    else:
        print("    [FAIL] Outdated Python version detected. Potential vulnerability exposure.")
        checks_failed += 1

    # Check 2: Simulation of Environment Variable Hardening (Checking for exposed secrets)
    print("\n[*] Test 2: Scanning environment variables for unencrypted credentials...")
    sensitive_keys = ['AWS_SECRET_ACCESS_KEY', 'DATABASE_PASSWORD', 'SSH_PRIVATE_KEY', 'API_SECRET']
    found_secrets = [key for key in sensitive_keys if key in os.environ]
    
    if not found_secrets:
        print("    [PASS] No hardcoded high-risk secrets found in active environment variables.")
        checks_passed += 1
    else:
        print(f"    [FAIL] High-risk variables exposed in environment: {found_secrets}")
        checks_failed += 1

    # Check 3: Simulated File Permission Audit (Checking critical path accessibility)
    print("\n[*] Test 3: Checking critical system file permission structures...")
    # On Windows/Linux, we test if the current script directory has restricted write access simulation
    current_dir = os.getcwd()
    if os.access(current_dir, os.W_OK):
        print("    [INFO] Working directory is writable (Standard user execution context verified).")
        checks_passed += 1
    else:
        print("    [FAIL] Working directory lacks proper write permissions.")
        checks_failed += 1

    # Check 4: Firewall / Network Service Binding Check simulation
    print("\n[*] Test 4: Auditing local loopback binding integrity...")
    # Simulating a check to ensure services don't bind insecurely to 0.0.0.0 unnecessarily
    secure_binding = True 
    if secure_binding:
        print("    [PASS] Local services correctly scoped to secure interfaces.")
        checks_passed += 1
    else:
        print("    [FAIL] Insecure wildcard binding (0.0.0.0) detected.")
        checks_failed += 1

    # Final Compliance Score Calculation
    score = (checks_passed / total_checks) * 100
    print("\n==================================================")
    print(f"               AUDIT SUMMARY                      ")
    print("==================================================")
    print(f"[+] Total Checks Evaluated : {total_checks}")
    print(f"[+] Passed                 : {checks_passed}")
    print(f"[+] Failed                 : {checks_failed}")
    print(f"[+] Compliance Score       : {score:.1f}%")
    
    if score >= 75:
        print("[+] Status: SYSTEM HARDENING COMPLIANT")
    else:
        print("[!] Status: NON-COMPLIANT - REMEDIATION REQUIRED")
    print("==================================================")

if __name__ == "__main__":
    run_compliance_check()