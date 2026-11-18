# Vectolith portfolio register

**Review baseline:** 2026-11-18  
**Owner:** Vectolith  
**Purpose:** Canonical index of Vectolith repositories, product boundaries, evidence-backed maturity, and cross-project dependencies.

This register is a snapshot of repository documentation, not a certification of production operation, legal ownership, security, or commercial readiness. A repository's presence in this register does not imply that its product is released.

## Portfolio principles

- Each product owns its implementation, roadmap, release lifecycle, and technical acceptance criteria.
- Shared Vectolith standards govern identity, security, privacy, provenance, interoperability, documentation, and release evidence.
- Product maturity is recorded separately from strategic importance.
- Demonstrations, unit tests, CI success, deployment configuration, and verified live operation are different evidence types.
- Do not describe a capability as live unless a reproducible test or deployment record establishes it.
- Budget constraints are project-specific. The zero-budget constraint for Models by Vectolith is mandatory and must not be silently relaxed.

## Product and project register

| Repository | Visibility | Portfolio role | Evidence-backed current position | Main next gate |
|---|---|---|---|---|
| [vectolith](https://github.com/vectolith/vectolith) | Public | Company identity, portfolio index, shared governance | Central README now provides a portfolio overview; this register remains the detailed canonical inventory | Maintain this register and company-wide standards as the source of truth |
| [velnor](https://github.com/vectolith/velnor) | Public | General-purpose AI agent platform and integration/runtime layer | Messaging and API surfaces, provider routing, tenant state, operational documentation and automated checks are documented; OCI is identified as current production deployment of record | Verify live provider delivery, operational observability, retention, global rate limits and release consolidation |
| [blud](https://github.com/vectolith/blud) | Public | Personal agent and browser-execution product | Browser automation, credential vault and integrations are documented; README explicitly says the software is not intended for production use and requires Vercel Pro for its scheduled-work model | Resolve production status, operating-cost model and relationship to Velnor |
| [Models-by-vectolith.](https://github.com/vectolith/Models-by-vectolith.) | Public | Model family, foundation selection, training, evaluation, registry and releases | Extensible family architecture and evaluation/training infrastructure are documented; no foundation is selected and no student training/release is claimed | Complete legal, teacher, data, human-evaluation and foundation gates before training |
| [pluco-network](https://github.com/vectolith/pluco-network) | Public | Base digital-ownership protocol and marketplace | README lists mainnet contract addresses and deployment date, but later contradicts itself by saying no contracts are deployed; 65 Foundry tests are documented but not in CI | Reconcile deployment evidence and run Foundry tests in CI |
| [VaultETH](https://github.com/vectolith/VaultETH) | Private | Native self-custodial wallet for iOS and Android | Native clients and CI are documented; real-money limitations are explicit; web surface is a disposable sandbox; ERC-20 sending is disabled and valuations are demo data | Independent wallet security review, recovery/signing verification, release and ownership/IP gates |
| [NYR](https://github.com/vectolith/NYR) | Public | From-scratch x86-64 operating-system kernel research | Reproducible toolchain, boot validation, memory management and early SMP/APIC work are documented; README explicitly says this is not a complete general-purpose OS | Continue gated kernel milestones; do not overstate OS completeness |
| [Cipher-messenger](https://github.com/vectolith/Cipher-messenger) | Private | Encrypted messaging research/product candidate | Phase 0 local Matrix/Synapse E2EE validation plan; no custom client is claimed | Prove E2EE and decide product differentiation before client development |
| [quietline-messenger](https://github.com/vectolith/quietline-messenger) | Private | Encrypted messaging research/product candidate | Phase 0 local Matrix/Synapse E2EE validation plan; substantially overlaps Cipher's documented scope | Decide whether it is a distinct product or consolidate the duplicate foundation |
| [AERYN](https://github.com/vectolith/AERYN) | Private | Autonomous intelligence and research synthesis initiative | README currently contains only the project name; architecture and implementation maturity cannot be established from available documentation | Write product charter, architecture, scope, milestones and verification plan |
| [demo-repository](https://github.com/vectolith/demo-repository) | Private | GitHub demonstration/template repository | README describes a generic GitHub demonstration repository, not a Vectolith product | Classify as internal tooling/demo or archive/remove from product portfolio |
| [my-project](https://github.com/vectolith/my-project) | Public | Unclassified placeholder | README contains only a placeholder line | Identify purpose or archive |

## Product boundaries and relationships

The following boundaries are the intended portfolio model. They are architectural direction, not a claim that every integration is implemented.

### Company layer

The Vectolith organization owns shared company identity, security principles, engineering governance, portfolio classification, and cross-product standards.

### Model layer

**Models by Vectolith** owns model specifications, foundation selection, training data lineage, teacher qualification, evaluations, model registry, artifacts, and model releases.

Products may consume released models through stable contracts. Product runtimes remain responsible for authorization, permissions, tenant isolation, tool execution, and audit records. A model's output is never itself proof that an external action occurred.

### Agent and execution products

- **Velnor** is the general-purpose agent platform and integration/runtime product. Its web/mobile companion interfaces are administration and control-centre surfaces, not ordinary chat clients.
- **Blud** is a browser-oriented personal agent and execution product. Its overlap with Velnor must be resolved through explicit capability ownership and integration contracts; do not assume they are already integrated.

### Digital ownership products

- **PLUCO Network** owns the Base digital-ownership protocol and marketplace surface.
- **VaultETH** owns the native self-custodial wallet clients. Wallet security, custody claims, chain support, and release gates are independent from PLUCO marketplace maturity.

### Research initiatives

- **NYR** is low-level OS/kernel research. It is not a Vectolith operating-system platform dependency and must not be used to redefine the scope of other products.
- **AERYN** is an unclassified research initiative until its specification and implementation evidence are published.
- **Cipher Messenger** and **Quietline Messenger** are separate repositories with materially overlapping Phase 0 plans. Their differentiation must be decided before parallel product investment.

## Portfolio status vocabulary

Use these labels consistently:

- **Research:** problem, feasibility or architecture investigation; no product capability implied.
- **Prototype:** partial implementation suitable for controlled demonstration; not production approval.
- **Active development:** implementation and tests are progressing; release may still be blocked.
- **Release candidate:** feature scope is frozen and all applicable release gates have evidence.
- **Production:** a named deployment/version is live, monitored, supported and has a reproducible operational record.
- **Paused:** work is intentionally suspended; no active delivery commitment.
- **Archived:** no active maintenance or roadmap.

Do not use "Active" as a substitute for maturity. Record lifecycle stage and release status separately.

## Known cross-project risks requiring resolution

1. **Portfolio source of truth:** keep the company README synchronized with this detailed register; the register is authoritative when the summary and repository-level documentation differ.
2. **Blud/Velnor overlap:** define which product owns messaging orchestration, browser execution, memory, scheduling, and integration contracts.
3. **PLUCO deployment contradiction:** reconcile the listed Base deployment addresses against the statement that no contracts are deployed. Require chain ID, transaction hashes, deployer/owner, verified source, bytecode match, and deployment commit.
4. **VaultETH ownership:** repository copyright identifies `pluco.dev`, while it is presented as a Vectolith product. Record the legal owner, license authority and any assignment or licence.
5. **Cipher/Quietline duplication:** establish whether the products have distinct threat models, user groups, protocols or product requirements.
6. **AERYN specification gap:** do not represent it as an implemented autonomous research engine until evidence exists.
7. **Cost and dependency transparency:** record required paid tiers, free-tier quotas, external providers and failure modes per product. The Models by Vectolith zero-budget constraint remains absolute for that project.

## Maintenance

Update this file whenever a repository is created, archived, renamed, changes owner, changes lifecycle stage, or ships a release. Every status change must link to evidence: a commit, test run, deployment record, security review, or release artifact. Review the register at least once per release cycle.
