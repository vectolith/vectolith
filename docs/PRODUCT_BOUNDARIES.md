# Independent Vectolith product boundaries

**Applies to:** Every Vectolith product and product initiative  
**Status:** Mandatory architecture rule

## 1. Company identity is not a product dependency

Vectolith is the company and ownership identity. It is not a shared runtime, platform, identity provider, data platform, orchestration service, or mandatory integration layer.

Every Vectolith product is a standalone product. Each must be independently buildable, deployable, configurable, operable, maintainable, supportable, and usable for its stated purpose. A product must not require another Vectolith product to start, authenticate users, access its own data, perform its core functions, or release updates.

Company-wide policies may define minimum security, privacy, accessibility, provenance, documentation and engineering standards. They must not impose shared credentials, shared databases, shared runtime processes, common deployment infrastructure, mandatory service APIs or synchronized release schedules.

## 2. Required independence invariants

Every product owns and controls its own:

- Product requirements, user experience, roadmap and acceptance criteria.
- Application code, runtime, process lifecycle and failure handling.
- User identity, authentication, authorization, sessions and permissions.
- Databases, files, encryption keys, secrets, retention and recovery.
- Deployment configuration, infrastructure, monitoring and incident response.
- External service accounts, credentials, quotas, billing and fallback behaviour.
- CI, tests, release approvals, versioning, rollback and support lifecycle.
- Security threat model, privacy disclosures and product-specific legal notices.

A product may use external open-source libraries, infrastructure providers, model providers or optional third-party integrations. Such dependencies must be declared and justified. Dependencies on another Vectolith product are not presumed or required.

## 3. Optional integration rules

An optional product-to-product integration is permitted only when it adds a distinct user benefit and is explicitly chosen by the product owner. It must satisfy all of the following:

1. The integrating product works for its core purpose when the integration is disabled or unavailable.
2. The integration is opt-in, replaceable and documented; no silent fallback may make it mandatory.
3. Each product retains its own identity, authorization, data ownership, secrets and deployment.
4. Communication uses a versioned, authenticated, least-privilege interface.
5. Data shared is minimized, user-authorized where appropriate, and subject to documented retention/deletion rules.
6. Failures, timeouts and partial results are handled without taking down the standalone product.
7. Each product tests and releases its side independently. No cross-product synchronized deployment is required.
8. The integration cannot expand the permissions of either product or bypass user approval.

A product must not be described as incomplete because it does not integrate with another Vectolith product.

## 4. Product ownership and scope

### Velnor — general-purpose AI agent

Velnor owns its own agent loop, model-provider adapters, user/workspace context, integrations, tool execution, authorization, persistence, task lifecycle and operational runtime. It may optionally connect to external services or other products through explicit adapters. It must not require Models by Vectolith, Blud, or another Vectolith repository to operate.

### Blud — personal browser agent

Blud owns its own agent application, browser execution, browser-session lifecycle, credential vault, user identity, storage, deployment and task evidence. It must operate as a standalone product. A Velnor-to-Blud browser bridge, if ever enabled, is an optional integration—not a required architecture or release dependency. Blud must remain usable without Velnor.

### Models by Vectolith — model research and model product

This repository owns its model specifications, foundation selection, training data lineage, teacher qualification, evaluation, model registry, artifacts and model release lifecycle. Any runtime/package in this repository serves this model product's own development and evaluation needs; it is not a mandatory shared runtime for other Vectolith products.

Another product may optionally consume a released model through a documented model interface, but that product owns its own runtime, provider adapter, authorization, data handling and operational fallback. No product is required to use this model family.

### PLUCO Network — digital ownership protocol and marketplace

PLUCO owns its own smart contracts, deployment registry, protocol economics, marketplace application, wallet connection interface, data and operations. It must not require VaultETH or any other Vectolith product. Wallet interoperability, where offered, must use ordinary documented wallet standards and remain user-selectable.

### VaultETH — self-custodial wallet

VaultETH owns its native iOS and Android clients, wallet creation/import, key lifecycle, secure storage, address derivation, signing, transaction validation, network support and release lifecycle. It must not require PLUCO or any other Vectolith product. It may connect to independent blockchain networks and user-selected external services under its own security and privacy controls.

### NYR — x86-64 operating system

NYR owns its kernel, boot process, memory management, interrupt handling, scheduling, drivers, toolchain and systems validation. It is an independent operating-system project, not a runtime or infrastructure dependency for another Vectolith product.

### Cipher Messenger — encrypted messaging

Cipher owns its own messaging client, identity and device model, encryption state, homeserver configuration, storage, user experience and release lifecycle. It must operate independently and must not require Quietline or another Vectolith product.

### Quietline Messenger — encrypted messaging

Quietline owns its own messaging client, identity and device model, encryption state, homeserver configuration, storage, user experience and release lifecycle. It must operate independently and must not require Cipher or another Vectolith product. Its current scaffold substantially overlaps Cipher; a distinct product specification is still needed, but that does not authorize a shared runtime or a forced consolidation.

### AERYN — autonomous intelligence and research

AERYN owns its own product requirements, research workflow, source retrieval, provenance, synthesis, data handling, runtime, evaluation and release lifecycle. Its detailed specification and implementation remain to be established. It must not depend on Velnor or Models by Vectolith.

## 5. Repository classification

Not every repository is a released product. Company governance repositories, internal demos, templates and placeholders must be classified honestly. Their existence does not create product dependencies:
- `vectolith` is the company identity and governance repository, not a runtime dependency.
- `demo-repository` is an internal GitHub demonstration/template.
- `my-project` is an unclassified placeholder until its purpose is specified.

## 6. Verification requirements

Each product's independent release checklist must verify:

- A clean checkout can install/build/test without checking out another Vectolith repository.
- Runtime startup does not require another Vectolith service, token, database, account or endpoint.
- Authentication and authorization work using product-owned mechanisms.
- Data access, persistence, backup and deletion are product-owned.
- Required external services are listed with purpose, permissions, limits, failure modes and fallback.
- Core workflows remain available when every optional Vectolith-to-Vectolith integration is disabled.
- CI and release workflows run and complete independently.
- Product documentation does not claim another Vectolith product is required.

Record the exact commit, commands, environment, workflow URLs and outcomes. A documentation statement alone is not proof of independence.

## 7. Governance

The portfolio register is an inventory and status record, not an architecture that binds products together. The company may share policy, brand assets and non-runtime documentation templates. Each product team remains responsible for implementing and proving the controls in its own repository.
