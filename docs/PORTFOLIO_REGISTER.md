# Vectolith portfolio register

**Review baseline:** 2026-11-18  
**Owner:** Vectolith  
**Purpose:** Public-facing inventory of Vectolith products and research initiatives, with evidence-backed maturity and product-specific release gates.

This register is a company portfolio index, not a shared product architecture or dependency map. A product's presence here does not certify production operation, security, commercial readiness or release status.

## Portfolio principles

- Vectolith is the company and ownership identity. Every product is an independent standalone product with its own purpose, implementation, runtime, identity, data, deployment, operations and release lifecycle.
- No Vectolith product is required to use another Vectolith product. Optional integrations must be opt-in, replaceable and nonessential to core operation.
- Shared company standards cover security, privacy, provenance, accessibility, documentation and evidence quality. They do not create shared services, credentials, databases, deployment systems or synchronized release gates.
- Product maturity is recorded separately from strategic importance.
- Demonstrations, unit tests, CI success, deployment configuration and verified live operation are different evidence types.
- Do not describe a capability as live unless a reproducible test or deployment record establishes it.

## Product and project register

| Product | Independent purpose | Evidence-backed current position | Main next gate |
|---|---|---|---|
| [Vectolith](https://github.com/vectolith/vectolith) | Company identity, portfolio index and governance; not a product runtime | Public company profile and engineering governance repository | Maintain accurate company standards and portfolio inventory |
| [Velnor](https://github.com/vectolith/velnor) | Standalone general-purpose AI agent, integrations and its own execution runtime | Messaging/API surfaces, provider routing, tenant state and operational documentation are present; live deployment health and provider operation require independent verification | Verify live provider delivery, observability, retention, rate limits and independent deployment/release evidence |
| [Blud](https://github.com/vectolith/blud) | Standalone personal agent with browser automation and protected credential vault | Browser automation, credential vault and external integrations are documented; production readiness is not established | Verify standalone setup, browser execution, storage, security and deployment |
| [Models by Vectolith](https://github.com/vectolith/Models-by-vectolith.) | Independent model research and model product: specifications, foundation selection, training, evaluation, registry, artifacts and releases | Model-family and training/evaluation infrastructure are documented; no foundation is selected and no student training/release is claimed | Complete legal, teacher, data, human-evaluation and foundation gates before training |
| [Pluco](https://github.com/vectolith/pluco-network) | Standalone digital-ownership protocol and marketplace | Foundry tests and website build evidence exist; configured Base addresses are not deployment proof | Maintain its own contract deployment register, independent security review and marketplace release gates |
| [NYR](https://github.com/vectolith/NYR) | Standalone from-scratch x86-64 operating-system project | Reproducible toolchain, boot validation and early kernel work are documented; it is not a complete general-purpose OS | Continue kernel milestones under its own toolchain and release process |
| VaultETH | Native self-custodial wallet for iOS and Android | Development-stage product; no store release or real-fund approval is claimed | Complete independent wallet security review and physical-device verification of biometric authorization, transaction simulation, key lifecycle and signing |
| Cipher Messenger | Encrypted messaging product | Development-stage client; no managed public homeserver or public release is verified | Operate its own public homeserver and complete device-verification, abuse and security review |
| Quietline Messenger | Encrypted messaging product | Development-stage client; no managed public homeserver or public release is verified | Define its distinct product scope, operate its own public homeserver and complete device-verification and security review |
| AERYN | On-chain generative-art/ERC-721 collection | Contract source and Foundry test work exist; no live deployment or public mint is claimed | Complete contract review, deployment verification, owner-key controls and token metadata review |

## Product independence

Each product is independently responsible for its own architecture, build, tests, runtime, authentication, authorization, storage, secrets, deployment, monitoring, privacy, support and release gates. No product inherits another product's readiness or failure status.

Optional integrations do not change this rule. PLUCO may support standard wallet connections; a user-selected wallet is not required to be a Vectolith product. An application may optionally consume a released model from Models by Vectolith, but the consuming application owns its own adapter, runtime and authorization. Velnor and Blud remain independently operable. Cipher and Quietline remain separate products with independent homeserver configuration and release processes.

## Portfolio status vocabulary

- **Research:** problem, feasibility or architecture investigation; no product capability implied.
- **Prototype:** partial implementation suitable for controlled demonstration; not production approval.
- **Active development:** implementation and tests are progressing; release may still be blocked.
- **Release candidate:** feature scope is frozen and all applicable release gates have evidence.
- **Production:** a named deployment/version is live, monitored, supported and has a reproducible operational record.
- **Paused:** work is intentionally suspended; no active delivery commitment.
- **Archived:** no active maintenance or roadmap.

Do not use "Active" as a substitute for maturity. Record lifecycle stage and release status separately.

## Cross-product dependency policy

No Vectolith product-to-product integration is part of the default architecture or a release requirement. Product-to-product calls, shared credentials, shared databases, shared identity, shared runtime processes and synchronized deployments are prohibited unless separately justified and explicitly approved.

- **Velnor and Blud:** neither product requires the other. Any future browser delegation is an optional integration, not a default dependency.
- **Pluco and wallets:** Pluco may support standard wallet providers. No particular wallet is required.
- **Models by Vectolith and applications:** no application is required to use this model family or its runtime. Any future model consumption must use a product-owned adapter and be independently operable and replaceable.
- **Cipher and Quietline:** separate products with independent identity, homeserver configuration and release processes. No shared runtime or operational service is assumed.

## Maintenance

Update this register when a product is created, archived, renamed, changes owner, changes lifecycle stage or ships a release. Every status change must link to evidence: a commit, test run, deployment record, security review or release artifact. Review the register at least once per release cycle.
