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
| [VaultETH](https://github.com/vectolith/VaultETH) | Self-custodial iOS and Android wallet | Rewrote privacy disclosures to identify local wallet data, RPC metadata, and public-chain visibility; corrected store checklist so it does not claim blanket zero data collection; clarified unsupported features and demo portfolio content | Android test exposed a real faulty test vector: the “changed” chain ID equaled the original. Corrected to a distinct chain ID; iOS and Android CI reruns are in progress. Store release and public deployment are not verified. ERC-20 sends, swaps, and fiat purchases remain documented as unavailable. |
| [AERYN](https://github.com/vectolith/AERYN) | Owner-minted on-chain ERC-721 artwork | Added accurate product/deployment documentation, Foundry CI, and tests for owner-only minting, on-chain metadata, and max supply | Foundry build and tests passed. Contract remains owner-mint only; no production chain deployment or public mint is claimed. |
| [demo-repository](https://github.com/vectolith/demo-repository) | Demonstration repository, not a production product | Corrected issue auto-assignment workflow so it runs on issue-open events only and removed unsupported action input | Proof HTML CI passed. Keep this repository explicitly classified as a demonstration, not a deployable Vectolith product. |
| [pluco-network](https://github.com/vectolith/pluco-network) | Digital-art and marketplace web product | Capped externally supplied ERC-2981 royalties after protocol fee reservation; rejected zero-address treasury/registry destinations; added settlement and payout regression tests; added Foundry CI | Frontend build and Foundry contract verification passed. Mainnet deployment, deployed contract addresses, and live settlement remain unverified. |
| [vectolith](https://github.com/vectolith/vectolith) | Vectolith portfolio/profile repository | Reconciled product descriptions and status claims with the actual repositories; linked the shared standard | No application CI is applicable to this profile-only repository. Product release/deployment evidence belongs in each product repository. |
| [blud](https://github.com/vectolith/blud) | Headless personal AI assistant and browser automation product | Added security disclosure policy; formatted the shared standard to repository formatter; corrected browser-worker test to assert retired endpoint returns 410 rather than fake success | Full Blud CI is still running. Its current hosted setup documents dependencies on Vercel Pro and paid/usage-billed integrations. It is not a verified zero-cost public deployment. |
| [velnor](https://github.com/vectolith/velnor) | Multi-provider AI agent platform | Added security disclosure policy and shared product baseline; reviewed tenant-token validation, gateway authentication, request-size limits, and tenant provisioning boundaries | Velnor Production CI passed. No Velnor-specific Cloudflare Worker or Pages project exists in the connected Cloudflare account; other hosting providers and production secrets were not verified. |
| [NYR](https://github.com/vectolith/NYR) | Experimental kernel/operating-system project | Migrated heap locking to IRQ-safe spinlock operations; moved invalid/double-free validation under the lock; replaced POSIX-only allocation with C11 aligned allocation; rejected oversized allocations that would exceed the single allocated backing page; added host regression coverage and synchronized accounting reads | CI previously stopped before compilation because Ubuntu snapshot endpoints returned HTTP 503. A retry is running. Heap changes are not yet verified by a successful host/kernel build. |
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
- [blud #4](https://github.com/vectolith/blud/pull/4)
- [velnor #36](https://github.com/vectolith/velnor/pull/36)
- [NYR #6](https://github.com/vectolith/NYR/pull/6)
- [my-project #1](https://github.com/vectolith/my-project/pull/1)
- [Models-by-vectolith. #78](https://github.com/vectolith/Models-by-vectolith./pull/78)

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
