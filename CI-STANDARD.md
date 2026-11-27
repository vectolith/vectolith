# Vectolith GitHub Actions Node standard

All new and existing Node.js repositories should use Node.js 24 in CI.

- Use `actions/setup-node@v7` with `node-version: "24"`.
- Use `actions/checkout@v7` for checkout.
- Prefer lockfile-backed installs (`npm ci`, `pnpm install --frozen-lockfile`, or `yarn --immutable`).
- Give CI workflows minimal explicit permissions, concurrency cancellation for PR CI, and job timeouts.
- Keep third-party actions updated; pin to verified immutable commit SHAs where supply-chain policy requires it and annotate the upstream release.
- Use Node 24 only for Node workloads. Python, Swift, Android, Solidity, and OS/kernel workflows retain their appropriate runtimes.
- Periodically review GitHub Actions upstream releases and Node LTS changes.

A reusable workflow is provided at `.github/workflows/node24-standard.yml`. New repositories can call it for their conventional npm test/build pipeline, or adapt the contract for their package manager and project scripts.
