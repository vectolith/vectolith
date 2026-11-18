# Vectolith portfolio register

**Review baseline:** 2026-11-18  
**Owner:** Vectolith  
**Purpose:** Inventory of independently operated Vectolith products and research initiatives, with evidence-backed maturity and product-specific release gates.

This register is a company portfolio index, not a shared product architecture or dependency map. A repository's presence here does not certify production operation, security, commercial readiness or release status.

## Portfolio principles

- Vectolith is the company and ownership identity. Every product is an independent standalone product with its own purpose, implementation, runtime, identity, data, deployment, operations and release lifecycle.
- No Vectolith product is required to use another Vectolith product. Optional integrations must be opt-in, replaceable and nonessential to core operation.
- Shared company standards cover security, privacy, provenance, accessibility, documentation and evidence quality. They do not create shared services, credentials, databases, deployment systems or synchronized release gates.
- Product maturity is recorded separately from strategic importance.
- Demonstrations, unit tests, CI success, deployment configuration and verified live operation are different evidence types.
- Do not describe a capability as live unless a reproducible test or deployment record establishes it.

## Product and project register

| Repository | Visibility | Independent product purpose | Evidence-backed current position | Main next gate |
|---|---|---|---|---|
| [vectolith](https://github.com/vectolith/vectolith) | Public | Company identity, portfolio index and governance only; not a product runtime | Central README and this register document the independent product portfolio | Maintain company standards and inventory; do not introduce shared runtime dependencies |
| [velnor](https://github.com/vectolith/velnor) | Public | Standalone general-purpose AI agent, integrations and its own execution runtime | Messaging/API surfaces, provider routing, tenant state and operational documentation are present; OCI is identified as current production deployment of record. Blud RPC work is an optional adapter and is not required for Velnor's core operation | Verify live provider delivery, operational observability, retention, global rate limits and independent deployment/release evidence |
| [blud](https://github.com/vectolith/blud) | Public | Standalone personal agent with browser automation and protected credential vault | Browser automation, credential vault and external integrations are documented; README states production readiness is not established and identifies hosting/service constraints. It must remain independently installable and operable without Velnor | Verify standalone setup, browser execution, storage and deployment; remove any Velnor requirement from core workflows |
| [Models-by-vectolith.](https://github.com/vectolith/Models-by-vectolith.) | Public | Standalone model research and model product: specifications, foundation selection, training, evaluation, registry, artifacts and releases | Model-family and training/evaluation infrastructure are documented; no foundation is selected and no student training/release is claimed. Its runtime package is scoped to this repository's own model workflows, not a shared downstream product runtime | Complete legal, teacher, data, human-evaluation and foundation gates before training; document optional model interfaces without requiring consumers |
| [pluco-network](https://github.com/vectolith/pluco-network) | Public | Standalone digital-ownership protocol and marketplace | Foundry tests and website build evidence exist; configured Base addresses must not be represented as deployed contracts without chain verification | Maintain its own contract deployment register, independent security review and marketplace release gates |
| [VaultETH](https://github.com/vectolith/VaultETH) | Private source | Standalone native self-custodial wallet for iOS and Android | Native clients and CI are documented; real-money release gates remain. Web surface is a disposable sandbox; ERC-20 sending is disabled and valuations are demo data | Independent wallet security review, on-device recovery/signing verification, biometric authorization, transaction simulation and platform signing/release checks |
| [NYR](https://github.com/vectolith/NYR) | Public | Standalone from-scratch x86-64 operating-system project | Reproducible toolchain, boot validation, memory management and early SMP/APIC work are documented; README says it is not a complete general-purpose OS | Continue kernel milestones under its own toolchain and release process |
| [Cipher-messenger](https://github.com/vectolith/Cipher-messenger) | Private source | Standalone encrypted messaging product | Phase 0 local Matrix/Synapse E2EE validation plan; not a released messaging product | Establish its own distinct product requirements, threat model, E2EE verification and deployment path |
| [quietline-messenger](https://github.com/vectolith/quietline-messenger) | Private source | Standalone encrypted messaging product | Phase 0 local Matrix/Synapse E2EE validation plan; not a released messaging product. Its current scaffold overlaps Cipher but is not a dependency | Establish its own distinct product requirements, threat model, E2EE verification and deployment path |
| [AERYN](https://github.com/vectolith/AERYN) | Private source | Standalone autonomous intelligence and research synthesis product initiative | Initial product charter is proposed; detailed specification and implementation evidence remain pending | Complete product requirements, architecture, threat model and verification plan |
| [demo-repository](https://github.com/vectolith/demo-repository) | Private | Internal GitHub demonstration/template, not a customer-facing product | README describes a generic demonstration repository | Retain as an internal asset or archive when no longer needed |
| [my-project](https://github.com/vectolith/my-project) | Public | Unclassified placeholder; no product purpose established | README contains only a placeholder line | Define its purpose or archive the placeholder |

## Product independence

Each product is independently responsible for its own architecture, build, tests, runtime, authentication, authorization, storage, secrets, deployment, monitoring, privacy, support and release gates. No product inherits another product's readiness or failure status.

Optional integrations do not change this rule. Velnor may optionally call Blud's browser capability; PLUCO may accept standard wallet connections including VaultETH; and any application may optionally use a released model from Models by Vectolith. None of these relationships is required, and each product must continue to fulfil its core purpose when the integration is disabled or the other product is unavailable.

The [independent product-boundary baseline](PRODUCT_BOUNDARIES.md) defines the required invariants and verification procedure.

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

- **Velnor and Blud:** The Velnor browser delegation tool and adapter have been removed from Velnor. Blud's legacy `/api/internal/browser-worker` endpoint is retired with HTTP 410 because it returned success-shaped responses without real browser execution. Each product continues independently.
- **PLUCO Network and VaultETH:** PLUCO supports external wallet standards and providers. VaultETH is not required; any standards-compliant wallet may be selected by the user.
- **Models by Vectolith and application products:** No application is required to use these models or this repository's runtime. Any future model consumption must use a product-owned adapter and be independently operable and replaceable.
- **Cipher and Quietline:** Separate products with independent repositories, homeserver configuration and release processes. No shared runtime or shared operational service is assumed.

## Maintenance

Update this register when a repository is created, archived, renamed, changes owner, changes lifecycle stage or ships a release. Every status change must link to evidence: a commit, test run, deployment record, security review or release artifact. Review the register at least once per release cycle.
