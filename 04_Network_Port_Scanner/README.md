\# Multi-Threaded Network Port Scanner



\## Objective

A Python-based network reconnaissance and attack surface auditing tool. This script utilizes multi-threading to rapidly scan a target's TCP ports, identifying exposed services and potential vulnerabilities.



\## Skills \& Concepts Demonstrated

\*   \*\*Network Protocols:\*\* Deep understanding of the OSI model, TCP/IP handshakes, and socket programming.

\*   \*\*Concurrency \& Threading:\*\* Uses Python's `concurrent.futures.ThreadPoolExecutor` to spawn 100 simultaneous threads, massively reducing scan times compared to sequential scanning.

\*   \*\*Attack Surface Management:\*\* Automates the discovery phase of an ethical hacking or vulnerability management engagement.

\*   \*\*CompTIA Security+ Alignment:\*\* Demonstrates hands-on competency in Domain 3 (Architecture and Design) and Domain 4 (Security Operations - Reconnaissance).



\## How It Works

1\.  \*\*Initialization:\*\* The script asks for a target IP or hostname (defaults to safe local testing on `127.0.0.1`).

2\.  \*\*Thread Pooling:\*\* It spins up a pool of 100 worker threads.

3\.  \*\*Socket Connections:\*\* Each thread attempts a TCP connection (`socket.SOCK\_STREAM`) to a specific port in the 1-1024 range. 

4\.  \*\*Timeout \& Error Handling:\*\* Implements a strict `0.5s` timeout so the scanner does not hang on filtered/dropped packets (simulating firewall presence).

5\.  \*\*Output Validation:\*\* Thread-safe locks (`threading.Lock()`) prevent output overlapping, resulting in a clean audit report of open ports.



\## Usage

1\. Clone the repository and navigate to the `04\_Network\_Port\_Scanner` directory.

2\. Run the script: `python port\_scanner.py`

3\. Enter a target IP address (ensure you have explicit authorization to scan external targets).

