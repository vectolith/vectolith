# Vectolith

**Vectolith builds public-facing software, AI systems, developer infrastructure, and self-custodial products.**

Our products are intended for real users. Product status, supported functionality, security boundaries, and operational limitations must be stated accurately. A public product does not require its source repository, datasets, signing infrastructure, or private operational systems to be publicly exposed.

## Product ecosystem

| Product / project | What it is | Verified scope and current status |
|---|---|---|
| [Models by Vectolith](https://github.com/vectolith/Models-by-vectolith.) | Independent model ecosystem, including Core Prime and Core Prima tracks | Active research, teacher qualification, evaluation, and runtime engineering. No public release of student weights is claimed by the repository README. |
| [Velnor](https://github.com/vectolith/velnor) | General-purpose AI agent platform with multi-provider routing, retrieval, messaging, and connected workflows | Active implementation. Messaging/API surfaces exist; production operation depends on correctly configured identity, secrets, durable storage, provider credentials, and deployment controls. |
| [Blud](https://github.com/vectolith/blud) | Headless personal AI assistant with browser automation and a protected credential vault | Active codebase. Requires external integrations and deployment configuration. The current hosted minute-level scheduling path has a Vercel Pro dependency; a zero-cost public release must remove or replace that dependency rather than assume a paid plan. |
| [PLUCO Network](https://github.com/vectolith/pluco-network) | Digital art ownership, collection discovery, and marketplace web product | Public web surface with Foundry contract tests. The repository explicitly states that configured Base addresses are not deployment proof and that contract settlement must not be advertised as live until independently verified. |
| [VaultETH](https://github.com/vectolith/VaultETH) | Self-custodial multi-chain wallet for iOS and Android | Mobile implementation and CI exist. Current documented limitations include native-asset EVM sends only, receive-only Bitcoin/Solana address derivation, and demo portfolio/market figures. ERC-20 sends, fiat purchases, and swaps are not released capabilities. |
| [AERYN](https://github.com/vectolith/AERYN) | On-chain ERC-721 art collection with generated SVG metadata | Owner-minted collection contract, fixed maximum supply of 100. No production deployment is claimed. |
| [Cipher-messenger](https://github.com/vectolith/Cipher-messenger) | Matrix-based encrypted messaging client | Early application implementation; requires a configured HTTPS homeserver and further reliability, UX, and security verification. |
| [Quietline Messenger](https://github.com/vectolith/quietline-messenger) | Matrix-based encrypted messaging client | Early application implementation; requires a configured HTTPS homeserver and further reliability, UX, and security verification. |

## Engineering principles

1. **Public-user quality:** Build for accessibility, understandable onboarding, dependable operation, and safe failure.
2. **Real functionality:** Do not present mock data, UI-only flows, or unverified integrations as working production features.
3. **Security and privacy:** Apply least privilege, strong trust boundaries, local protection for secrets, and honest data-flow disclosures.
4. **Evidence-led releases:** Require reproducible builds, tests, dependency review, security review, and operational evidence.
5. **Model and data provenance:** Preserve immutable revisions, licensing evidence, dataset lineage, evaluation records, and model limitations.
6. **Responsible operations:** Prefer free and open-source infrastructure where viable. Do not introduce paid services or paid quotas without explicit authorization.
7. **Clear release status:** Distinguish development, experimental, beta, production, and discontinued capabilities.

## Repository governance

The [Public Product Readiness Standard](https://github.com/vectolith/vectolith/blob/main/PUBLIC_PRODUCT_STANDARD.md) defines the shared baseline. Each repository must translate it into project-specific implementation, tests, release gates, and operational evidence. A checklist or README is not proof of compliance.

Repository visibility is managed separately from product availability. Private source code can support a public product, provided the product's distribution, access, and operational model are intentionally designed and secured.
