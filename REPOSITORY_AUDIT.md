# Vectolith Public Repository Consolidation Snapshot

**Review date:** 2026-11-18  
**Scope:** Six public repositories in the Vectolith portfolio. Private repositories are outside this review.  
**Purpose:** Compare discovered branches with each repository's own `main`, review public open pull-request readiness, and record verified consolidation actions. This is a point-in-time engineering snapshot, not a production certification.

## Product boundary

Every product is independently buildable, deployable, maintainable, and useful. No product is presumed to depend on another Vectolith product. Integrations remain optional and require an explicit decision, a documented interface, and independently enforced security and failure handling.

## Verified merges

Ten PRs have been merged into their respective repository's `main` during this consolidation cycle:

| Repository | PR | Change | Verification |
|---|---:|---|---|
| Velnor | #32 | Consumer-grade Sendblue channel | CI passed on the exact reviewed head. A live provider round-trip was not established by that PR. |
| Velnor | #35 | Async tenant storage migration and credential maintenance | Production build, typecheck, regression tests, E2E verification, and gateway bundle checks passed on the exact head. |
| Velnor | #40 | Standalone public-product and security baseline | Documentation-only; clean branch from `main`, two files reviewed. |
| Models by Vectolith | #79 | Remove downstream runtime assumptions | Runtime and evaluation tests passed on the exact head. |
| Models by Vectolith | #80 | Independent model product readiness and security baseline | Documentation-only; clean branch from `main`, two files reviewed. |
| Vectolith | #5 | Public portfolio, standalone product boundaries, readiness and security governance | Documentation-only; rebuilt from `main`; public-only portfolio and audit; no private repository locations or budget figures. |
| NYR | #8 | Standalone OS and kernel security baseline | Documentation-only; clean branch from `main`, two files reviewed. |
| Blud | #9 | Standalone personal-agent, browser and credential security baseline | Documentation-only; clean branch from `main`, two files reviewed. |
| Pluco | #11 | Base V1 deployment verification and runtime-bytecode regression tests | Latest CI passed on exact head: contract verification run 44389773943 and build run 44389773952. Preserved V2 source/tests; verifier remains scoped to V1. |
| Pluco | #12 | Standalone protocol and smart-contract security baseline | Documentation-only; clean branch from `main`, two files reviewed. |

## Open pull-request disposition

All currently open PRs in the reviewed public repositories target that repository's `main`. This remains mandatory for every future PR.

| Repository | PR | Current disposition |
|---|---:|---|
| Blud | #8 | Keep open until fresh CI passes. Previous runs exposed Turbo environment/test alignment and formatting defects. A correction was pushed to the latest head; the new CI run must pass before merge. |
| Blud | #1 | Hold. Draft, non-mergeable, 229 commits ahead and five behind its merge base. Rebuild only the required browser-session changes from `main`; do not merge the stacked history. |
| Blud | #2 | Hold. Draft, non-mergeable, 303 commits ahead and five behind its merge base. Separate and review the actual encryption/account-lifecycle fixes from stacked history. |
| Velnor | #31 | Hold. Non-mergeable; requires conflict resolution, fresh CI on the current head, and overlap review against merged PR #32. |
| Models by Vectolith | #73 | Hold. Draft and large; training preflight and evaluation changes require full semantic review. |
| Models by Vectolith | #74 | Hold. Draft evidence update. Artifact metadata was checked, but archived artifact contents have not been independently downloaded and re-hashed in this review. |
| Models by Vectolith | #75 | Hold. Draft candidate-contribution changes require evidence and qualification review. |
| Models by Vectolith | #76 | Hold. Draft inference pipeline; requires complete code, provenance, security, and evaluation review. |

No PR should be merged solely because GitHub reports it as mergeable or because an earlier workflow passed. Require passing CI on the exact current head SHA and rerun after every change.

## Branch inventory findings

Discovered non-main branches in the six public repositories were compared with that repository's `main`.

- A branch with zero commits ahead of `main` is not merge work; its unique commits are already contained in `main` or the branch is behind.
- A branch that is ahead and behind is divergent. Its changes must be reviewed independently, rebased or rebuilt where necessary, and tested against the current `main`.
- Large stacked branches are not safe to merge as a unit merely because some of their changes are useful.
- Clean documentation branches were rebuilt from `main` where their original branches contained unrelated code or stale history.
- Some old standards branches remain unmerged because they also contain application, kernel, workflow or evaluation changes that require separate review.
- Branch deletion/retirement is separate from merging; no branch is reported deleted by this review.

### Repository status

| Repository | Current consolidation state |
|---|---|
| [Pluco](https://github.com/vectolith/pluco-network) | PRs #11 and #12 merged. Remaining old feature/deployment branches are not blanket-merge candidates; review contract, marketplace and deployment changes by feature. |
| [Vectolith](https://github.com/vectolith/vectolith) | PR #5 merged. Public company profile, portfolio register, readiness standard, security policy and repository snapshot now describe independent products without exposing private repository locations or budget figures. |
| [Blud](https://github.com/vectolith/blud) | PR #9 merged. PR #8 is the narrow quality/security patch but remains blocked on fresh CI. PR #1/#2 are large stacked branches and are not merge-ready. The old standards branch contains unrelated browser-worker/dashboard changes and is not merged wholesale. |
| [Velnor](https://github.com/vectolith/velnor) | PRs #32, #35 and #40 merged. PR #31 remains blocked. Other delivery/security branches require dependency-aware review before new PRs are opened. |
| [NYR](https://github.com/vectolith/NYR) | PR #8 merged. The old standards branch also contains physical-memory allocator and heap changes; its latest CI failed at host memory-manager tests, so those code changes remain unmerged. |
| [Models by Vectolith](https://github.com/vectolith/Models-by-vectolith.) | PRs #79 and #80 merged. PRs #73–76 remain under review. The old standards branch contains workflow changes that were not included in the documentation-only merge. Preserve evidence lineage and merge changes in dependency order. |

## Merge rules

1. Every PR must target the same repository's `main` branch.
2. Review the complete diff, commit ancestry, dependencies, security implications, and product boundary before merging.
3. Require passing CI on the exact current head SHA. Rerun checks after any commit, rebase, or conflict resolution.
4. Require a production build and relevant regression tests for application or kernel code.
5. Keep model training authorization, data rights, teacher qualification, and human evaluation as independent gates. Passing software tests does not satisfy them.
6. Merge only the verified portion of a branch. Rebuild or split stacked branches rather than importing unrelated history.
7. Do not merge stale branches whose unique changes are already in `main`; retire them through a separately reviewed branch-cleanup action.
8. Do not claim deployment, live provider behavior, production readiness, or release completion without direct evidence.

## Remaining work

- Complete the Blud #8 CI repair and re-review its patch before merging.
- Resolve Velnor #31's conflict and determine whether any remaining changes are still needed after #32.
- Review Models by Vectolith #73–76 individually, preserving the separation between inference evidence, teacher qualification, human review, and training authorization.
- Review the remaining Pluco, NYR, Blud, Velnor, and Models branches in dependency order; open focused PRs against `main` only for changes that are still needed.
- Recheck all open PR base branches after each round of repository changes.

**Status:** Ten verified PRs have been merged across the reviewed public repositories. Remaining branches and PRs are not blanket-merge candidates. Public-product readiness is not certified by this snapshot.
