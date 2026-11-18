# Vectolith portfolio register

**Review baseline:** 2026-11-18  
**Owner:** Vectolith  
**Purpose:** Canonical index of Vectolith repositories, product boundaries, evidence-backed maturity, and cross-project dependencies.

This register is the company portfolio index for Vectolith-owned products and initiatives. It is a snapshot of repository documentation, not a certification of production operation, security, or commercial readiness. A repository's presence in this register does not imply that its product is released.

## Portfolio principles

- Vectolith owns the portfolio and its products. Each product retains its own implementation, roadmap, release lifecycle, and technical acceptance criteria.
- Shared Vectolith standards govern identity, security, privacy, provenance, interoperability, documentation, and release evidence.
- Product maturity is recorded separately from strategic importance.
- Demonstrations, unit tests, CI success, deployment configuration, and verified live operation are different evidence types.
- Do not describe a capability as live unless a reproducible test or deployment record establishes it.

## Product and project register

| Repository | Visibility | Portfolio role | Evidence-backed current position | Main next gate |
|---|---|---|---|---|
| [vectolith](https://github.com/vectolith/vectolith) | Public | Company identity, portfolio index, shared governance | Central README now provides a portfolio overview; this register remains the detailed canonical inventory | Maintain this register and company-wide standards as the source of truth |
| [velnor](https://github.com/vectolith/velnor) | Public | General-purpose AI agent platform and integration/runtime layer | Messaging and API surfaces, provider routing, tenant state, operational documentation and automated checks are documented; OCI is identified as current production deployment of record | Verify live provider delivery, operational observability, retention, global rate limits and release consolidation |
| [blud](https://github.com/vectolith/blud) | Public | Personal agent and browser-execution product | Browser automation, credential vault and integrations are documented; README explicitly says the software is not intended for production use. The internal browser-worker route currently returns success without executing browser actions; fail-closed correction is proposed in Blud PR #3 | Resolve production status, scheduled-work dependencies and relationship to Velnor |
| [Models-by-vectolith.](https://github.com/vectolith/Models-by-vectolith.) | Public | Model family, foundation selection, training, evaluation, registry and releases | Extensible family architecture and evaluation/training infrastructure are documented; no foundation is selected and no student training/release is claimed | Complete legal, teacher, data, human-evaluation and foundation gates before training |
| [pluco-network](https://github.com/vectolith/pluco-network) | Public | Base digital-ownership protocol and marketplace | root README now records a deployment manifest at `contracts/art/deployments/base.json` with Base addresses and transaction hashes, but chain execution, bytecode, and current owner/treasury state remain independently unverified; contracts README correction is proposed in PLUCO PR #3; 65 Foundry tests are documented but not in CI | Reconcile deployment evidence and run Foundry tests in CI |
| [VaultETH](https://github.com/vectolith/VaultETH) | Private | Native self-custodial wallet for iOS and Android | Native clients and CI are documented; real-money limitations are explicit; web surface is a disposable sandbox; ERC-20 sending is disabled and valuations are demo data | Independent wallet security review, recovery/signing verification and release gates |
| [NYR](https://github.com/vectolith/NYR) | Public | From-scratch x86-64 operating-system kernel research | Reproducible toolchain, boot validation, memory management and early SMP/APIC work are documented; README explicitly says this is not a complete general-purpose OS | Continue gated kernel milestones; do not overstate OS completeness |
| [Cipher-messenger](https://github.com/vectolith/Cipher-messenger) | Private | Encrypted messaging research/product candidate | Phase 0 local Matrix/Synapse E2EE validation plan; no custom client is claimed | Prove E2EE and decide product differentiation before client development |
| [quietline-messenger](https://github.com/vectolith/quietline-messenger) | Private | Encrypted messaging research/product candidate | Phase 0 local Matrix/Synapse E2EE validation plan; substantially overlaps Cipher's documented scope | Decide whether it is a distinct product or consolidate the duplicate foundation |
| [AERYN](https://github.com/vectolith/AERYN) | Private | Autonomous intelligence and research synthesis initiative | initial product-charter PR is open; no implementation or release maturity is established | Write product charter, architecture, scope, milestones and verification plan |
| [demo-repository](https://github.com/vectolith/demo-repository) | Private | GitHub demonstration/template repository | README describes a generic GitHub demonstration repository, not a Vectolith product | Classify as internal tooling/demo or archive/remove from product portfolio |
| [my-project](https://github.com/vectolith/my-project) | Public | Unclassified placeholder | README contains only a placeholder line | Identify purpose or archive |

## Product boundaries and relationships

See the [Vectolith product-boundary baseline](PRODUCT_BOUNDARIES.md) for explicit ownership, responsibilities and integration contracts. The boundaries are architectural direction, not a claim that every integration is implemented.

### Company layer

All products in this portfolio are Vectolith products. The company layer maintains identity, security principles, engineering governance, portfolio classification and cross-product standards. Product ownership does not override applicable third-party licenses, contributor rights or copyright notices.

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
2. **Blud/Velnor integration:** Velnor has an RPC bridge, but Blud's current endpoint fabricates success without browser execution. Paired fail-closed fixes are proposed in Blud PR #3 and Velnor PR #33; the real browser-agent adapter remains unimplemented.
3. **PLUCO deployment evidence:** the manifest records three Base addresses and deployment/marketplace transaction hashes, but no independent chain verification has been established. PLUCO PR #3 aligns the contracts guide with the canonical manifest; chain-state verification and contract CI remain outstanding.
4. **VaultETH company attribution:** identify Vectolith as product owner while preserving accurate copyright authorship and existing proprietary license terms; do not change a copyright holder without a documented rights assignment.
5. **Cipher/Quietline differentiation:** their Phase 0 READMEs are nearly identical except for the local server name. Retain both products and define distinct user problems, threat models and product requirements before building separate clients.
6. **AERYN specification gap:** an initial product-charter PR is open; approve a detailed PRD and threat model before implementation or capability claims.
7. **External dependency transparency:** record required services, operational limits, external providers and failure modes per product.

## Maintenance

Update this file whenever a repository is created, archived, renamed, changes owner, changes lifecycle stage, or ships a release. Every status change must link to evidence: a commit, test run, deployment record, security review, or release artifact. Review the register at least once per release cycle.
