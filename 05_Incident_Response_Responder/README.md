\# Automated Incident Response Playbook \& Host Isolator



\## Objective

A Python-based SOAR (Security Orchestration, Automation, and Response) script designed to simulate automated containment playbooks during a security incident.



\## Skills \& Concepts Demonstrated

\*   \*\*Incident Response Lifecycle:\*\* Implements automated containment, evidence collection, and escalation workflows.

\*   \*\*Audit Trail Compliance:\*\* Generates strict timestamped logs (`incident\_audit.log`) to maintain chain-of-custody during a forensic investigation.

\*   \*\*Remediation Automation:\*\* Simulates rapid network isolation to stop lateral movement during a ransomware or C2 callback attack.

\*   \*\*CompTIA Security+ Alignment:\*\* Aligns with Domain 4 (Security Operations) incident handling and mitigation protocols.



\## How It Works

1\.  \*\*Trigger:\*\* Ingests a malicious IP indicator from detection telemetry.

2\.  \*\*Collection:\*\* Simulates a memory and socket artifact dump for forensic analysis.

3\.  \*\*Containment:\*\* Programmatically executes a simulated firewall block rule to sever network access.

4\.  \*\*Escalation:\*\* Records audit events to a structured local log file for SIEM ingestion.



\## Usage

1\. Navigate to the `05\_Incident\_Response\_Responder` directory.

2\. Run the script: `python ir\_responder.py`

3\. Enter a target rogue IP to simulate an automated containment action.

