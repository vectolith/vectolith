# Vectolith Organization Security Policy

Vectolith develops software and research systems across autonomous AI, model infrastructure, cryptographic wallets, digital ownership, messaging and systems engineering. This policy defines the organization-wide vulnerability reporting process and minimum security invariants.

This policy is a standard, not a certification that every repository has implemented or independently verified every control. Product-specific threat models and release gates remain mandatory.

## Scope and repository coverage

The policy applies to all repositories owned or operated by Vectolith. The following register distinguishes maintained products from research and unclassified repositories; it does not imply that every project is production-supported.

| Repository | Scope | Current classification | Security posture |
|---|---|---|---|
| `vectolith/vectolith` | Company identity, portfolio and shared governance | Company foundation | Organization policy and portfolio register |
| `vectolith/velnor` | AI agent platform, messaging and execution runtime | Active development; production deployment documented | Product security and operations documentation exist; ongoing verification required |
| `vectolith/blud` | Personal agent and browser automation | Active development; README says not intended for production use | Product security controls documented; no production readiness claim |
| `vectolith/Models-by-vectolith.` | Model training, evaluation, artifacts and releases | Research/infrastructure | Training rights, data provenance, model qualification and release gates remain mandatory |
| `vectolith/pluco-network` | Base smart contracts and marketplace | Active development; deployment documentation contains a contradiction | Deployment evidence and contract CI require reconciliation |
| `vectolith/VaultETH` | Native self-custodial wallet clients | Active development; real-money release gated | Threat model and security policy exist; independent audit and release gates remain outstanding |
| `vectolith/NYR` | x86-64 kernel research | Research | Kernel-specific memory, privilege and interrupt safety review required |
| `vectolith/Cipher-messenger` | Matrix-based encrypted messaging | Phase 0 research | Local E2EE validation only; not a released messaging product |
| `vectolith/quietline-messenger` | Matrix-based encrypted messaging | Phase 0 research | Local E2EE validation only; scope overlap with Cipher unresolved |
| `vectolith/AERYN` | Autonomous intelligence and research synthesis | Research/specification; not released | Initial product charter is proposed; detailed specification and threat model remain outstanding |
| `vectolith/demo-repository` | GitHub demonstration | Internal demo | Not a supported product |
| `vectolith/my-project` | Unclassified placeholder | Unclassified | No product support claim |

Maintained products and active research repositories must accept vulnerability reports even when they are not production releases. The absence of a repository from a production support list does not make security reporting optional.

## Reporting a vulnerability

**Do not report security vulnerabilities through public GitHub issues.**

1. **Private GitHub Security Advisory (preferred):** use the Security tab of the affected repository and select **Report a vulnerability**, where private vulnerability reporting is enabled.
2. **Direct security contact:** email `security@vectolith.com`.

Do not include live secrets, recovery phrases, private keys or unnecessary personal data in a report. Use a safe reproduction and redact sensitive values.

### What to include

- Affected repository, branch, commit and version.
- Description, impact and suspected severity.
- Reproduction steps or a proof of concept that does not harm users or systems.
- Affected deployment or environment, if known.
- Mitigations or workarounds, if known.

### Response targets

These are organizational response targets, not a guarantee that every fix can be deployed within the stated window.

- Initial triage acknowledgement: within 24 hours.
- Assessment and status update: within 48 hours.
- Critical remediation target: within 72 hours where a safe fix and deployment path are available.
- Medium remediation target: within 7 days where a safe fix and deployment path are available.
- Public disclosure: coordinated after mitigation/release, subject to applicable legal and user-safety considerations.

If a target cannot be met, communicate the reason, mitigation and next update through the private reporting channel.

## Organization-wide security invariants

Every maintained product must implement and test controls appropriate to its threat model:

- **No fabricated execution receipts:** systems must not claim an external action completed without validated evidence from the external system.
- **Credential hygiene:** raw API keys, private keys, passwords, recovery phrases and tokens must not enter model context, source control, client bundles or logs.
- **Tenant and workspace isolation:** user and workspace data must be scoped at the trusted data-access boundary.
- **Consequential action gates:** irreversible or financially consequential actions require explicit authorization and approval appropriate to the action.
- **Least privilege:** services, agents, integrations and deployment identities receive only necessary permissions.
- **Secure transport:** production network traffic uses authenticated TLS; webhook signatures and freshness are verified where supported.
- **Safe failure:** timeouts and ambiguous external outcomes must not be misreported as success or blindly retried when actions are non-idempotent.
- **Auditability:** record action metadata and security-relevant events without recording secrets or unnecessary sensitive content.
- **Data lifecycle:** retention, deletion, backup, recovery and access review are documented for systems processing user data.
- **Supply-chain integrity:** critical dependencies, build actions and release artifacts are traceable and verified.

## Product-specific requirements

- **AI and agent systems:** tool schemas, permissions, approvals, prompt-injection boundaries and proof-of-action semantics are enforced by trusted runtime code, not model-generated text.
- **Model development:** training data and teacher outputs require verified provenance, license and specific training-use permission; evaluation holdouts must be protected.
- **Wallets and cryptographic products:** key generation, storage, recovery, signing, transaction validation and residual memory risks require specialist review. No real-money readiness claim without appropriate independent security review.
- **Smart contracts:** maintain a canonical deployment register, verify source/bytecode, run contract tests in CI, and document privileged roles, upgradeability, fees and withdrawal paths.
- **Messaging products:** validate E2EE, device verification, homeserver configuration, registration and federation choices before any public release.
- **Kernel and systems software:** document privilege boundaries, memory ownership, concurrency assumptions, interrupt safety and boot/recovery behavior.

## Governance and exceptions

The [company-wide engineering governance](docs/ENGINEERING_GOVERNANCE.md) defines lifecycle and release gates. The [portfolio register](docs/PORTFOLIO_REGISTER.md) identifies current repository classifications and known gaps.

Security exceptions must identify the requirement, reason, affected product/version, risk, compensating control, accountable owner, expiry/review date and approval record. A documentation exception does not waive a critical security or legal release gate.
