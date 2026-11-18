# Vectolith Public Repository Consolidation Snapshot

**Review date:** 2026-11-18  
**Scope:** Public repositories in the Vectolith portfolio. Private repositories are outside this review.  
**Purpose:** Compare discovered branches with each repository's own `main`, review public open pull-request readiness, and record verified consolidation actions. This is a point-in-time engineering snapshot, not a production certification.

## Product boundary

Every product is independently buildable, deployable, maintainable, and useful. No product is presumed to depend on another Vectolith product. Integrations remain optional and require an explicit decision, a documented interface, and independently enforced security and failure handling.

## Verified consolidation actions

| Repository | Change | Result |
|---|---|---|
| Velnor | PR #32 — consumer-grade Sendblue channel | Merged to `main`; CI passed on the exact reviewed head. A live provider round-trip was not established by that PR. |
| Velnor | PR #35 — async tenant storage migration and credential maintenance | Merged to `main`; production build, typecheck, regression tests, E2E verification, and gateway bundle checks passed on the exact head. |
| Models by Vectolith | PR #79 — remove downstream runtime assumptions | Merged to `main`; runtime and evaluation tests passed on the exact head. Models by Vectolith is documented as an independent model product. |
| Blud | PR #8 — quality, proxy security, and dashboard regression coverage | Not merged. CI exposed environment declaration and formatting defects; fixes were committed to the PR branch and a fresh CI run is pending. |
| Velnor | PR #31 — Sendblue delivery tracking and recovery | Not merged. GitHub reports it non-mergeable; it requires conflict resolution, fresh CI, and overlap review against merged PR #32. |

## Open pull-request disposition

All open PRs in the reviewed public repositories were checked against the required base branch. The required target is `main` in the same repository.

| Repository | PR | Disposition |
|---|---:|---|
| Blud | #8 | Keep open until fresh CI passes and the complete patch is re-reviewed. |
| Blud | #1 | Hold. Draft, non-mergeable, and 229 commits ahead with five commits behind its merge base. |
| Blud | #2 | Hold. Draft, non-mergeable, and 303 commits ahead with five commits behind its merge base. Its large diff must be separated from stacked history before acceptance. |
| Velnor | #31 | Hold. Non-mergeable and requires conflict resolution plus fresh CI on the current head. |
| Models by Vectolith | #73 | Hold. Draft and large; training preflight and evaluation changes require full semantic review. |
| Models by Vectolith | #74 | Hold. Draft evidence update. Artifact metadata was checked, but the archived artifact contents have not been independently downloaded and re-hashed in this review. |
| Models by Vectolith | #75 | Hold. Draft candidate-contribution changes require evidence and qualification review. |
| Models by Vectolith | #76 | Hold. Draft inference pipeline; requires complete code, provenance, security, and evaluation review. |

Previously verified open PRs target `main`; this must remain an invariant for every future PR. Do not merge a PR solely because GitHub reports it as mergeable or because an earlier workflow passed.

## Branch inventory findings

Every discovered non-main branch in the six public repositories below was compared with that repository's `main`.

- A branch with zero commits ahead of `main` is not merge work; its unique commits are already contained in `main` or the branch is behind.
- A branch that is ahead and behind is divergent. Its changes must be reviewed independently, rebased or rebuilt where necessary, and tested against the current `main`.
- Large stacked branches are not safe to merge as a unit merely because some of their changes are useful.
- Branch deletion and repository administration are separate operations; no branch is reported deleted by this review.

### Repository status

| Repository | Current consolidation state |
|---|---|
| [Pluco](https://github.com/vectolith/pluco-network) | Multiple feature, deployment, security, and documentation branches diverge from `main`. Several branches are already behind. No blanket merge is safe; changes need feature-level review and grouping. |
| [Vectolith](https://github.com/vectolith/vectolith) | Portfolio and governance documentation branches diverge from `main`. The public-product standard and company profile need a final content review before a PR is opened. |
| [Blud](https://github.com/vectolith/blud) | Several large architecture and remediation branches are stacked or divergent. PR #1 and #2 are not merge-ready. PR #8 is the narrowest active quality change but remains blocked on fresh CI. |
| [Velnor](https://github.com/vectolith/velnor) | Several old delivery, storage, and security branches are divergent; some are already behind `main`. PR #32 and #35 are merged. PR #31 remains blocked. Other branches require dependency-aware review before any new PR is opened. |
| [NYR](https://github.com/vectolith/NYR) | Some branches are already behind `main`; remaining documentation and import branches are divergent. No automatic merge is justified without reviewing their changes against the current kernel and build state. |
| [Models by Vectolith](https://github.com/vectolith/Models-by-vectolith.) | The repository has many parallel evaluation, qualification, infrastructure, and research branches. Some are already behind `main`; many are divergent. Preserve evidence lineage and merge only narrowly reviewed changes in dependency order. PR #79 is merged; PRs #73–76 remain under review. |

## Merge rules

1. Every PR must target the same repository's `main` branch.
2. Review the complete diff, commit ancestry, dependencies, security implications, and product boundary before merging.
3. Require passing CI on the exact current head SHA. Rerun checks after any commit, rebase, or conflict resolution.
4. Require a production build and relevant regression tests for application code.
5. Keep model training authorization, data rights, teacher qualification, and human evaluation as independent gates. Passing software tests does not satisfy them.
6. Merge only the verified portion of a branch. Rebuild or split stacked branches rather than importing unrelated history.
7. Do not merge stale branches whose unique changes are already in `main`; retire them through a separately reviewed branch-cleanup action.
8. Do not claim deployment, live provider behavior, production readiness, or release completion without direct evidence.

## Remaining work

- Complete the Blud #8 CI repair and re-review its patch before merging.
- Resolve Velnor #31's conflict and determine whether any remaining changes are still needed after #32.
- Review Models by Vectolith #73–76 individually, preserving the separation between inference evidence, teacher qualification, human review, and training authorization.
- Review the remaining Pluco, Vectolith, NYR, Blud, Velnor, and Models branches in dependency order; open focused PRs against `main` only for changes that are still needed.
- Recheck all open PR base branches after each round of repository changes.

**Status:** Three verified PRs have been merged in the reviewed public repositories. Remaining branches and PRs are not blanket-merge candidates. Public-product readiness is not certified by this snapshot.
