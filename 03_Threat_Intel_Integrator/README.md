\# Automated Threat Intel API Integrator



\## Objective

A Python-based Security Orchestration, Automation, and Response (SOAR) script that automatically queries a public REST API to enrich suspicious IP addresses with geolocation, ISP, and organizational context.



\## Skills \& Concepts Demonstrated

\*   \*\*API Integration:\*\* Connects to external REST APIs using native Python libraries, handling HTTP requests and network exceptions.

\*   \*\*JSON Data Parsing:\*\* Extracts and formats specific telemetry from structured JSON responses.

\*   \*\*Automated Triage Logic:\*\* Employs programmatic logic to assess risk (e.g., flagging traffic originating from datacenters or cloud providers as higher risk than residential ISPs).

\*   \*\*CompTIA Security+ Alignment:\*\* Demonstrates competency in Domain 4 (Threat Intelligence and Incident Response) by automating the initial triage phase of a security alert.



\## How It Works

1\.  \*\*Input:\*\* Accepts a target IP address via standard input (simulating an alert feed from a SIEM).

2\.  \*\*Enrichment:\*\* Sends an HTTP GET request to `ip-api.com` to resolve the IP address.

3\.  \*\*Parsing:\*\* Decodes the JSON response to extract the ISP, Organization, City, and Country.

4\.  \*\*Triage:\*\* Analyzes the ISP/Organization string against a predefined list of cloud and datacenter keywords to assign a baseline risk assessment.

5\.  \*\*Output:\*\* Generates a clean, structured security report in the terminal.



\## Usage

1\. Clone the repository and navigate to the `03\_Threat\_Intel\_Integrator` directory.

2\. Run the script: `python threat\_intel.py`

3\. Enter a target IP address (or press Enter to test with Google's `8.8.8.8` DNS server) to view the automated Threat Intelligence report.

