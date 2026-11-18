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
| [velnor](https://github.com/vectolith/velnor) | Public | General-purpose AI agent platform and integration/runtime layer | Messaging and API surfaces, provider routing, tenant state, operational documentation and automated checks are documented; OCI is identified as current production deployment of record; Velnor PR #33 adds authenticated Blud RPC with a 32-character minimum shared secret, resumable Eve session references and structured extraction; CI passed on head `7d69807bb84d0f92555e2405558f2c52b5bc7bbc` ([run 44294868107](https://github.com/vectolith/velnor/actions/runs/44294868107)). Velnor PR #34 adds fail-closed GitHub webhook HMAC-SHA256 verification primitives and delivery-ID validation; CI passed on head `6fabe4345dab826a3543cf944566749ea7cc2a46` ([run 44294353534](https://github.com/vectolith/velnor/actions/runs/44294353534)); no webhook route or autonomous writes are enabled. | Verify live provider delivery, operational observability, retention, global rate limits and release consolidation |
| [blud](https://github.com/vectolith/blud) | Public | Personal agent and browser-execution product | Browser automation, credential vault and integrations are documented; README explicitly says the software is not intended for production use. Blud PR #3 implements authenticated Velnor-to-Eve session dispatch, service-owned session enforcement, `run_browser` orchestration, structured worker completion, extraction schema/evidence validation and browser-output-bound SHA-256 receipts. Blud CI passed formatting, lint, typecheck, dependency checks and 835 tests across 81 files on head `4d7a859a304b4ba1eb4df7c0ef578db90c7eb0e9` ([run 44295871042](https://github.com/vectolith/blud/actions/runs/44295871042)); Velnor PR #33 preserves Eve session references and validates receipts. Production operation remains unverified until both deployments share the configured service secret, Blud has a valid self API origin and an authorized end-to-end browser task succeeds; private image artifact transport remains unimplemented | Verify deployment configuration and run an authorized end-to-end browser task; resolve production status and scheduled-work dependencies |
| [Models-by-vectolith.](https://github.com/vectolith/Models-by-vectolith.) | Public | Model family, foundation selection, training, evaluation, registry and releases | Extensible family architecture and evaluation/training infrastructure are documented; Models PR #76 Core Prime runtime/evaluation and Vectolith Runtime workflows passed on head `b3c977c72e3ea742682526d8c7ec9979b079a9f9` ([Core Prime run 44283419821](https://github.com/vectolith/Models-by-vectolith./actions/runs/44283419821), [Runtime run 44283419793](https://github.com/vectolith/Models-by-vectolith./actions/runs/44283419793)); no foundation is selected, no teacher is qualified and no student training/release is claimed | Complete legal, teacher, data, human-evaluation and foundation gates before training |
| [pluco-network](https://github.com/vectolith/pluco-network) | Public | Base digital-ownership protocol and marketplace | PLUCO PR #3 adds a no-key public Base RPC verifier. On implementation head `20fb856bd1bbb32ecd0cc8ec5632592c1fcdad24`, 65 Foundry tests passed; all eight manifest transaction receipts, expected destinations/created addresses, and deployed bytecode were verified; all three deployed executable runtimes matched current Foundry artifacts after compiler metadata/immutable slots were normalized; current owner/treasury roles, marketplace registry, fee settings, max supply, mint price, max-per-wallet (3), active registry state, mint/list state and EIP-2981 royalty receiver/rate matched the manifest ([contract + chain verification 44294504204](https://github.com/vectolith/pluco-network/actions/runs/44294504204)); build check passed ([44294504200](https://github.com/vectolith/pluco-network/actions/runs/44294504200)). Explorer verified-source status and independent contract security review remain open | Obtain explorer verified-source status and independent security review |
| [VaultETH](https://github.com/vectolith/VaultETH) | Private | Native self-custodial wallet for iOS and Android | Native clients and CI are documented; real-money limitations are explicit; web surface is a disposable sandbox; ERC-20 sending is disabled and valuations are demo data; VaultETH PR #74 adds SLIP-0010 Solana and BIP-84 Bitcoin derivation, BIP-39 checksum validation, one-time legacy address migration, Gradle 8.13 compatibility and BouncyCastle 1.87. Android unit tests, debug APK build and artifact verification passed on head `6faf00caec6219efaaccfc542410fa00e9e57161` ([run 44293187886](https://github.com/vectolith/VaultETH/actions/runs/44293187886)); iOS unit tests, app build, unsigned IPA packaging and artifact verification passed on the same head ([run 44293187714](https://github.com/vectolith/VaultETH/actions/runs/44293187714)). Artifacts are development builds, not signed/store-ready releases; independent wallet review remains outstanding | Independent wallet security review, on-device recovery/signing verification, biometric authorization, transaction simulation and platform signing/release checks |
| [NYR](https://github.com/vectolith/NYR) | Public | From-scratch x86-64 operating-system kernel research | Reproducible toolchain, boot validation, memory management and early SMP/APIC work are documented; NYR PR #5 CI passed on head `4604be6a03c9dd030b2bd150325f7375930e927a` ([run 44284864923](https://github.com/vectolith/NYR/actions/runs/44284864923)): host memory tests, clean/incremental kernel builds, UEFI ISO verification, QEMU serial boot and development-container image build; README explicitly says this is not a complete general-purpose OS | Continue gated kernel milestones; do not overstate OS completeness |
| [Cipher-messenger](https://github.com/vectolith/Cipher-messenger) | Private | Encrypted messaging research/product candidate | Phase 0 local Matrix/Synapse E2EE validation plan; no custom client is claimed | Prove E2EE and decide product differentiation before client development |
| [quietline-messenger](https://github.com/vectolith/quietline-messenger) | Private | Encrypted messaging research/product candidate | Phase 0 local Matrix/Synapse E2EE validation plan; substantially overlaps Cipher's documented scope | Decide whether it is a distinct product or consolidate the duplicate foundation |
| [AERYN](https://github.com/vectolith/AERYN) | Private | Vectolith autonomous intelligence and research synthesis product | Product charter is proposed in AERYN PR #1; no implementation or release maturity is established | Complete product requirements, architecture, threat model and verification plan |
| [demo-repository](https://github.com/vectolith/demo-repository) | Private | Vectolith-managed internal demonstration/template repository | README describes a generic GitHub demonstration repository; it is not currently classified as a customer-facing product | Retain as internal asset or archive when no longer needed |
| [my-project](https://github.com/vectolith/my-project) | Public | Vectolith-managed placeholder repository; product classification pending | README contains only a placeholder line, so no product purpose or capabilities can yet be established | Define its Vectolith product purpose or archive the placeholder |

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
- **AERYN** is a Vectolith research product; its detailed specification and implementation evidence remain pending.
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
2. **Blud/Velnor integration:** Velnor has an RPC bridge, but Blud's current endpoint fabricates success without browser execution. Paired fail-closed fixes are implemented in Blud PR #3 and Velnor PR #33, with both current PR CI runs passing; the real browser-agent adapter remains unimplemented.
3. **PLUCO deployment evidence:** the manifest records three Base addresses and deployment/marketplace transaction hashes, but no independent chain verification has been established. PLUCO PR #3 aligns both README files with the canonical manifest and adds passing contract CI; independent chain-state verification remains outstanding.
4. **VaultETH company attribution:** identify Vectolith as product owner while preserving accurate copyright authorship and existing proprietary license terms; VaultETH PR #72 makes this attribution change without changing the copyright holder.
5. **Cipher/Quietline differentiation:** their Phase 0 READMEs are nearly identical except for the local server name. Retain both products and define distinct user problems, threat models and product requirements before building separate clients.
6. **AERYN specification gap:** an initial product-charter PR is open; approve a detailed PRD and threat model before implementation or capability claims.
7. **External dependency transparency:** record required services, operational limits, external providers and failure modes per product.

## Maintenance

Update this file whenever a repository is created, archived, renamed, changes owner, changes lifecycle stage, or ships a release. Every status change must link to evidence: a commit, test run, deployment record, security review, or release artifact. Review the register at least once per release cycle.
