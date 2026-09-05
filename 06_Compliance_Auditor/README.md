\# Automated System Hardening \& Compliance Auditor



\## Objective

A Python-based configuration auditing tool designed to assess host security posture, evaluate runtime compliance against baseline standards, and detect environmental misconfigurations.



\## Skills \& Concepts Defined

\*   \*\*Security Posture Assessment:\*\* Automates host auditing to verify environment hygiene and security controls.

\*   \*\*Vulnerability \& Configuration Management:\*\* Scans for exposed environment variables, insecure permissions, and outdated runtimes.

\*   \*\*Quantitative Scoring:\*\* Calculates a deterministic compliance percentage (`100%` passing state) for quick executive reporting.

\*   \*\*CompTIA Security+ Alignment:\*\* Aligns with Domain 3 (Architecture and Design) secure configuration and hardening concepts.



\## How It Works

1\.  \*\*Environment Telemetry:\*\* Captures OS architecture, platform type, and active Python runtime versions.

2\.  \*\*Secret Leak Detection:\*\* Parses active environment variables to prevent accidental credential exposure (e.g., hardcoded API keys or AWS secrets).

3\.  \*\*Permission \& Binding Audits:\*\* Evaluates file path access controls and network loopback integrity.

4\.  \*\*Reporting:\*\* Generates a structured compliance summary indicating pass/fail metrics and hardening status.



\## Usage

1\. Navigate to the `06\_Compliance\_Auditor` directory.

2\. Run the auditor: `python auditor.py`

