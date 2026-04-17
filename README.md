# The Enterprise Internet of AI Agents

**Open-source primitives for decentralized, cryptographically governed AI agent networks.**
**Built on [Project NANDA](https://projectnanda.org) standards.**

---

## The Vision

The industry is scaling the Internet of Agents — AI agents that discover, communicate, and collaborate across the web. But the mainstream narrative assumes reliable cloud connectivity, abundant compute, and low-stakes consumer tasks.

Critical segments of the autonomous economy — aerospace, defense, maritime logistics, physical infrastructure — operate at the extreme edge. Connectivity is intermittent. Trust must be continuously verified. The penalty for an AI hallucination or unauthorized action can be severe.

To scale AI agents in the enterprise, we need more than discovery. We need **cryptographic model governance**, **offline-capable identity**, **structural regulatory compliance**, and **verifiable capability restriction**.

These libraries are the building blocks.

---

## How the libraries fit together

Each library ships a **small, versioned Protocol surface** and a **public conformance test suite**. Any third-party backend — including proprietary ones — plugs in behind the same Protocol and proves compliance against the same public tests. The open substrate is the standard; what you build above it is yours. No vendor lock-in, no forked forks.

---

## Two tiers of trust

**Model Trust** answers *"what is this model?"* — identity, metadata, integrity, approval.
**Behavioral Trust** answers *"what is this agent allowed to do, right now?"* — regulation, capability, staging.
**Federation** sits beneath both — how agents find each other on the network.

```
  +-----------------------------------------------------------+
  |                      BEHAVIORAL TRUST                     |
  |                                                           |
  |    sm-locp     →     sm-airlock    →     sm-enclave       |
  |  (compliance)     (capabilities)      (speculative exec)  |
  +-----------------------------------------------------------+
                              |
  +-----------------------------------------------------------+
  |                         MODEL TRUST                       |
  |                                                           |
  |  sm-model-       sm-model-     sm-model-       sm-model-  |
  |  provenance  →   card      →   integrity-  →   governance |
  |  (identity)     (metadata)      layer          (approval) |
  |                                (verification)             |
  +-----------------------------------------------------------+
                              |
  +-----------------------------------------------------------+
  |                         FEDERATION                        |
  |                                                           |
  |   sm-bridge  —  registry endpoints, Quilt delta sync      |
  +-----------------------------------------------------------+
```

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

The Open Compliance Protocol (OCP) — a defeasible-logic engine, machine-readable regulations (MRR) format, and W3C Verifiable Credential issuance layer. Agents observe their operational state, check it against regulatory theories, and produce cryptographic proofs of compliance that any third party can verify without re-running the evaluation.

Persistence Protocol v1 is frozen. Ship your own corpus, your own backend — the engine is indifferent as long as your implementation passes the public conformance suite.

`pip install git+https://github.com/Sharathvc23/sm-locp.git`

---

### 6. Capability Restriction — sm-airlock *(private)*

Attribute-level sandbox that restricts what agent plugins can access through allowlist-based access control, rate limiting, and effect staging with commit/discard semantics.

### 7. Decision Staging — sm-enclave *(private)*

Speculative execution sandbox that stages agent side effects in isolated contexts with irreversibility gating, priority-ordered atomic commit, and parallel branch execution with winner/loser finalization.

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
| **Zero dependencies** | All core libraries use only the Python standard library. Crypto and database backends are optional extras. |
| **Protocol-based** | Extension points use `@runtime_checkable` protocols — no forced inheritance, no vendor lock-in. |
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

# Regulatory compliance
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
| sm-airlock | 0.1.0 | 84 | None |
| sm-enclave | 0.1.0 | 84 | None |
| **Total** | | **646** | |


---

**Sharath Chandra** — Personal research contributions aligned with [Project NANDA](https://projectnanda.org) standards. [Stellarminds.ai](https://stellarminds.ai)
