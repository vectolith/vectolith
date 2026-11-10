# Vectolith Organization Security Policy

Vectolith designs, trains, and deploys autonomous AI agents and vector infrastructure. We take the safety, integrity, and cryptographic privacy of all models, weights, webhooks, and onchain smart contracts seriously.

## Supported Repositories & Versions

The following active production systems receive high-priority security updates:

| Repository | Scope | Support Status |
| :--- | :--- | :--- |
| **`vectolith/velnor`** | Headless executive messaging agent & rsLoRA inference | :white_check_mark: Active (main) |
| **`vectolith/blud`** | Browser automation coordinator & Kernel integration | :white_check_mark: Active (main) |
| **`vectolith/pluco-network`** | Base mainnet smart contracts & NFT marketplace | :white_check_mark: Active (main) |
| **`vectolith/vectolith`** | Profile & foundation infrastructure | :white_check_mark: Active (main) |

## Reporting a Vulnerability

**Please do NOT report security vulnerabilities through public GitHub issues.**

If you discover a potential vulnerability in any Vectolith repository:

1. **Private GitHub Security Advisory (Preferred)**:
   Navigate to the **Security** tab of the impacted repository and click **"Report a vulnerability"** to open a confidential report.
2. **Direct Security Contact**:
   Email `security@vectolith.com` (or submit encrypted via our security lead).

### What to Include in Your Report

To help us triage and patch as rapidly as possible, please include:
- Description of the issue, severity, and potential impact.
- Affected repository, branch, and commit hash.
- Step-by-step reproduction instructions or Proof-of-Concept (PoC).
- Any details on mitigation steps or suspected root causes.

### Response Timelines & SLA

- **Initial Triage & Confirmation**: Within **24 hours**.
- **Assessment & Status Update**: Within **48 hours**.
- **Fix & Patch Deployment**: Within **72 hours** for critical severity; within **7 days** for medium severity.
- **Public Disclosure**: Coordinated disclosure only after the patch has been released and deployed.

## Core Security Invariants

All Vectolith repositories adhere strictly to these principles:
- **Zero Fabrication**: Systems must never fabricate execution receipts or hallucinate completed actions.
- **Cryptographic Credential Hygiene**: Raw API keys, private keys, passwords, and tokens are strictly quarantined from chat contexts and logs.
- **Tenant & Workspace Isolation**: Multi-tenant memory partitions (iMessage, SMS, Slack, Web) cannot cross-pollinate.
- **Consequential Action Gates**: Irreversible destructive external actions (fund transfers, data deletion, bulk messaging) require explicit confirmation.
