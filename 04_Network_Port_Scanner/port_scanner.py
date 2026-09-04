import socket
import sys
import threading
from concurrent.futures import ThreadPoolExecutor

# Lock to prevent print statements from overlapping on the screen
print_lock = threading.Lock()
open_ports = []

def scan_port(ip, port):
    """Attempts to connect to a specific TCP port on the target IP."""
    try:
        # Create a socket object (IPv4, TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5) # Fast timeout for rapid scanning
        
        # connect_ex returns 0 if the connection succeeds (port is open)
        result = s.connect_ex((ip, port))
        
        if result == 0:
            with print_lock:
                print(f"[+] Port {port} is OPEN")
            open_ports.append(port)
            
        s.close()
    except Exception:
        pass # Silently ignore network errors for closed/filtered ports

def start_scan(target_ip, start_port, end_port):
    print(f"\n[*] Starting multi-threaded scan on target: {target_ip}")
    print(f"[*] Scanning ports {start_port} to {end_port}...")
    print("[*] Spawning 100 concurrent threads...\n")
    
    # Using ThreadPoolExecutor for enterprise-grade multi-threading
    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, target_ip, port)
            
    print("\n=== Attack Surface Audit Complete ===")
    if open_ports:
        print(f"[!] Total Open Ports Found: {len(open_ports)}")
        print(f"[!] Open Ports: {sorted(open_ports)}")
    else:
        print("[-] No open TCP ports found in that range.")

if __name__ == "__main__":
    print("--- Security Operations: Network Port Scanner ---")
    
    # Defaulting to localhost (127.0.0.1) for safe, legal testing
    target = input("Enter target IP (or press Enter for '127.0.0.1' - localhost): ")
    if not target.strip():
        target = "127.0.0.1"
        
    try:
        # Resolve hostname to IP just in case a URL is entered
        target_ip = socket.gethostbyname(target)
        
        # Scan the "Well-Known" ports (1 to 1024)
        start_port = 1
        end_port = 1024
        
        start_scan(target_ip, start_port, end_port)
        
    except socket.gaierror:
        print("\n[-] Error: Hostname could not be resolved.")
    except KeyboardInterrupt:
        print("\n[-] Scan canceled by user.")
        sys.exit()