## Overview

<!-- Provide a clear, concise summary of the change and the architectural rationale behind it. -->

## Motivation & Context

- Fixes issue #
- Relates to: <!-- velnor / blud / pluco-network / foundation -->

## Type of Change

- [ ] :bug: Bug fix (non-breaking change which fixes an issue)
- [ ] :sparkles: New feature (non-breaking change adding functionality)
- [ ] :zap: Performance optimization or memory improvement
- [ ] :lock: Security hardening or credential sanitation
- [ ] :recycle: Refactoring (no functional changes)
- [ ] :books: Documentation or type definition update
- [ ] :boom: Breaking change (fix or feature causing existing behavior to change)

## Verification Checklist

Please verify that all applicable checks pass before requesting review:

- [ ] **Tests**: New and existing tests pass locally (`npm test` / `vitest run`).
- [ ] **Type Safety**: TypeScript compiler check passes cleanly (`npx tsc --noEmit`).
- [ ] **Security**: No secrets, auth tokens, or private keys are committed or logged.
- [ ] **Zero Fabrication**: All execution receipts, tool states, and citations are strictly verified.
- [ ] **Multi-Tenant Isolation**: No memory, cache, or workspace state leaks across tenant boundaries.
- [ ] **Documentation**: Updated README, JSDoc, or relevant architecture diagrams.
