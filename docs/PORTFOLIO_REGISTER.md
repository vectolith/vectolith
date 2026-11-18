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
| [velnor](https://github.com/vectolith/velnor) | Public | Standalone general-purpose AI agent, integrations and its own execution runtime | Messaging/API surfaces, provider routing, tenant state and operational documentation are present; The README identifies OCI as the current production deployment of record; live deployment health and provider operation have not been independently verified. The standalone boundary is proposed in Velnor PR #37 and Blud PR #6. Until those changes are merged, the default branches still contain legacy coupling; the Blud bridge must not become a required dependency | Verify live provider delivery, operational observability, retention, global rate limits and independent deployment/release evidence |
| [blud](https://github.com/vectolith/blud) | Public | Standalone personal agent with browser automation and protected credential vault | Browser automation, credential vault and external integrations are documented; README states production readiness is not established and identifies hosting/service constraints. It must remain independently installable and operable without Velnor | Verify standalone setup, browser execution, storage and deployment; remove any Velnor requirement from core workflows |
| [Models-by-vectolith.](https://github.com/vectolith/Models-by-vectolith.) | Public | Standalone model research and model product: specifications, foundation selection, training, evaluation, registry, artifacts and releases | Model-family and training/evaluation infrastructure are documented; no foundation is selected and no student training/release is claimed. Its runtime package is scoped to this repository's own model workflows, not a shared downstream product runtime | Complete legal, teacher, data, human-evaluation and foundation gates before training; document optional model interfaces without requiring consumers |
| [pluco-network](https://github.com/vectolith/pluco-network) | Public | Standalone digital-ownership protocol and marketplace | Foundry tests and website build evidence exist; configured Base addresses must not be represented as deployed contracts without chain verification | Maintain its own contract deployment register, independent security review and marketplace release gates |
| [VaultETH](https://github.com/vectolith/VaultETH) | Private source; public product development | Standalone native self-custodial wallet for iOS and Android | Native clients and CI are documented; real-money release gates remain. Web surface is a disposable sandbox; ERC-20 sending is disabled and valuations are demo data | Independent wallet security review and physical-device verification of the biometric authorization, transaction simulation, key-material lifecycle and platform signing/release controls |
| [NYR](https://github.com/vectolith/NYR) | Public | Standalone from-scratch x86-64 operating-system project | Reproducible toolchain, boot validation, memory management and early SMP/APIC work are documented; README says it is not a complete general-purpose OS | Continue kernel milestones under its own toolchain and release process |
| [Cipher-messenger](https://github.com/vectolith/Cipher-messenger) | Private source; public product development | Standalone encrypted messaging product | Early Matrix client implementation; fail-closed E2EE sends and HTTPS homeserver validation are in CI-tested development branches; no managed public homeserver or release is verified | Provision and operate its own public homeserver, complete device-verification and abuse controls, and pass product security review |
| [quietline-messenger](https://github.com/vectolith/quietline-messenger) | Private source; public product development | Standalone encrypted messaging product | Early Matrix client implementation; fail-closed E2EE sends and HTTPS homeserver validation are in CI-tested development branches; no managed public homeserver or release is verified | Provision and operate its own public homeserver, complete device-verification and abuse controls, and pass product security review |
| [AERYN](https://github.com/vectolith/AERYN) | Private source; public collection development | Standalone on-chain generative-art/ERC-721 collection | `AerynOnChain721.sol` defines a 100-token owner-minted collection with on-chain SVG metadata; deployment script exists, but no live Base deployment evidence is recorded | Complete contract tests, deployment verification, owner/key controls and token metadata review |
| [demo-repository](https://github.com/vectolith/demo-repository) | Private | Internal GitHub demonstration/template, not a customer-facing product | README describes a generic demonstration repository | Retain as an internal asset or archive when no longer needed |
| [my-project](https://github.com/vectolith/my-project) | Public | Unclassified placeholder; no product purpose established | README contains only a placeholder line | Define its purpose or archive the placeholder |

## Product independence

Each product is independently responsible for its own architecture, build, tests, runtime, authentication, authorization, storage, secrets, deployment, monitoring, privacy, support and release gates. No product inherits another product's readiness or failure status.

Optional integrations do not change this rule. PLUCO may accept standard wallet connections including VaultETH; and any application may optionally use a released model from Models by Vectolith. No Velnor-to-Blud bridge is approved as a default dependency. None of these relationships is required, and each product must continue to fulfil its core purpose when an integration is disabled or another product is unavailable.

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

- **Velnor and Blud:** The Velnor browser delegation tool and adapter are being removed in Velnor PR #37; Blud's legacy `/api/internal/browser-worker` endpoint is being removed in Blud PR #6 because it returned success-shaped responses without real browser execution. These changes are not yet merged into the default branches. Each product must continue independently.
- **PLUCO Network and VaultETH:** PLUCO supports external wallet standards and providers. VaultETH is not required; any standards-compliant wallet may be selected by the user.
- **Models by Vectolith and application products:** No application is required to use these models or this repository's runtime. Any future model consumption must use a product-owned adapter and be independently operable and replaceable.
- **Cipher and Quietline:** Separate products with independent repositories, homeserver configuration and release processes. No shared runtime or shared operational service is assumed.

## Maintenance

Update this register when a repository is created, archived, renamed, changes owner, changes lifecycle stage or ships a release. Every status change must link to evidence: a commit, test run, deployment record, security review or release artifact. Review the register at least once per release cycle.
