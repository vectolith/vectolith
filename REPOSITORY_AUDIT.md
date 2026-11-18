# Vectolith Repository Engineering Audit

**Audit date:** 2026-11-18  
**Scope:** All 12 repositories accessible under the `vectolith` GitHub account.  
**Audit branch:** `main` (consolidated from `docs/company-wide-portfolio-governance`)  
**Purpose:** Evidence-based implementation and release-readiness review. This report is a point-in-time record, not a certification.

## Executive result

The public-product standard is merged into company governance and eight product repositories. A fresh account-wide GitHub search on 2026-11-18 returned **18 open pull requests** across the 12 repositories after duplicate tracks were consolidated and readiness work was merged. Several repositories still have overlapping or stacked implementation tracks; this is not a one-PR-per-repository programme. Repository visibility settings were not changed.

The audit found multiple real engineering and release blockers. Several have been corrected and verified through GitHub Actions. No repository has a published GitHub release. Cloudflare account inspection found two Workers (`olli` and `velnor-github-ruleset-manager`) and zero Pages projects; neither Worker is verified as a product runtime. Deployments hosted elsewhere were not verified. No product is being represented as production-ready solely because its documentation or CI passes.

## Live recheck — 2026-11-18

### Current open pull-request inventory

| Repository | Open PRs |
|---|---:|
| Velnor | 7 |
| Blud | 3 |
| Models by vectolith | 5 |
| demo-repository | 2 |
| my-project | 1 |
| **Total** | **18** |

### Verified changes and current release gates

- **Company governance:** PR #1 merged. This audit is maintained on the default branch.
- **Cipher Messenger and Quietline Messenger:** readiness PR #2 merged in each repository. Their standalone boundaries, fail-closed E2EE send policy, HTTPS homeserver validation, regression tests and CI are on the default branches. Neither has a verified managed public homeserver or public launch.
- **VaultETH:** readiness PR #75 and Android wallet-security PR #74 are merged. PR #74's exact head passed Android and iOS CI (44365511456 and 44365511605); main-branch Android/iOS CI is still running after merge (44368572674 and 44368572682). Android recovery-phrase reads, legacy cross-chain address derivation and native signing now require fresh strong-biometric-bound Keystore proof in the reviewed source paths. Physical-device security testing, independent review, store identity/URLs, signing and release approval remain outstanding. No real-fund or store-release approval is claimed.
- **Models by vectolith:** readiness PR #78 merged. PRs #73, #75, #76 and #79 remain active tracks. Current evidence includes passing Core Prime runtime/evaluation and Vectolith Runtime checks on #76, and passing runtime/evaluation checks on #79. Teacher qualification, legal/provenance review, independent human adjudication, protected holdout evidence and training authorization remain release gates.
- **PLUCO Network:** readiness PR #4 and separately versioned V2 successor PR #10 merged. Main-branch contract verification run 44364688447 passed **91 Foundry tests**, verifier syntax checks and public Base RPC checks. The verifier confirmed all eight manifest transactions, three deployed V1 executable runtimes against Foundry artifacts, ownership/treasury/fee/supply/mint-price/registry/royalty state. V2 remains source-only and undeployed. V1 has documented immutable-contract limitations; independent specialist review and explorer source verification remain outstanding.
- **Blud:** standalone-boundary PR #6 merged; main CI 44364193704 passed. The fake browser-worker endpoint and Velnor bridge were removed; Blud no longer requires Velnor for core operation. PR #8 adds proxy/session security, dashboard regression coverage and CI repairs; its only initial failure was formatting in `tests/proxy.test.ts`, which was corrected with the repository formatter, and the current CI rerun is pending. Draft PRs #1 and #2 remain stacked on an unmerged architecture branch and require separate security, account-lifecycle and functionality review. PRs #3 and #7 were closed as rejected/superseded tracks.
- **Velnor:** standalone-boundary PR #37, platform-architecture PR #38 and reminder-claim PR #39 merged; main production CI passed after each merge. The Blud bridge PR #33, synthetic-curriculum PR #23, unused GitHub-webhook-helper PR #34, older reminder-claim PR #26 and provider-policy PR #25 were closed. PR #32 is now the consolidated mainline candidate for the messaging stack (including the former #27–#30 dependencies) and is under full production CI. It removes the Blud runtime bridge, includes durable task execution, Discord/iMessage identities, Twilio/Sendblue channels, provider callbacks, SQLite attempt tracking and duplicate-send guards. PR #31's SMS-downgrade and LoopMessage delivery fixes were ported into #32; PR #31 itself has passing CI but remains a parallel stack. PR #35 remains a draft partial async-storage migration. The explicit-provider misconfiguration gap from closed PR #25 remains open in main: an explicitly selected but unconfigured provider must not silently fall through to the built-in orchestrator.
- **AERYN:** standalone and contract-verification PR #5 merged. Main contract CI run 44364331741 passed. It remains an owner-minted ERC-721 source project; no live deployment, public mint or independent contract audit is claimed.
- **NYR:** hardening PR #5 merged after passing host memory, clean/incremental build, ELF/ISO and QEMU validation. Standalone documentation PR #7 was closed unmerged by the repository owner. OS release and broad hardware compatibility are not claimed.
- **demo-repository:** the HTML proof workflow passed. The issue auto-assignment correction still needs a real issue-open event test. It remains an internal demonstration, not a Vectolith public product.
- **my-project:** no product build or deployable application is declared. It remains an unclassified placeholder and must not be counted as a viable public product.

### Current dependency and failure details

- Velnor reminder dispatch: PR #39 is merged. It claims reminders in a SQLite `BEGIN IMMEDIATE` transaction, uses a bounded lease and marks claims terminal only after state persistence. It prevents overlapping workers, but a process crash after an external provider accepts a send and before state persistence can still cause at-least-once duplicate delivery. Do not claim exactly-once external delivery until provider idempotency/outbox tracking is integrated.
- Velnor messaging: PR #32 is now the consolidated candidate on main and includes the former #27/#28/#30 stack plus PR #31's critical delivery safeguards. Its exact-head CI must pass before merge. Automatic retries must not resend while an attempt is pending, queued, processing or delivered. Ambiguous outcomes—including Sendblue SMS downgrade—require explicit, provider-reconciled retry authorization.
- Velnor provider selection: explicit provider selection must be preserved. If a selected provider lacks credentials, return a configuration error; do not silently substitute another provider or the built-in orchestrator. The attempted fix in PR #25 was closed before merge, so this remains an open implementation gap.
- Blud: PR #8 is the active quality/security candidate; its exact-head CI result must be green before merge. PRs #1 and #2 are stacked on an unmerged architecture branch and must not be merged independently of that base.
- Models by vectolith: do not treat passing runtime/evaluation CI as teacher qualification or training authorization. Candidate responses and evaluation evidence must remain immutable, rights-cleared and independently adjudicated.

### Dependency and architecture decisions

- The Velnor-to-Blud browser integration is not part of the default architecture. Any future cross-product adapter requires explicit approval and must remain optional and removable without impairing either product.
- PLUCO V1 remains immutable. Security fixes are introduced as separately versioned successors; V2 has not been deployed or authorized for migration.
- Do not merge draft PRs, stacked PRs, or PRs with failing/conflicting checks merely because GitHub reports a mergeable branch.
- A green CI run verifies only the checks that actually ran on that exact commit. It does not replace physical-device testing, independent security review, legal review, or production deployment verification.

## Repository findings and current evidence

| Repository | Product classification | Implemented in this audit | Current evidence / remaining blocker |
|---|---|---|---|
| [Cipher-messenger](https://github.com/vectolith/Cipher-messenger) | Early Matrix encrypted-messaging client | Secure homeserver URL validation; removed silent localhost production fallback; local secret/state ignores; required local Postgres secret; loopback-only dev homeserver port; active-room event reference and UI error handling; accessible room controls; locked npm dependencies; CI | Build and production-dependency audit passed. Full audit still reports an upstream dev-tooling advisory for picomatch with no published fix. No managed public homeserver or public deployment verified. |
| [quietline-messenger](https://github.com/vectolith/quietline-messenger) | Early Matrix encrypted-messaging client | Same security, local-stack, UX, dependency, and CI remediation as Cipher | Build and production-dependency audit passed. Same unpatched dev-only picomatch advisory. No managed public homeserver or public deployment verified. |
| [VaultETH](https://github.com/vectolith/VaultETH) | Self-custodial iOS and Android wallet | Reworked privacy disclosures across the policy, hosted HTML, iOS privacy screen, Android settings, support pages, and store submission kit; removed synthetic portfolio-return percentages; clearly separated live native balances from demo holdings/prices and illustrative charts; corrected the Android Gradle wrapper to an AGP-compatible version; corrected an Android authorization test vector in the separate security PR | Latest readiness-branch iOS and Android CI both passed (runs 44351487979 and 44351487610). Separate wallet-security PR #74 also passed Android and iOS workflows on its exact head. These are development artifacts, not signed store releases. Store URLs/legal identity, physical-device security, on-device recovery/signing and provider-specific data-safety declarations remain unverified; no store release is claimed. ERC-20 sends, swaps, purchases, and Solana/Bitcoin sends remain unavailable. |
| [AERYN](https://github.com/vectolith/AERYN) | Owner-minted on-chain ERC-721 artwork | Added accurate product/deployment documentation, Foundry CI, and tests for owner-only minting, on-chain metadata, and max supply | Foundry build and tests passed. Contract remains owner-mint only; no production chain deployment or public mint is claimed. |
| [demo-repository](https://github.com/vectolith/demo-repository) | Demonstration repository, not a production product | Corrected issue auto-assignment workflow so it runs on issue-open events only and removed unsupported action input | Proof HTML CI passed. Keep this repository explicitly classified as a demonstration, not a deployable Vectolith product. |
| [pluco-network](https://github.com/vectolith/pluco-network) | Digital-art and marketplace web product | Capped externally supplied ERC-2981 royalties after protocol fee reservation; rejected zero-address treasury/registry destinations; added settlement and payout regression tests; added Foundry CI | Frontend build and Foundry contract verification passed. Mainnet deployment, deployed contract addresses, and live settlement remain unverified. |
| [vectolith](https://github.com/vectolith/vectolith) | Vectolith portfolio/profile repository | Reconciled product descriptions and status claims with the actual repositories; linked the shared standard | No application CI is applicable to this profile-only repository. Product release/deployment evidence belongs in each product repository. |
| [blud](https://github.com/vectolith/blud) | Headless personal AI assistant and browser automation product | Added security disclosure policy; restored the missing Tailwind CSS entry point; formatted legacy dashboard/UI files flagged by CI; corrected Knip's dependency inventory and replaced untyped auth mocks with Better Auth domain types; consolidated work in PR #7 on the browser-worker execution-boundary prerequisite | Current PR #3 and #7 CI runs fail at the formatting gate; PR #6 also fails because 13 existing dashboard/UI files are not formatted. The PR #3 browser-execution bridge conflicts with PR #6's standalone direction to remove the Velnor-facing bridge, and PR #7 is stacked on PR #3. Velnor PR #33 depends on Blud #3 while Velnor #37 removes that coupling. Resolve this architecture conflict before selecting a merge path. Hosted setup documents Vercel Pro and paid/usage-billed integrations; it is not a verified zero-cost public deployment. |
| [velnor](https://github.com/vectolith/velnor) | Multi-provider AI agent platform | Added security disclosure policy and shared product baseline; reviewed tenant-token validation, gateway authentication, request-size limits, and tenant provisioning boundaries | Velnor Production CI passed on PR #37 head (run 44350677194). The connected Cloudflare account currently has two Workers (olli and velnor-github-ruleset-manager) and zero Pages projects; neither Worker is verified as Velnor's product runtime. Other hosting providers, production domains, secrets and live integrations were not verified. |
| [NYR](https://github.com/vectolith/NYR) | Experimental kernel/operating-system project | Migrated heap, scheduler, and console locking to IRQ-safe operations; added physically contiguous frame allocation/free; implemented multi-page heap allocations for real task stacks; added contiguous-frame and 16 KiB heap regression tests; fixed the CI snapshot fallback environment handoff | NYR PR #5 passed its full host memory tests, clean/incremental builds, ELF/ISO verification and four-vCPU QEMU boot checks on exact head 3141c4e3fc467230760e0cd1945a34343584e62e (run 44352740036). The older main-based standalone-doc PR #7 still inherits main-branch host-test failures; do not merge it ahead of PR #5. No OS release or broad hardware compatibility claim is made. |
| [my-project](https://github.com/vectolith/my-project) | Development workspace; no deployable product declared | Removed tracked local Antigravity chat/relay state from the readiness branch; added ignore rules and clarified repository purpose | No product build or deployment is declared. Deleting files in the PR does not erase their earlier Git history. |
| [Models-by-vectolith.](https://github.com/vectolith/Models-by-vectolith.) | Independent model ecosystem and Core Prime evaluation/runtime project | Added shared standard and security policy; removed duplicate runtime-only CI workflow because the consolidated runtime-and-evaluation workflow runs both test suites | Runtime and evaluation CI passed. Model training, teacher qualification, data provenance, and release readiness remain governed by their separate evidence pipeline; no public model release is claimed here. |

## Cross-repository security and quality observations

- Targeted code searches did not reveal an obvious committed live API key or private-key literal in the sampled product code and configuration. This is not a substitute for GitHub secret-scanning alerts or a full historical secret scan.
- Example environment files contain placeholders and public configuration values. Real secrets must remain in local ignored files or protected deployment secret stores.
- Cipher and Quietline previously lacked ignore rules for Synapse data and generated signing keys. The readiness branch now excludes those local artifacts and requires a non-default Postgres password.
- Cipher and Quietline now gate the production dependency tree. Their full development dependency inventory still reports an upstream picomatch advisory with no published patched release as of this audit date. The affected package is in the Vite development toolchain; it is not being suppressed as a production dependency vulnerability.
- No GitHub releases were found for any of the 12 repositories (rechecked against each repository's releases endpoint on 2026-11-18).
- Cloudflare account inspection found two Workers (olli, velnor-github-ruleset-manager) and zero Pages projects. Neither Worker is verified as a Velnor product runtime. This does not establish whether another hosting provider is in use.

## Pull requests

The standard and repository-specific changes are proposed through these open pull requests:

- [Cipher-messenger #2](https://github.com/vectolith/Cipher-messenger/pull/2)
- [quietline-messenger #2](https://github.com/vectolith/quietline-messenger/pull/2)
- [VaultETH #75](https://github.com/vectolith/VaultETH/pull/75)
- [AERYN #2](https://github.com/vectolith/AERYN/pull/2)
- [demo-repository #3](https://github.com/vectolith/demo-repository/pull/3)
- [pluco-network #4](https://github.com/vectolith/pluco-network/pull/4)
- Company governance and public-product standards: [vectolith #1 — merged](https://github.com/vectolith/vectolith/pull/1)
- [blud #7](https://github.com/vectolith/blud/pull/7)
- [velnor #36](https://github.com/vectolith/velnor/pull/36)
- [NYR #6](https://github.com/vectolith/NYR/pull/6)
- [my-project #1](https://github.com/vectolith/my-project/pull/1)
- [Models-by-vectolith. #78](https://github.com/vectolith/Models-by-vectolith./pull/78)

## Related product-specific remediation pull requests

These are separate, active implementation tracks that must be reviewed alongside the baseline PRs:

- Cipher Messenger: fail-closed E2EE, HTTPS homeserver validation and standalone product boundaries are consolidated into [#2](https://github.com/vectolith/Cipher-messenger/pull/2); duplicate PRs #1, #3 and #4 are closed.
- Quietline Messenger: fail-closed E2EE, HTTPS homeserver validation and standalone product boundaries are consolidated into [#2](https://github.com/vectolith/quietline-messenger/pull/2); duplicate PRs #1, #3 and #4 are closed.
- VaultETH: [#74 Android wallet derivation/security gates](https://github.com/vectolith/VaultETH/pull/74), [#76 standalone wallet boundary](https://github.com/vectolith/VaultETH/pull/76).
- AERYN: [#3 ERC-721 tests and CI](https://github.com/vectolith/AERYN/pull/3), [#4 independent on-chain art product](https://github.com/vectolith/AERYN/pull/4).
- PLUCO: [#6 hardened marketplace and Originals V2](https://github.com/vectolith/pluco-network/pull/6), [#7 standalone setup instructions](https://github.com/vectolith/pluco-network/pull/7).
- Blud: [#3 browser execution boundary](https://github.com/vectolith/blud/pull/3), [#6 remove legacy Velnor bridge](https://github.com/vectolith/blud/pull/6), [#7 public standard and quality fixes](https://github.com/vectolith/blud/pull/7).
- Velnor: [#33 verified browser-delegation receipts](https://github.com/vectolith/velnor/pull/33), [#37 remove Blud coupling](https://github.com/vectolith/velnor/pull/37).
- NYR: [#5 heap allocator repair](https://github.com/vectolith/NYR/pull/5), [#7 independent OS project boundary](https://github.com/vectolith/NYR/pull/7).
- Models by vectolith: [#76 independent Core Prime candidate pipeline](https://github.com/vectolith/Models-by-vectolith./pull/76), [#79 remove shared-runtime assumptions](https://github.com/vectolith/Models-by-vectolith./pull/79).

## Live recheck — 2026-11-18 18:20 +01:00

### Pull-request inventory

The current global search returns **51 open PRs** after consolidating eight duplicate identity, standalone-boundary, E2EE and company-portfolio PRs and merging the company governance PR:

| Repository | Open PRs |
|---|---:|
| Velnor | 17 |
| Models by vectolith | 6 |
| VaultETH | 6 |
| Blud | 5 |
| PLUCO Network | 4 |
| NYR | 4 |
| AERYN | 4 |
| Cipher Messenger | 1 |
| Quietline Messenger | 1 |
| Vectolith company repository | 0 |
| demo-repository | 2 |
| my-project | 1 |
| **Total** | **51** |

### Current CI evidence and blockers

- **Models by vectolith:** PR #73 runtime/evaluation and Vectolith Runtime checks passed; PR #76 runtime/evaluation and Vectolith Runtime checks passed. Teacher qualification, legal rights, human adjudication, foundation selection, protected holdout and training authorization remain open gates. PR #79 requires its own final CI result.
- **VaultETH:** PR #74 now enforces a fresh strong-biometric Keystore proof at the SecureVault mnemonic-read boundary, gates recovery-phrase viewing and legacy receive-address re-derivation, and removes automatic startup mnemonic reads. Android and iOS CI on the updated head are running (44360757869 and 44360757983); prior readiness-branch Android/iOS workflows passed. No signed store release or real-fund approval is established.
- **PLUCO Network:** PR #6 frontend build and Foundry contract tests passed (91 tests); PR #7 standalone documentation build passed. V2 is a source proposal, not a deployment. V1 independent security review, source verification and migration/operations decisions remain open.
- **Blud:** PR #3 and #7 currently fail formatting checks; PR #6 fails formatting on 13 files. The #3/#6 architecture conflict and #7's stacked base must be resolved before merge.
- **Velnor:** PR #37 standalone-boundary CI passed. PR #33 is an optional Blud bridge track that conflicts with the newer no-coupling direction in #37. Several older delivery PRs are stacked on one another and require dependency-aware review.
- **NYR:** PR #5 passed full host, build, ISO and QEMU validation. PR #7 is based on main and must be rebased/retested after the heap/scheduler repair is integrated.
- **Cipher Messenger and Quietline Messenger:** Vectolith product identity, standalone ownership, fail-closed E2EE policy, HTTPS homeserver validation, regression tests and CI checks are consolidated into each repository's readiness PR #2. Final CI passed on the code/security heads (Cipher 44359914657; Quietline 44360006867); duplicate product-identity PR #1, E2EE PR #3 and standalone README PR #4 were closed in each repository. README-only updates since those runs are awaiting the next CI result. They still lack verified public homeserver deployments and independent public launch evidence.
- **AERYN:** contract CI and Foundry tests passed on PR #3. No mainnet deployment or public mint is claimed.
- **demo-repository:** HTML proof workflow passed. The latest auto-assignment failure was caused by the main-branch workflow also triggering on pull requests and passing an unsupported action input; the readiness branch corrects both by restricting the trigger to newly opened issues and removing the unsupported input. The corrected issue-event path still needs a real issue-open event test. It remains an internal demonstration.
- **Vectolith company repository:** documentation/governance only; no application CI is applicable.
- **my-project:** no product build is declared; it remains an unclassified placeholder.

### Merge and dependency observations

- All 60 open PRs were initially enumerated and metadata-inspected; eight duplicate identity, standalone-boundary, E2EE and company-portfolio PRs were consolidated and closed, and company governance PR #1 was merged, leaving 51 open. PR metadata was inspected for base branch, head branch, head SHA, draft state, GitHub mergeability, update time and changed-file count.
- GitHub's mergeable=true is only a conflict signal; it is not approval, passing CI, semantic compatibility or release readiness.
- Blud #7 is stacked on #3, while #6 proposes removing the bridge. Velnor #33 depends on #3, while #37 removes the dependency. Treat these as conflicting architectural tracks, not independently mergeable changes.
- Velnor #27, #28, #30, #31 and #32 form a stacked delivery chain; #29 and #30 currently report merge conflicts. PRs #23 and #21 also report merge conflicts and need rebase/review before acceptance.
- VaultETH #70 (Gradle 9.9.1) is explicitly superseded by the compatible Gradle 8.13 correction in #74; #71's BouncyCastle upgrade is already integrated into #74; #72's attribution changes overlap #74. Do not merge these dependency/documentation PRs independently.
- Several baseline PRs are draft or documentation-only. Do not mark them production approval; merge only after product-specific review and the relevant required checks.

## Release gates still open

1. Wait for and resolve the current VaultETH Android/iOS, Blud, and NYR CI runs. Do not merge failing or unverified code.
2. Complete a product-specific security and privacy review for each deployed service, including production secrets, access controls, third-party processors, backups, and incident response.
3. Verify actual deployment targets, domains, TLS, health checks, monitoring, rollback, and production configuration. A green build is not deployment evidence.
4. Resolve Blud's hosted-service cost and provider dependencies before representing its current deployment model as zero-cost.
5. Provision and test real public Matrix homeservers before launching Cipher or Quietline to public users.
6. Verify AERYN and PLUCO contract addresses, source verification, ownership, treasury configuration, and chain-specific operational controls before announcing live blockchain functionality.
7. Complete VaultETH transaction authorization, physical-device testing, store privacy declarations, and store review before a public wallet release.
8. Maintain immutable model/data provenance and human evaluation evidence before any Models by Vectolith model release.
9. Require passing CI, a reviewed release checklist, and a tested rollback path for every future public release.

**Status:** Company governance, public-product standard, repository audit and product-boundary policy are merged into the Vectolith company repository's main branch. Product-specific remediation remains in its own repositories and pull requests. Repository-wide production readiness is not yet achieved or certified.
