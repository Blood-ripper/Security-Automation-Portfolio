\# Host-Based File Integrity Monitor (HIDS)



\## Objective

A lightweight, automated Host-Based Intrusion Detection System (HIDS) developed in Python. This tool establishes a cryptographic baseline of critical files and continuously monitors for unauthorized modifications, additions, or deletions, effectively detecting tampering and potential ransomware activity.



\## Skills \& Concepts Demonstrated

\*   \*\*Cryptographic Hashing:\*\* Utilizes SHA-256 to ensure data integrity (CIA Triad).

\*   \*\*Continuous Monitoring:\*\* Simulates automated Endpoint Detection and Response (EDR) behavior.

\*   \*\*Incident Alerting:\*\* Real-time terminal output for hash mismatches indicating malicious activity.

\*   \*\*Python Automation:\*\* File system parsing, JSON state management, and exception handling.



\## How It Works

1\.  \*\*Baseline Creation:\*\* The script traverses a target directory, calculates the SHA-256 hash for every file, and stores these known-good states in a `baseline.json` file.

2\.  \*\*Continuous Auditing:\*\* The script enters an infinite loop, continuously recalculating hashes of the live directory.

3\.  \*\*Threat Detection:\*\* If a file's hash changes (modification), a new file appears (unauthorized drop), or a file disappears (deletion), the script immediately triggers an alert.



\## Usage

1\. Clone the repository and navigate to the directory.

2\. Run the script: `python fim.py`

3\. Select Option `1` to calculate the initial secure baseline.

4\. Select Option `2` to begin live monitoring.

