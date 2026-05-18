# The Enterprise Internet of AI Agents

**Open-source primitives for decentralized, cryptographically governed AI agent networks.**
**Built on [Project NANDA](https://projectnanda.org) standards.**

---

## The Vision

The industry is scaling the Internet of Agents — AI agents that discover, communicate, and collaborate across the web. But the mainstream narrative assumes reliable cloud connectivity, abundant compute, and low-stakes consumer tasks.

Critical segments of the autonomous economy — aerospace, defense, maritime logistics, physical infrastructure — operate at the extreme edge. Connectivity is intermittent. Trust must be continuously verified. The penalty for an AI hallucination or unauthorized action can be severe.

To scale AI agents in the enterprise, we need more than discovery. We need **cryptographic model governance**, **offline-capable identity**, **structural regulatory compliance**, **verifiable capability restriction**, and **operator-facing surfaces** that turn signed evidence into something a human can triage in real time.

These libraries are the building blocks.

---

## How the libraries fit together

Each library ships a **small, versioned Protocol surface** and a **public conformance test suite**. Any third-party backend — including proprietary ones — plugs in behind the same Protocol and proves compliance against the same public tests. The open substrate is the standard; what you build above it is yours. No vendor lock-in, no forked forks.

---

## Trust tiers

**Operator Surfaces** answer *"how does a human see what the agents are doing?"* — forensic, filterable timelines of signed agent action evidence.
**Behavioral Trust** answers *"what is this agent allowed to do, right now?"* — regulation, capability, staging.
**Model Trust** answers *"what is this model?"* — identity, metadata, integrity, approval.
**Federation** sits beneath all three — how agents find each other on the network.

```
  +-----------------------------------------------------------+
  |                    OPERATOR SURFACES                      |
  |                       (TS / React)                        |
  |                                                           |
  |                  sm-attest-viewer                         |
  |        renders AAE event streams as forensic              |
  |        filterable timelines for compliance ops            |
  +--------------------------- ↑ -----------------------------+
                               |  W3C VC streams (AAE wire envelope)
                               |
  +-----------------------------------------------------------+
  |                      BEHAVIORAL TRUST                     |
  |                                                           |
  |    sm-locp     →     sm-airlock    →     sm-enclave       |
  |  (compliance)     (capabilities)      (speculative exec)  |
  |  *emits AAEs*                                             |
  +-----------------------------------------------------------+
                              |
  +-----------------------------------------------------------+
  |                         MODEL TRUST                       |
  |   sm-model-provenance · sm-model-card ·                   |
  |   sm-model-integrity-layer · sm-model-governance          |
  +-----------------------------------------------------------+
                              |
  +-----------------------------------------------------------+
  |                         FEDERATION                        |
  |                                                           |
  |   sm-bridge  —  registry endpoints, Quilt delta sync      |
  +-----------------------------------------------------------+
```

Substrate tiers (Behavioral / Model / Federation) are Python-first because they run where agents run. The Operator Surfaces tier is TypeScript / React because it runs where humans look — browsers, dashboards, embedded panels.

---

## Model Trust Tier

### 1. Base Identity — [`sm-model-provenance`](https://github.com/Sharathvc23/sm-model-provenance)

> Agents need a standardized way to broadcast who they are and what model powers them, without heavy dependencies in constrained edge environments.

A zero-dependency Python dataclass capturing core model identity (model ID, provider, version, governance tier). Omit-when-empty serialization keeps payloads compact. Maps into the JSON shapes required by NANDA AgentFacts and decision envelopes.

`pip install git+https://github.com/Sharathvc23/sm-model-provenance.git`

---

### 2. Metadata & Lifecycle — [`sm-model-card`](https://github.com/Sharathvc23/sm-model-card)

> Enterprise environments require structured documentation of an AI's capabilities, training metrics, and deployment lifecycle.

A unified model card schema for federated registries. Covers LoRA adapters, edge ONNX, federated learning, and heuristic models under a single validated dataclass. Four-state lifecycle (shadow → ready → deprecated → archived) with transition guards.

`pip install git+https://github.com/Sharathvc23/sm-model-card.git`

---

### 3. Cryptographic Verification — [`sm-model-integrity-layer`](https://github.com/Sharathvc23/sm-model-integrity-layer)

> In a decentralized network, systems must mathematically verify an agent hasn't been compromised in transit or loaded with unauthorized model weights.

An additive integrity gate. Offline SHA-256 weight hashing, HMAC-SHA256 attestation, model lineage tracking, and 6 built-in governance policies. Prevents base-swapping attacks. Zero runtime dependencies.

`pip install git+https://github.com/Sharathvc23/sm-model-integrity-layer.git`

---

### 4. Approval & Drift — [`sm-model-governance`](https://github.com/Sharathvc23/sm-model-governance)

> AI cannot autonomously execute high-stakes actions without a legally defensible audit trail and verifiable oversight.

Three-plane ML governance (Training → Approval → Serving). Ed25519 cryptographic signatures, M-of-N multi-party quorum, time-bounded approvals, and autonomous drift detection with auto-revocation. Designed for aerospace and defense compliance frameworks.

`pip install git+https://github.com/Sharathvc23/sm-model-governance.git`

---

## Behavioral Trust Tier

### 5. Regulatory Compliance — [`sm-locp`](https://github.com/Sharathvc23/sm-locp)

> An approved model can still do the wrong thing. Regulatory compliance is about what the *agent* does in the world, not what the *model* is.

The Open Compliance Protocol (OCP) — a defeasible-logic engine, machine-readable regulations (MRR) format, and W3C Verifiable Credential issuance layer. Agents observe their operational state, check it against regulatory theories, and produce cryptographic proofs of compliance that any third party can verify without re-running the evaluation. The VC issuance layer is what mints **Attested Action Envelopes (AAEs)** — the per-action evidence primitive consumed by `sm-attest-viewer`.

Persistence Protocol v1 is frozen. Ship your own corpus, your own backend — the engine is indifferent as long as your implementation passes the public conformance suite.

`pip install git+https://github.com/Sharathvc23/sm-locp.git`

---

### 6. Capability Restriction — sm-airlock *(private)*

Attribute-level sandbox that restricts what agent plugins can access through allowlist-based access control, rate limiting, and effect staging with commit/discard semantics.

### 7. Decision Staging — [`sm-enclave`](https://github.com/Sharathvc23/sm-enclave)

> AI agents that touch real-world state need to evaluate their options before committing. Otherwise a wrong decision fires hardware that cannot be undone.

Speculative execution sandbox. Stages side effects produced during speculative branch execution in isolated enclaves, commits the winner atomically, discards the losers. Irreversibility gate blocks hardware-touching commands from firing in speculative branches unless explicitly allowed. Pluggable committers per effect type. Zero runtime dependencies.

`pip install git+https://github.com/Sharathvc23/sm-enclave.git`

---

## Operator Surfaces Tier

### 8. Attestation Inbox — `sm-attest-viewer` *(private)*

> Compliance evidence and operator triage are useless if there's no way to *see* the signed envelopes flowing past in real time. Chat logs are not signed, not rule-citing, and not causal. Operators need a different artefact.

The reference renderer for **Attested Action Envelopes (AAEs)** — the per-action evidence primitive minted by `sm-locp` and conformant rule engines. A React / TypeScript component library that displays an AAE event stream as a forensic, filterable, reverse-chronological timeline.

Substrate-neutral by design: connect it to AG-UI, MCP, A2A, a websocket, or a JSONL file — the renderer never opens a connection itself. Domain-neutral by design: no hardcoded taxonomy for classifications, regimes, or action verbs. Conformance-driven: trust-state derivation and filter combinatorics are exported as pure, exhaustively tested functions.

AAE implements the **Attestation pillar** of NANDA's four-pillar architecture (DNS / CA / Orchestration / Attestation), complementing AgentFacts (per-credential identity) and KYA 1.0 (credential-vouching) at the per-action level. The normative wire format lives in the package's `SPEC.md`; the design rationale lives in its `WHITEPAPER.md`.

Repository currently private during v0.1 stabilization; npm publication via `@sharathvc/sm-attest-viewer` will follow.

---

## Federation

### 0. Transport & Federation — [`sm-bridge`](https://github.com/Sharathvc23/sm-bridge)

> Exposing enterprise agents to a federated network should not require rewriting an entire database or implementing complex sync protocols from scratch.

A reference implementation for NANDA-compatible registry endpoints and Quilt-style delta synchronization. Drop-in FastAPI router, DID/handle parsing, thread-safe delta store, and a protocol-based converter for integrating with any internal data model.

`pip install git+https://github.com/Sharathvc23/sm-bridge.git`

---

## Design Principles

| Principle | How |
|-----------|-----|
| **Zero dependencies** (Python tier) | All core Python libraries use only the standard library. Crypto and database backends are optional extras. |
| **Substrate-neutral** (TS tier) | The renderer accepts events as a prop. It never opens connections, polls endpoints, or makes network calls. |
| **Protocol-based** | Extension points use `@runtime_checkable` protocols (Python) or typed event arrays (TS) — no forced inheritance, no vendor lock-in. |
| **Conformance-driven** | Every versioned Protocol ships with a public test suite. Backends prove compliance by passing the same tests as the reference implementation. |
| **Fail-fast validation** | Invalid data is rejected at construction time, not discovered downstream. |
| **Composable** | Each library answers one question. Stack them for full governance or use any one standalone. |
| **Offline-first** | Every operation works without network access. Federation is additive, not required. |

---

## Quick Start

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
from sm_locp import (
    RegulatoryTheoryBuilder, Literal, VCGenerator, ComplianceCredentialSubject,
)
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

A TypeScript / React Operator Surface quickstart will land alongside `sm-attest-viewer` once that repo opens.

---

## Test Coverage

| Package | Version | Tests | Dependencies |
|---------|:-------:|:-----:|:------------:|
| [sm-bridge](https://github.com/Sharathvc23/sm-bridge) | 0.3.0 | 40 | FastAPI, Pydantic |
| [sm-model-provenance](https://github.com/Sharathvc23/sm-model-provenance) | 0.2.0 | 43 | None |
| [sm-model-card](https://github.com/Sharathvc23/sm-model-card) | 0.2.0 | 43 | None |
| [sm-model-integrity-layer](https://github.com/Sharathvc23/sm-model-integrity-layer) | 0.2.0 | 153 | None |
| [sm-model-governance](https://github.com/Sharathvc23/sm-model-governance) | 0.2.0 | 97 | None |
| [sm-locp](https://github.com/Sharathvc23/sm-locp) | 0.2.0 | 102 | cryptography |
| [sm-enclave](https://github.com/Sharathvc23/sm-enclave) | 0.2.0 | 86 | None |
| sm-airlock *(private)* | 0.1.1 | 84 | None |
| sm-attest-viewer *(private)* | 0.1.0 | 29 | React 19, Radix UI, lucide-react |
| **Total** | | **677** | |


---

**Sharath Chandra** — Personal research contributions aligned with [Project NANDA](https://projectnanda.org) standards. [Stellarminds.ai](https://stellarminds.ai)
