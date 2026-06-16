# The Enterprise Internet of AI Agents

**Open-source primitives for decentralized, cryptographically governed AI agent networks.**
**Aligned with [Project NANDA](https://projectnanda.org) standards.**

---

## The Vision

The industry is scaling the Internet of Agents. But the mainstream narrative assumes reliable
cloud connectivity, abundant compute, and low-stakes consumer tasks. The autonomous economy at
the extreme edge — aerospace, defense, maritime, physical infrastructure — needs more:
**cryptographic model governance**, **offline-capable identity**, **structural compliance**,
**verifiable capability restriction**, and **operator surfaces** that turn signed evidence into
something a human can triage in real time. These libraries are the building blocks.

Each ships a **small, versioned Protocol surface** and a **public conformance suite**. Any backend
— including proprietary ones — plugs in behind the same Protocol and proves compliance against the
same public tests. Compliance is **mechanical, not declarative**: a runtime ships a signed
[`sm-conformance`](https://github.com/Sharathvc23/sm-conformance) badge, re-verifiable offline by
anyone holding the runtime's `did:key` — no service on the path, no vendor lock-in.

---

## Stellar Minds map

```
  +-----------------------------------------------------------+
  |          OPERATOR SURFACES   (TS / React)                 |
  |   attest-viewer · decision-inspector · attest-auditor     |
  +--------------------------- ↑ -----------------------------+
                               |  W3C VC streams (AAE envelope)
  +-----------------------------------------------------------+
  |          BEHAVIORAL TRUST   locp → airlock → enclave      |
  +-----------------------------------------------------------+
  |          MODEL TRUST   provenance · card · integrity · gov|
  +-----------------------------------------------------------+
  |          FEDERATION   sm-bridge · NANDA Chapter Protocol  |
  +-----------------------------------------------------------+
```

*Substrate tiers are Python-first (they run where agents run); Operator Surfaces are TS / React
(they run where humans look).*

---

## The libraries

<details>
<summary><b>🧠 Model Trust</b> — what is this model? · identity · cards · integrity · governance (4)</summary>

| Library | What it does | Install |
|---|---|---|
| [`sm-model-provenance`](https://github.com/Sharathvc23/sm-model-provenance) | Zero-dep model identity dataclass (id, provider, version, tier); maps into AgentFacts | `pip install git+https://github.com/Sharathvc23/sm-model-provenance.git` |
| [`sm-model-card`](https://github.com/Sharathvc23/sm-model-card) | Unified model-card schema; 4-state lifecycle with transition guards | `pip install git+https://github.com/Sharathvc23/sm-model-card.git` |
| [`sm-model-integrity-layer`](https://github.com/Sharathvc23/sm-model-integrity-layer) | Offline SHA-256 weight hashing, HMAC attestation, lineage; blocks base-swap attacks | `pip install git+https://github.com/Sharathvc23/sm-model-integrity-layer.git` |
| [`sm-model-governance`](https://github.com/Sharathvc23/sm-model-governance) | 3-plane ML governance; Ed25519 sigs, M-of-N quorum, drift auto-revocation | `pip install git+https://github.com/Sharathvc23/sm-model-governance.git` |
</details>

<details>
<summary><b>🛡️ Behavioral Trust</b> — what may this agent do, right now? · compliance · capability · staging (3)</summary>

| Library | What it does | Install |
|---|---|---|
| [`sm-locp`](https://github.com/Sharathvc23/sm-locp) | Open Compliance Protocol — defeasible-logic engine + W3C VC issuance; mints **AAEs** | `pip install git+https://github.com/Sharathvc23/sm-locp.git` |
| [`sm-airlock`](https://github.com/Sharathvc23/sm-airlock) | Allowlist-gated plugin sandbox; deny-by-default, sliding-window rate limits, signed manifests | `pip install git+https://github.com/Sharathvc23/sm-airlock.git` |
| [`sm-enclave`](https://github.com/Sharathvc23/sm-enclave) | Speculative-execution sandbox; stages effects, commits the winner, irreversibility gate | `pip install git+https://github.com/Sharathvc23/sm-enclave.git` |
</details>

<details>
<summary><b>👁️ Operator Surfaces</b> — how does a human see what the agents are doing? (TS / React, 3)</summary>

| Library | What it does |
|---|---|
| [`sm-attest-viewer`](https://github.com/Sharathvc23/sm-attest-viewer) | Renders AAE streams as forensic, filterable, reverse-chronological timelines |
| [`sm-decision-inspector`](https://github.com/Sharathvc23/sm-decision-inspector) | HITL workbench for `decision` envelopes; M-of-N quorum chip, gesture-safe approve / deny |
| [`sm-attest-auditor`](https://github.com/Sharathvc23/sm-attest-auditor) | Bidirectional audit drill; RFC 6962 merkle inclusion verified in-browser via Web Crypto |
</details>

<details>
<summary><b>🌐 Federation &amp; NANDA Chapter Protocol</b> — how agents find, join, and trust each other (5)</summary>

| Library | What it does | Install |
|---|---|---|
| [`sm-bridge`](https://github.com/Sharathvc23/sm-bridge) | NANDA-compatible registry endpoints + Quilt delta sync; drop-in FastAPI router | `pip install git+https://github.com/Sharathvc23/sm-bridge.git` |
| [`sm-arp`](https://github.com/Sharathvc23/sm-arp) | Agency Receipt Protocol — per-action, Ed25519-signed, JCS-canonical, hash-chained receipts | `pip install sm-arp` |
| [`sm-org-server`](https://github.com/Sharathvc23/sm-org-server) | Minimal, backend-agnostic **server** implementing the Chapter Protocol wire (~550 lines) | `pip install sm-org-server` |
| [`sm-org-agent`](https://github.com/Sharathvc23/sm-org-agent) | The **agent** client signing surface — did:key identity, canonical strings, Ed25519 headers | `pip install sm-org-agent` |
| [`sm-federation`](https://github.com/Sharathvc23/sm-federation) | Cross-server federation descriptor + envelope spec | `pip install git+https://github.com/Sharathvc23/sm-federation.git` |
</details>

<details>
<summary><b>✅ Conformance</b> — the shared substrate that makes "compliant" checkable</summary>

[`sm-conformance`](https://github.com/Sharathvc23/sm-conformance) is orthogonal to the four tiers —
not one of them, but the substrate that lets any of them prove it is honestly implemented. A runtime
runs a tier's vectors-driven suite, then ships a small JSON **badge** signed by its own Ed25519 key,
recording which suite it passed (pinned by a `suite_digest` over the vector corpus) and the pass/fail
counts. Any party re-verifies the badge offline against the runtime's `did:key` — no service, no
proprietary library on the path. It ships a trust ladder — **self-signed** badge and **lab
counter-signature** — with `--require-countersigned` admission gates, so a registry can *demand* a
trusted lab's attestation rather than accept a runtime's self-claim.

`pip install sm-conformance`
</details>

---

## Design Principles

| Principle | How |
|---|---|
| **Zero dependencies** (Python tier) | Core libraries use only the standard library; crypto and database backends are optional extras |
| **Substrate-neutral** (TS tier) | The renderer accepts events as a prop — it never opens connections, polls endpoints, or makes network calls |
| **Protocol-based** | Extension points use `@runtime_checkable` protocols (Python) or typed event arrays (TS) — no forced inheritance, no lock-in |
| **Conformance-driven** | Every versioned Protocol ships a public test suite; backends prove compliance by passing the same tests as the reference implementation |
| **Fail-fast validation** | Invalid data is rejected at construction time, not discovered downstream |
| **Composable** | Each library answers one question; stack them for full governance or use any one standalone |
| **Offline-first** | Every operation works without network access; federation is additive, not required |

<details>
<summary><b>Quick start</b> — five tiers in ~25 lines</summary>

```python
# Identity
from sm_model_provenance import ModelProvenance
provenance = ModelProvenance(model_id="my-model", provider_id="local", model_version="1.0")

# Metadata
from sm_model_card import ModelCard
card = ModelCard(model_id="my-model", model_type="lora_adapter", status="shadow")

# Integrity
from sm_integrity import check_governance, STANDARD_POLICIES
report = check_governance(provenance, policies=STANDARD_POLICIES)

# Governance
from sm_governance import GovernanceCoordinator
coord = GovernanceCoordinator()
output = coord.complete_training("my-model", "sha256:abc", {"loss": 0.28})
approval = coord.submit_for_governance(output, approved_by="governance-lead")

# Regulatory compliance — produces AAEs
from sm_locp import RegulatoryTheoryBuilder, Literal
theory = (
    RegulatoryTheoryBuilder("WAREHOUSE")
    .defeasible("D1", ["operator_certified"], "permitted", priority=5)
    .fact("operator_certified")
    .build()
)
result = theory.query(Literal.parse("permitted"))

# Federation
from sm_bridge import SmBridge, SimpleAgent
bridge = SmBridge(registry_id="my-registry", provider_name="My Org", provider_url="https://example.com")
bridge.register_agent(SimpleAgent(id="my-agent", name="My Agent", description="An AI assistant"))
```
</details>

---

## Test coverage

| Package | Version | Tests | Dependencies |
|---|:-:|:-:|:-:|
| [sm-bridge](https://github.com/Sharathvc23/sm-bridge) | 0.3.1 | 40 | FastAPI, Pydantic |
| [sm-model-provenance](https://github.com/Sharathvc23/sm-model-provenance) | 0.2.0 | 43 | None |
| [sm-model-card](https://github.com/Sharathvc23/sm-model-card) | 0.2.0 | 43 | None |
| [sm-model-integrity-layer](https://github.com/Sharathvc23/sm-model-integrity-layer) | 0.2.0 | 153 | None |
| [sm-model-governance](https://github.com/Sharathvc23/sm-model-governance) | 0.2.0 | 97 | None |
| [sm-locp](https://github.com/Sharathvc23/sm-locp) | 0.2.0 | 102 | cryptography |
| [sm-enclave](https://github.com/Sharathvc23/sm-enclave) | 0.2.0 | 86 | None |
| [sm-airlock](https://github.com/Sharathvc23/sm-airlock) | 0.2.0 | 78 | None |
| [sm-attest-viewer](https://github.com/Sharathvc23/sm-attest-viewer) | 0.2.3 | 69 | React 19, Radix UI |
| [sm-decision-inspector](https://github.com/Sharathvc23/sm-decision-inspector) | 0.1.1 | 45 | React 19, Radix UI |
| [sm-attest-auditor](https://github.com/Sharathvc23/sm-attest-auditor) | 0.1.1 | 35 | React 19, Radix UI |
| [sm-arp](https://github.com/Sharathvc23/sm-arp) | 0.2.1 | 89 | cryptography, base58, jcs |
| [sm-org-server](https://github.com/Sharathvc23/sm-org-server) | 0.1.0 | 75 | FastAPI, sm-arp |
| [sm-org-agent](https://github.com/Sharathvc23/sm-org-agent) | 0.1.0 | 34 | cryptography, sm-arp |
| [sm-federation](https://github.com/Sharathvc23/sm-federation) | 0.1.0 | 28 | None |
| [sm-conformance](https://github.com/Sharathvc23/sm-conformance) | 0.3.1 | 96 | cryptography, base58 |
| **Total** | | **1,113** | |

---

**Sharath Chandra** — Personal research contributions aligned with [Project NANDA](https://projectnanda.org) standards. [Stellarminds.ai](https://stellarminds.ai)
