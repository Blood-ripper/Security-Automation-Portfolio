\# Automated System Log Analyzer \& Alerting Engine



\## Objective

A Python-based Security Operations Center (SOC) automation tool designed to ingest Linux system logs, parse authentication events, and detect brute-force attack patterns in real-time.



\## Skills \& Concepts Demonstrated

\*   \*\*Security Information and Event Management (SIEM) Logic:\*\* Replicates the core functionality of log ingestion and anomaly detection.

\*   \*\*Regular Expressions (Regex):\*\* Utilizes complex pattern matching to extract threat actor IP addresses from unstructured `auth.log` data.

\*   \*\*Threshold-Based Alerting:\*\* Employs stateful tracking to differentiate between benign login failures and targeted brute-force attacks.

\*   \*\*CompTIA Security+ Alignment:\*\* Demonstrates hands-on competency in Domain 4 (Security Operations) and Log Analysis.



\## How It Works

1\.  \*\*Ingestion:\*\* Reads unstructured Linux authentication logs (`/var/log/auth.log`).

2\.  \*\*Extraction:\*\* Applies a Regex pattern `(?:invalid user )?\\w+ from (\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3})` to isolate the source IP of failed login attempts.

3\.  \*\*Analysis:\*\* Aggregates failure counts per IP address.

4\.  \*\*Alerting:\*\* Automatically triggers a `\[CRITICAL ALERT]` if an IP exceeds the predefined security baseline (e.g., 3+ failed attempts).



\## Usage

1\. Clone the repository and navigate to the `02\_System\_Log\_Analyzer` directory.

2\. Run the script: `python log\_analyzer.py`

3\. The script will output an automated Security Alert Audit based on the provided log file.

