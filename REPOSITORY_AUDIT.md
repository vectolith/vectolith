# Vectolith Repository Engineering Audit

**Audit date:** 2026-11-18  
**Scope:** All 12 repositories accessible under the `vectolith` GitHub account.  
**Audit branch:** `standards/public-product-readiness`  
**Purpose:** Evidence-based implementation and release-readiness review. This report is a point-in-time record, not a certification.

## Executive result

The shared public-product standard is present on a dedicated branch in all 12 repositories, with one corresponding open pull request per repository. Repository visibility settings were not changed.

The audit found multiple real engineering and release blockers. Several have been corrected and verified through GitHub Actions. No repository has a published GitHub release. Cloudflare account inspection found no Pages projects and no Velnor-specific Worker; deployments hosted elsewhere were not verified. No product is being represented as production-ready solely because its documentation or CI passes.

## Repository findings and current evidence

| Repository | Product classification | Implemented in this audit | Current evidence / remaining blocker |
|---|---|---|---|
| [Cipher-messenger](https://github.com/vectolith/Cipher-messenger) | Early Matrix encrypted-messaging client | Secure homeserver URL validation; removed silent localhost production fallback; local secret/state ignores; required local Postgres secret; loopback-only dev homeserver port; active-room event reference and UI error handling; accessible room controls; locked npm dependencies; CI | Build and production-dependency audit passed. Full audit still reports an upstream dev-tooling advisory for picomatch with no published fix. No managed public homeserver or public deployment verified. |
| [quietline-messenger](https://github.com/vectolith/quietline-messenger) | Early Matrix encrypted-messaging client | Same security, local-stack, UX, dependency, and CI remediation as Cipher | Build and production-dependency audit passed. Same unpatched dev-only picomatch advisory. No managed public homeserver or public deployment verified. |
| [VaultETH](https://github.com/vectolith/VaultETH) | Self-custodial iOS and Android wallet | Reworked privacy disclosures across the policy, hosted HTML, iOS privacy screen, Android settings, support pages, and store submission kit; removed synthetic portfolio-return percentages; clearly separated live native balances from demo holdings/prices and illustrative charts; corrected the Android Gradle wrapper to an AGP-compatible version; corrected an Android authorization test vector in the separate security PR | Latest iOS CI passed on the readiness branch. Android CI is still running after the Gradle compatibility correction. Store URLs/legal identity and provider-specific data-safety declarations remain unverified; no store release is claimed. ERC-20 sends, swaps, purchases, and Solana/Bitcoin sends remain unavailable. |
| [AERYN](https://github.com/vectolith/AERYN) | Owner-minted on-chain ERC-721 artwork | Added accurate product/deployment documentation, Foundry CI, and tests for owner-only minting, on-chain metadata, and max supply | Foundry build and tests passed. Contract remains owner-mint only; no production chain deployment or public mint is claimed. |
| [demo-repository](https://github.com/vectolith/demo-repository) | Demonstration repository, not a production product | Corrected issue auto-assignment workflow so it runs on issue-open events only and removed unsupported action input | Proof HTML CI passed. Keep this repository explicitly classified as a demonstration, not a deployable Vectolith product. |
| [pluco-network](https://github.com/vectolith/pluco-network) | Digital-art and marketplace web product | Capped externally supplied ERC-2981 royalties after protocol fee reservation; rejected zero-address treasury/registry destinations; added settlement and payout regression tests; added Foundry CI | Frontend build and Foundry contract verification passed. Mainnet deployment, deployed contract addresses, and live settlement remain unverified. |
| [vectolith](https://github.com/vectolith/vectolith) | Vectolith portfolio/profile repository | Reconciled product descriptions and status claims with the actual repositories; linked the shared standard | No application CI is applicable to this profile-only repository. Product release/deployment evidence belongs in each product repository. |
| [blud](https://github.com/vectolith/blud) | Headless personal AI assistant and browser automation product | Added security disclosure policy; restored the missing Tailwind CSS entry point; formatted legacy dashboard/UI files flagged by CI; corrected Knip's dependency inventory and replaced untyped auth mocks with Better Auth domain types; consolidated work in PR #7 on the browser-worker execution-boundary prerequisite | PR #7 CI is running after the latest type/lint fixes; earlier runs exposed real formatting and lint failures, so compliance is not yet verified. Hosted setup still documents Vercel Pro and paid/usage-billed integrations. It is not a verified zero-cost public deployment. |
| [velnor](https://github.com/vectolith/velnor) | Multi-provider AI agent platform | Added security disclosure policy and shared product baseline; reviewed tenant-token validation, gateway authentication, request-size limits, and tenant provisioning boundaries | Velnor Production CI passed. No Velnor-specific Cloudflare Worker or Pages project exists in the connected Cloudflare account; other hosting providers and production secrets were not verified. |
| [NYR](https://github.com/vectolith/NYR) | Experimental kernel/operating-system project | Migrated heap, scheduler, and console locking to IRQ-safe operations; added physically contiguous frame allocation/free; implemented multi-page heap allocations for real task stacks; added contiguous-frame and 16 KiB heap regression tests; fixed the CI snapshot fallback environment handoff | The latest CI run is in progress. Earlier runs exposed a scheduler stack-size regression and an Ubuntu snapshot 401/503 fallback issue; both have targeted fixes awaiting verification. No OS release or hardware compatibility claim is made. |
| [my-project](https://github.com/vectolith/my-project) | Development workspace; no deployable product declared | Removed tracked local Antigravity chat/relay state from the readiness branch; added ignore rules and clarified repository purpose | No product build or deployment is declared. Deleting files in the PR does not erase their earlier Git history. |
| [Models-by-vectolith.](https://github.com/vectolith/Models-by-vectolith.) | Independent model ecosystem and Core Prime evaluation/runtime project | Added shared standard and security policy; removed duplicate runtime-only CI workflow because the consolidated runtime-and-evaluation workflow runs both test suites | Runtime and evaluation CI passed. Model training, teacher qualification, data provenance, and release readiness remain governed by their separate evidence pipeline; no public model release is claimed here. |

## Cross-repository security and quality observations

- Targeted code searches did not reveal an obvious committed live API key or private-key literal in the sampled product code and configuration. This is not a substitute for GitHub secret-scanning alerts or a full historical secret scan.
- Example environment files contain placeholders and public configuration values. Real secrets must remain in local ignored files or protected deployment secret stores.
- Cipher and Quietline previously lacked ignore rules for Synapse data and generated signing keys. The readiness branch now excludes those local artifacts and requires a non-default Postgres password.
- Cipher and Quietline now gate the production dependency tree. Their full development dependency inventory still reports an upstream picomatch advisory with no published patched release as of this audit date. The affected package is in the Vite development toolchain; it is not being suppressed as a production dependency vulnerability.
- No GitHub releases were found for any of the 12 repositories.
- Cloudflare account inspection found zero Pages projects and no Velnor-specific Worker. This does not establish whether another hosting provider is in use.

## Pull requests

The standard and repository-specific changes are proposed through these open pull requests:

- [Cipher-messenger #2](https://github.com/vectolith/Cipher-messenger/pull/2)
- [quietline-messenger #2](https://github.com/vectolith/quietline-messenger/pull/2)
- [VaultETH #75](https://github.com/vectolith/VaultETH/pull/75)
- [AERYN #2](https://github.com/vectolith/AERYN/pull/2)
- [demo-repository #3](https://github.com/vectolith/demo-repository/pull/3)
- [pluco-network #4](https://github.com/vectolith/pluco-network/pull/4)
- [vectolith #2](https://github.com/vectolith/vectolith/pull/2)
- [blud #7](https://github.com/vectolith/blud/pull/7)
- [velnor #36](https://github.com/vectolith/velnor/pull/36)
- [NYR #6](https://github.com/vectolith/NYR/pull/6)
- [my-project #1](https://github.com/vectolith/my-project/pull/1)
- [Models-by-vectolith. #78](https://github.com/vectolith/Models-by-vectolith./pull/78)

## Related product-specific remediation pull requests

These are separate, active implementation tracks that must be reviewed alongside the baseline PRs:

- Cipher Messenger: [#3 fail-closed E2EE send path](https://github.com/vectolith/Cipher-messenger/pull/3), [#4 independent product boundary](https://github.com/vectolith/Cipher-messenger/pull/4).
- Quietline Messenger: [#3 fail-closed E2EE send path](https://github.com/vectolith/quietline-messenger/pull/3), [#4 independent product boundary](https://github.com/vectolith/quietline-messenger/pull/4).
- VaultETH: [#74 Android wallet derivation/security gates](https://github.com/vectolith/VaultETH/pull/74), [#76 standalone wallet boundary](https://github.com/vectolith/VaultETH/pull/76).
- AERYN: [#3 ERC-721 tests and CI](https://github.com/vectolith/AERYN/pull/3), [#4 independent on-chain art product](https://github.com/vectolith/AERYN/pull/4).
- PLUCO: [#6 hardened marketplace and Originals V2](https://github.com/vectolith/pluco-network/pull/6), [#7 standalone setup instructions](https://github.com/vectolith/pluco-network/pull/7).
- Blud: [#3 browser execution boundary](https://github.com/vectolith/blud/pull/3), [#6 remove legacy Velnor bridge](https://github.com/vectolith/blud/pull/6), [#7 public standard and quality fixes](https://github.com/vectolith/blud/pull/7).
- Velnor: [#33 verified browser-delegation receipts](https://github.com/vectolith/velnor/pull/33), [#37 remove Blud coupling](https://github.com/vectolith/velnor/pull/37).
- NYR: [#5 heap allocator repair](https://github.com/vectolith/NYR/pull/5), [#7 independent OS project boundary](https://github.com/vectolith/NYR/pull/7).
- Models by vectolith: [#76 independent Core Prime candidate pipeline](https://github.com/vectolith/Models-by-vectolith./pull/76), [#79 remove shared-runtime assumptions](https://github.com/vectolith/Models-by-vectolith./pull/79).
- Vectolith portfolio: [#3 reflect the model ecosystem in the product portfolio](https://github.com/vectolith/vectolith/pull/3).

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

**Status:** Shared baseline and targeted remediation are implemented on pull-request branches. Repository-wide production readiness is not yet achieved or certified.
