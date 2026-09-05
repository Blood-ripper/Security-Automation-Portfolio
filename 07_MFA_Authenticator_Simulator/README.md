\# Enterprise MFA / TOTP Token Generator \& Validator



\## Objective

A Python-based Multi-Factor Authentication (MFA) simulator implementing the Time-based One-Time Password (TOTP) algorithm (RFC 6238) to secure access control and identity management workflows.



\## Skills \& Concepts Demonstrated

\*   \*\*Cryptographic Hashing:\*\* Utilizes HMAC-SHA1 and base32 decoding to manage secure token secrets.

\*   \*\*Identity and Access Management (IAM):\*\* Simulates enterprise-grade MFA mechanisms used by standard authenticators (e.g., Google Authenticator, Microsoft Authenticator).

\*   \*\*Time-Step Mathematics:\*\* Computes 30-second sliding time windows and binary counter representations for dynamic token validation.

\*   \*\*CompTIA Security+ Alignment:\*\* Aligns with Domain 1 (General Security Concepts) and Domain 3 (Identity and Access Management / Authentication controls).



\## How It Works

1\.  \*\*Secret Ingestion:\*\* Decodes a base32 encoded shared secret key.

2\.  \*\*Time Window Calculation:\*\* Divides current Unix epoch time by a 30-second interval counter.

3\.  \*\*HMAC Generation:\*\* Combines the secret and counter bytes via SHA-1 hashing, performing dynamic truncation to extract a 6-digit one-time code.

4\.  \*\*Audit Cycling:\*\* Simulates live continuous token validation cycles with active TTL countdowns.



\## Usage

1\. Navigate to the `07\_MFA\_Authenticator\_Simulator` directory.

2\. Run the script: `python mfa\_auth.py`

