import os
import hashlib
import json
import time

# Configuration
TARGET_DIR = "./secure_folder"
BASELINE_FILE = "baseline.json"

def calculate_sha256(filepath):
    """Calculates the SHA-256 hash of a given file."""
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return None
    except Exception as e:
        print(f"[!] Error reading {filepath}: {e}")
        return None

def create_baseline(directory, baseline_path):
    """Scans the directory and saves a baseline of file hashes."""
    print(f"\n[*] Calculating baseline for {directory}...")
    baseline = {}
    
    for root, _, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            file_hash = calculate_sha256(filepath)
            if file_hash:
                baseline[filepath] = file_hash
                
    with open(baseline_path, 'w') as f:
        json.dump(baseline, f, indent=4)
    print("[+] Baseline created successfully. Cryptographic hashes stored.\n")

def monitor_integrity(directory, baseline_path):
    """Continuously monitors the directory against the baseline."""
    print("\n[*] Starting continuous monitoring. Press Ctrl+C to stop.")
    
    if not os.path.exists(baseline_path):
        print("[-] Baseline not found. Please create a baseline first.")
        return

    with open(baseline_path, 'r') as f:
        baseline = json.load(f)

    try:
        while True:
            # Check for modified or new files
            for root, _, files in os.walk(directory):
                for file in files:
                    filepath = os.path.join(root, file)
                    current_hash = calculate_sha256(filepath)
                    
                    if filepath not in baseline:
                        print(f"[ALERT] New file detected: {filepath}")
                        baseline[filepath] = current_hash # Update baseline in memory
                    elif baseline[filepath] != current_hash:
                        print(f"[ALERT] File modified (Hash Mismatch): {filepath}")
                        baseline[filepath] = current_hash # Update baseline in memory

            # Check for deleted files
            missing_files = []
            for filepath in baseline.keys():
                if not os.path.exists(filepath):
                    print(f"[ALERT] File deleted: {filepath}")
                    missing_files.append(filepath)
            
            for file in missing_files:
                del baseline[file]
                
            time.sleep(2) # Wait 2 seconds before checking again
            
    except KeyboardInterrupt:
        print("\n[*] Monitoring stopped by user.")

if __name__ == "__main__":
    print("=== Host-Based File Integrity Monitor ===")
    print("1. Create New Baseline")
    print("2. Start Monitoring")
    choice = input("Select an option (1 or 2): ")

    if choice == '1':
        create_baseline(TARGET_DIR, BASELINE_FILE)
    elif choice == '2':
        monitor_integrity(TARGET_DIR, BASELINE_FILE)
    else:
        print("[-] Invalid selection.")