# Vectolith product boundaries and ownership

**Applies to:** Vectolith's product and research portfolio  
**Status:** Portfolio architecture baseline; implementation claims are explicitly separated from intended boundaries.

All products in this portfolio are Vectolith products. Each product keeps its own identity, roadmap, architecture, release lifecycle and acceptance criteria. Shared Vectolith standards govern security, privacy, provenance, interoperability and release evidence. Product ownership does not override applicable third-party licenses, contributor rights or copyright notices.

This document defines product responsibilities to reduce accidental duplication. A proposed interface or responsibility is not evidence that an integration has already been implemented.

## 1. Velnor — general-purpose agent platform

**Product responsibility:** General-purpose intelligence orchestration, user and workspace context, integrations, task planning, tool routing, execution coordination, policy enforcement and activity reporting.

- Owns the common agent loop and orchestration contracts.
- Owns channel and service integration contracts, tenant isolation and action lifecycle semantics.
- Owns model-provider and released-model integration behind stable interfaces.
- Its web and mobile companion interfaces are administration and control-centre surfaces for integrations, connection management, activity/execution monitoring, administration, permissions, security and system controls. They are not ordinary chat clients.
- Does not own or subsume the independent NYR kernel research project.
- Velnor OS is out of scope.

## 2. Blud — browser-oriented personal agent

**Product responsibility:** A focused personal-agent product whose distinguishing execution capability is browser automation and browser-session interaction.

- Owns browser-session lifecycle, browser action execution, page observation, browser-specific credential isolation and browser-task evidence.
- Remains a distinct Vectolith product with its own user-facing product identity and release lifecycle.
- When used alongside Velnor, Blud should expose browser execution through a narrow, authenticated capability contract. Velnor may plan and coordinate; Blud performs the browser-specialist work and returns structured execution evidence.
- Browser credentials and secrets must remain outside model context. Browser execution must enforce user authorization and report proposed, attempted, completed, failed or unknown outcomes accurately.
- **Verified implementation gap:** Velnor contains `src/lib/tools/bludBridge.ts`, but Blud's current `app/api/internal/browser-worker/route.ts` initializes the Kernel SDK without executing a browser action and returns a success-shaped response. This is not a working browser integration and must not be treated as one.
- Paired corrective changes are proposed in [Blud PR #3](https://github.com/vectolith/blud/pull/3) and [Velnor PR #33](https://github.com/vectolith/velnor/pull/33). They remove fabricated success, require internal authentication and require a verifiable completion receipt. They deliberately leave the integration unavailable until the actual browser-agent runtime is connected.
- The proposed Velnor–Blud responsibility boundary is a target architecture, not a claim that a production integration exists.

## 3. Models by Vectolith — model ecosystem

**Product responsibility:** Foundation-model evaluation and selection, model-specific specifications, teacher qualification, training-data lineage, training, evaluation, model registry, artifacts and model release lifecycle.

- The model ecosystem is extensible; Core Prime and Core Prima are initial models, not the entire product.
- Each model has its own specialization, objectives, evaluation criteria and release lifecycle while sharing Vectolith identity, behavioural and safety standards, communication/task formats and collaboration protocols.
- Product runtimes such as Velnor remain responsible for authorization, permissions, tool execution and proof of external action.
- No model is considered qualified or released without reproducible evaluation and provenance evidence.
- Model training rights, dataset rights and teacher-output training permissions are separate gates.

## 4. PLUCO Network — digital ownership protocol and marketplace

**Product responsibility:** Base-based digital-ownership protocol, collection registration, minting, marketplace rules, fees/royalties and associated web product surface.

- Owns its smart-contract architecture, deployment registry, protocol economics and marketplace integration.
- Contract deployments are not considered live until chain ID, transaction hashes, deployer, owner/admin roles, source revision, compiler settings, verified source and bytecode match are recorded.
- Website configuration is not proof of deployment.
- PLUCO's release gates are independent from VaultETH's wallet release gates.

## 5. VaultETH — self-custodial wallet

**Product responsibility:** Native iOS and Android self-custodial wallet clients, wallet creation/import, key protection, address derivation, signing, transaction validation, network support and wallet security.

- Owns wallet-specific key lifecycle, signing and recovery behaviour.
- PLUCO may integrate with VaultETH as a wallet or transaction-signing client through explicit, user-approved interfaces; neither product's maturity implies the other's.
- No simulated balance, demo price, disabled signing path or UI-only purchase/swap flow may be represented as a live capability.
- Real-money release requires specialist security review and verified transaction behaviour.

## 6. Cipher Messenger and Quietline Messenger — separate messaging products

Both repositories remain Vectolith products. Their current README files are nearly identical Phase 0 Matrix/Synapse and end-to-end-encryption validation guides; the material difference is the local homeserver name (`cipher.local` versus `quietline.local`). The available documentation does not establish a defensible distinction in target user, threat model, product experience or protocol.

Until each product has an approved specification:

- Keep both repositories and histories intact; do not silently merge, archive or discard either.
- Do not claim either is a released messaging product or that Phase 0 validation proves production E2EE.
- Define separate user problems, threat models, supported clients, device-verification model, homeserver/federation posture, metadata/privacy expectations and release criteria.
- Only after those specifications exist should shared infrastructure or protocol components be considered for reuse.

## 7. AERYN — autonomous intelligence and research synthesis

**Provisional product charter based on the existing portfolio description:** AERYN is a Vectolith autonomous intelligence and deep-research synthesis initiative.

Its first specification must define:
- Intended users and research domains.
- Source discovery, retrieval, provenance and citation requirements.
- Evidence reconciliation, uncertainty handling and contradiction reporting.
- Synthesis outputs, review workflow and export/integration contracts.
- Tool permissions, data handling, privacy, threat model and audit trail.
- Evaluation corpus, quality criteria and release gates.

The repository's current minimal README does not establish that these capabilities are implemented. This charter is a scope definition for specification work, not a capability claim.

## 8. NYR — independent kernel research

NYR is Vectolith's independent x86-64 kernel research project. It owns its kernel architecture, boot process, memory management, interrupt handling, scheduling, drivers and systems-level validation. It is not a Velnor OS initiative, not a dependency of Velnor, and must not be used to expand Velnor's product scope.

## 9. Repository classification

Not every repository is a customer-facing product. Company repositories, internal demos, templates and placeholders are Vectolith-managed portfolio assets and must be classified honestly; third-party licenses and contributor rights remain in force:
- `vectolith` is the company and governance repository.
- `demo-repository` is currently documented as an internal demonstration/template, not a released product.
- `my-project` is currently an unclassified placeholder; no product capabilities should be inferred until its purpose is specified.

## 10. Shared integration contract

Cross-product integrations must define, at minimum:
- Stable versioned request and response schemas.
- Authenticated service identity and least-privilege scopes.
- User/workspace/tenant context with explicit isolation boundaries.
- Idempotency keys and bounded retry semantics for actions.
- Correlation IDs and traceable source revisions.
- Structured action states: proposed, authorized, attempted, accepted, completed, failed or unknown.
- Evidence receipts from the system that performed the action.
- Timeout, cancellation, partial-failure and recovery behaviour.
- Data minimization, retention and deletion expectations.

A product may consume another Vectolith product's capabilities only through an explicit contract. Shared ownership does not imply shared databases, credentials, deployment environments or unrestricted access.
