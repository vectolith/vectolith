# Vectolith engineering and release governance

**Baseline:** 2026-11-18  
**Applies to:** All Vectolith-owned and Vectolith-operated repositories, subject to product-specific legal and operational requirements.

This document defines minimum company-wide engineering controls. It does not replace a product's threat model, regulatory obligations, contract audit, or specialist release checklist.

## 1. Governance principles

1. **Evidence over claims.** Distinguish implemented, tested, deployed, monitored, and independently audited capabilities.
2. **Product autonomy with shared contracts.** Projects may use different languages, architectures, runtimes and release cycles. They must honour shared security, provenance, interoperability and reporting requirements.
3. **Fail closed for consequential actions.** Authorization and approval are enforced by trusted runtime code, not model-generated text or UI state.
4. **No fabricated execution receipts.** A system may report success only after receiving and validating evidence from the external system.
5. **Least privilege and isolation.** Credentials, tenant data, signing keys, model artifacts and deployment permissions must be scoped to the minimum required.
6. **Reproducibility.** Builds, evaluations, deployments and releases must identify source revision, configuration and dependencies.
7. **Honest maturity.** A demo, prototype, passing unit test, successful build or configured workflow is not equivalent to production readiness.

## 2. Minimum repository requirements

Every maintained product repository must contain or link to:

- A README with purpose, intended users, scope, current lifecycle stage and known limitations.
- An architecture overview and trust-boundary description.
- A threat model appropriate to its assets and capabilities.
- A security reporting policy and supported-version policy.
- A license/copyright/ownership declaration consistent with company records.
- A dependency and deployment requirements section, including operational dependencies and service limits.
- A test and verification guide with reproducible commands.
- A release checklist and change history.
- A data, privacy and retention description where user data is processed.
- A clear statement of unsupported, simulated, disabled or not-yet-verified functionality.

Research repositories may use a lighter template, but must still document scope, owner, risks, dependencies, and the evidence needed to advance.

## 3. Standard lifecycle gates

A project may move through these gates only when the required evidence is recorded.

### Gate 0 — Classification

- Product/research purpose and user problem are defined.
- Repository owner and legal/IP status are recorded.
- Product boundary and dependencies are identified.
- Lifecycle status is assigned.

### Gate 1 — Specification

- Requirements and non-goals are explicit.
- Architecture, data flows and trust boundaries are documented.
- Threat model and privacy considerations are recorded.
- External services, licenses, operational assumptions and service limits are listed.
- Acceptance criteria are measurable.

### Gate 2 — Implementation

- Changes are traceable to requirements.
- Secrets and private data are not committed.
- Permission checks and validation occur in trusted code.
- Errors, retries, timeouts and partial failures are handled.
- Disabled or simulated capabilities cannot be mistaken for live capabilities.

### Gate 3 — Automated verification

Applicable checks run on every pull request and protected-branch update:

- Formatting, linting, static analysis and type checks.
- Unit and integration tests.
- Security and dependency checks.
- Build/package reproducibility.
- Contract, migration, API-schema or protocol tests where applicable.
- Regression tests for previously fixed defects.

A workflow file existing in the repository is not proof that it ran. Record the actual run URL, commit SHA, result and artifact when relevant.

### Gate 4 — System and integration verification

- Test against real external systems in a controlled environment when feasible.
- Clearly label mocks, simulators and testnets.
- Verify authentication, permissions, tenant boundaries, retries, idempotency and recovery.
- Capture external receipts or chain transaction evidence for consequential operations.
- Verify observability, backup and restore, data retention and rollback.

### Gate 5 — Security and legal review

Review depth must match risk:

- Wallets, custody, signing, smart contracts, identity and sensitive data require specialist review.
- Model training requires dataset provenance, privacy review, license review, output-training permissions, evaluation integrity and holdout protection.
- Agent systems require tool-contract validation, approval boundaries, prompt-injection handling and proof-of-action semantics.
- No self-attestation or automated test suite should be described as an independent audit.

### Gate 6 — Release approval

A release record must identify:

- Product and version.
- Source commit and build artifact digest.
- Configuration and dependency versions.
- Test and security evidence.
- Known limitations and rollback procedure.
- Deployment target and operator.
- Support/maintenance status.

A release is blocked by unresolved critical security issues, contradictory deployment claims, missing legal rights, unverified handling of sensitive assets, or failure of required tests.

### Gate 7 — Operations and maintenance

- Monitor availability, errors, security events and provider failures.
- Maintain backup and recovery procedures.
- Track supported versions, patch deadlines and deprecation.
- Review access, credentials, data retention and third-party dependencies.
- Preserve incident and release records.

## 4. Security baseline

All products must:

- Keep secrets out of source control, prompts, model context, client bundles and logs.
- Encrypt sensitive persisted credentials and restrict decryption to the service that needs them.
- Authenticate webhook and service-to-service requests; validate signatures and freshness where supported.
- Enforce tenant/workspace isolation at the data-access boundary.
- Use TLS for production network traffic.
- Validate external inputs and tool arguments against explicit schemas.
- Apply bounded retries, timeouts, rate limits and idempotency for external actions.
- Require explicit user approval for irreversible or financially consequential actions unless a documented user authorization model safely covers the exact action.
- Record auditable action metadata without storing secrets or unnecessary sensitive payloads.
- Define incident response, vulnerability intake, patch ownership and disclosure procedures.

Projects must document residual risks and exceptions rather than silently weakening the baseline.

## 5. AI model and agent requirements

- The model is not the authorization authority. Runtime policy and trusted code enforce permissions.
- Tool availability, tool schemas and action results must be explicit and validated.
- The system must distinguish proposed, attempted, accepted, completed, failed and unknown action states.
- A timeout after dispatch is an ambiguous outcome, not proof of failure or success. Reconcile before retrying non-idempotent actions.
- Training datasets must have immutable provenance, rights basis, privacy review, deduplication and contamination controls.
- Teacher outputs may be used for training only when the specific model revision, license and output-training permission are verified.
- Evaluation datasets must include protected holdouts; training data must not leak into final evaluation.
- Report quality, safety, calibration, tool reliability, latency, resource use and regression. Training loss alone is insufficient.
- Preserve candidate outputs and revisions where the evaluation protocol requires additive evidence; do not silently discard unfavourable results.

## 6. Smart contract and wallet requirements

For blockchain products:

- Maintain a canonical deployment registry with chain ID, address, deploy transaction, deployer, owner/admin, source commit, compiler settings and verified source status.
- Verify deployed bytecode against the reviewed build.
- Run contract tests in CI, including fuzz/invariant tests where applicable.
- Document upgradeability, admin powers, pause controls, fee/royalty logic and withdrawal paths.
- Treat testnet, local-EVM and mainnet evidence as distinct.
- Wallets must document key generation, storage, recovery, signing, chain validation, transaction simulation and residual memory risks.
- Never represent a simulated transaction, static balance or demo valuation as live chain state.
- Independent security review is required before production claims involving user custody or meaningful user funds.

## 7. CI and pull-request policy

- Work on a named feature branch; do not make unreviewed direct changes to protected release branches.
- PRs must explain intent, scope, tests run, risks and rollback.
- Required CI must be green for the exact PR head commit.
- Do not merge a draft PR or claim readiness from stale CI.
- Keep changes reviewable and avoid combining unrelated product work.
- Pin critical build actions and dependencies where practical.
- Preserve reproducible artifacts and provenance for releases.
- If a check cannot run due to permissions, quota or external dependency, state the exact limitation; do not mark it as passed.

## 8. External dependency register

Each product must identify its external services and operational dependencies, including purpose, authentication boundary, service limits, data exposure, failure behaviour and any viable fallback. Do not assume a service is available or unlimited; verify its actual terms and quotas before relying on it.

## 9. Exceptions and waivers

An exception must state the requirement, reason, affected product/version, risk, compensating control, owner, expiry/review date and approval record. Critical security and legal gates cannot be waived by documentation alone.

## 10. Portfolio review cadence

At least once per release cycle, review:

- Repository inventory and lifecycle status.
- Product boundaries and shared interfaces.
- Open critical/high risks and security advisories.
- CI coverage and latest successful commit.
- Deployment evidence and release support.
- External dependencies, service limits and fallback behaviour.
- Legal ownership, licenses and data rights.
- Duplicated or abandoned repositories.

The portfolio register in `docs/PORTFOLIO_REGISTER.md` is the canonical starting point. Update it when a product, repository, owner, lifecycle stage or deployment status changes.
