# Vectolith

**Vectolith builds public-facing software, AI systems, developer infrastructure, and digital products.**

Our products are intended for real users. Product status, supported functionality, security boundaries, and operational limitations must be stated accurately. A public product does not require its source repository, datasets, signing infrastructure, or private operational systems to be publicly exposed.

## Public product ecosystem

| Product | What it is | Product boundary |
|---|---|---|
| [Models by Vectolith](https://github.com/vectolith/Models-by-vectolith.) | Independent model ecosystem, including Core Prime and Core Prima tracks | Owns its model specifications, training, evaluation, artifacts, and model releases. Other products do not depend on its runtime or release schedule. |
| [Velnor](https://github.com/vectolith/velnor) | General-purpose AI agent platform with multi-provider routing, retrieval, messaging, and connected workflows | Owns its application runtime, identity, authorization, storage, integrations, deployment, and release lifecycle. |
| [Blud](https://github.com/vectolith/blud) | Personal AI assistant with browser automation and a protected credential vault | Owns its application runtime, browser execution boundary, credential handling, storage, and deployment lifecycle. |
| [Pluco](https://github.com/vectolith/pluco-network) | Digital art ownership, collection discovery, and marketplace product | Owns its frontend, contracts, marketplace logic, deployment, and chain-specific operational controls. |
| [NYR](https://github.com/vectolith/NYR) | Experimental kernel and operating-system project | Owns its kernel, build system, test environment, and release lifecycle. |
| [Vectolith](https://github.com/vectolith/vectolith) | Company and product portfolio repository | Maintains accurate company-level product descriptions and links to public product repositories. |

## Engineering principles

1. **Public-user quality:** Build for accessibility, understandable onboarding, dependable operation, and safe failure.
2. **Real functionality:** Do not present mock data, UI-only flows, or unverified integrations as working production features.
3. **Security and privacy:** Apply least privilege, strong trust boundaries, secure defaults, and honest data-flow disclosures.
4. **Evidence-led releases:** Require reproducible builds, tests, dependency review, security review, and operational evidence.
5. **Model and data provenance:** Preserve immutable revisions, licensing evidence, dataset lineage, evaluation records, and model limitations.
6. **Independent products:** Each product must remain independently buildable, deployable, maintainable, and useful. Product-to-product integration is optional and requires an explicit decision and documented interface.
7. **Clear release status:** Distinguish development, experimental, beta, production, and discontinued capabilities.

## Repository governance

See [REPOSITORY_AUDIT.md](REPOSITORY_AUDIT.md) for the current public-repository consolidation snapshot.

The [Public Product Readiness Standard](PUBLIC_PRODUCT_STANDARD.md) defines the shared engineering baseline. Each repository must translate it into project-specific implementation, tests, release gates, and operational evidence. A checklist or README is not proof of compliance.

Repository visibility is managed separately from product availability. Private source code can support a public product, provided the product's distribution, access, and operational model are intentionally designed and secured.
