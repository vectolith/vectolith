<div align="center">

<img src="./assets/vectolith-icon.svg" alt="VECTOLITH" width="220" />

# V E C T O L I T H

**Autonomous Intelligence · Applied Systems Engineering · Digital Ownership**

[Independent Product Portfolio](docs/PORTFOLIO_REGISTER.md) · [Public Product Standard](PUBLIC_PRODUCT_STANDARD.md) · [Repository Audit](REPOSITORY_AUDIT.md) · [Product Boundaries](docs/PRODUCT_BOUNDARIES.md) · [Engineering Governance](docs/ENGINEERING_GOVERNANCE.md) · [Security Policy](SECURITY.md)

</div>

---

## Company

**Vectolith** (*VEK-to-lith* — **Vector** + **Monolith**) is a technology company that owns and develops independent products and research projects across AI, model development, autonomous software, digital ownership, cryptography and systems engineering.

Vectolith is the company identity and owner—not a shared product platform. Every product has its own purpose, implementation, runtime, data stores, authentication and authorization, deployment, operations, roadmap, and release lifecycle. No Vectolith product is required to install, call, authenticate through, store data in, or otherwise depend on another Vectolith product.

The company may establish consistent security, privacy, legal, documentation and engineering standards. Those standards do not create shared runtime services, shared credentials, shared databases, mandatory APIs, cross-product release gates or operational dependencies.

## Portfolio

| Product | Independent purpose | Current documented position |
|---|---|---|
| [Velnor](https://github.com/vectolith/velnor) | General-purpose AI agent product with its own orchestration, integrations and execution runtime | Active development; production deployment and live-provider evidence must be assessed per release |
| [Blud](https://github.com/vectolith/blud) | Standalone personal agent with browser automation and protected credential vault | Active development; its README documents deployment requirements and current production limitations |
| [Models by Vectolith](https://github.com/vectolith/Models-by-vectolith.) | Independent model research and model product: specifications, foundation selection, training, evaluation, artifacts and releases | Active research and evaluation; no foundation selection, student training run or public model release is claimed |
| [Pluco](https://github.com/vectolith/pluco-network) | Independent digital-ownership protocol and marketplace | Contract deployment claims require independent chain verification; release evidence is maintained in its own repository |
| [NYR](https://github.com/vectolith/NYR) | Independent from-scratch x86-64 operating-system project | Early-kernel milestone; not a complete general-purpose OS |
| VaultETH | Native self-custodial wallet for iOS and Android | Development-stage product; physical-device security, transaction and store-release gates remain |
| Cipher Messenger | Encrypted messaging product | Development-stage client; managed public homeserver and release evidence are not verified |
| Quietline Messenger | Encrypted messaging product | Development-stage client; managed public homeserver and release evidence are not verified |
| AERYN | On-chain generative-art collection | Collection development; no production deployment or public mint is claimed |

Repository visibility and product maturity are separate. Source visibility does not establish product availability, and a public product does not require its source repository or operational systems to be public. The [portfolio register](docs/PORTFOLIO_REGISTER.md) records product scope and release gates without exposing private repository locations.

## Engineering principles

1. **Product independence:** each product must build, deploy, operate and fulfil its own purpose without another Vectolith product.
2. **Public-user quality:** build for accessibility, understandable onboarding, dependable operation and safe failure.
3. **Real functionality:** do not present mock data, UI-only flows or unverified integrations as working production features.
4. **Security and privacy:** apply least privilege, product-owned trust boundaries and honest data-flow disclosures.
5. **Evidence-led releases:** require reproducible builds, tests, dependency review, security review and operational evidence per product.
6. **Dependency discipline:** identify external services, limits and failure modes; do not rely on unverified service behaviour.
7. **Clear release status:** distinguish research, development, prototype, beta, production and discontinued capabilities.

No product-to-product integration is part of the default architecture. A future integration requires separate explicit approval, must be replaceable and must remain nonessential to each product's core purpose. No product may rely on another Vectolith product's runtime, identity service, database, credentials or deployment.

See the [company-wide engineering and release governance](docs/ENGINEERING_GOVERNANCE.md) and [security policy](SECURITY.md).

---

<div align="center">
  <sub>© 2026 Vectolith · Engineered with precision.</sub>
</div>
