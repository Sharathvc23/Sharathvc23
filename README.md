# The Enterprise Internet of Agents

**Open-source primitives for decentralized, cryptographically governed AI agent networks.**
**Built on [Project NANDA](https://projectnanda.org) standards.**

---

## The Vision

The industry is scaling the Internet of Agents — AI agents that discover, communicate, and collaborate across the web. But the mainstream narrative assumes reliable cloud connectivity, abundant compute, and low-stakes consumer tasks.

Critical segments of the autonomous economy — aerospace, defense, maritime logistics, physical infrastructure — operate at the extreme edge. Connectivity is intermittent. Trust must be continuously verified. The penalty for an AI hallucination or unauthorized action can be severe.

To scale AI agents in the enterprise, we need more than discovery. We need **cryptographic model governance**, **offline-capable identity**, and **structural regulatory compliance**.

These five libraries are the building blocks.

---

## The Architecture of Trust

Five composable libraries. Use independently or stack together for a mathematically verifiable agent ecosystem.

```
                    +---------------------------+
                    |        sm-bridge          |   Transport & Federation
                    |  Registry endpoints,      |   "How is it exposed?"
                    |  Quilt delta sync         |
                    +-------------+-------------+
                                  |
                    +-------------+-------------+
                    |   sm-model-governance     |   Execution & Compliance
                    |  3-plane separation,      |   "Has it been approved?"
                    |  Ed25519 signing, drift   |
                    +-------------+-------------+
                                  |
                    +-------------+-------------+
                    |  sm-model-integrity-      |   Cryptographic Verification
                    |          layer            |   "Is it tamper-free?"
                    |  Hashing, attestation,    |
                    |  lineage, policy gates    |
                    +-------------+-------------+
                                  |
                    +-------------+-------------+
                    |     sm-model-card         |   Metadata & Lifecycle
                    |  20-field schema, 4 model |   "What is this model?"
                    |  types, lifecycle FSM     |
                    +-------------+-------------+
                                  |
                    +-------------+-------------+
                    |   sm-model-provenance     |   Base Identity
                    |  8-field dataclass,       |   "Where did it come from?"
                    |  3 serialization targets  |
                    +---------------------------+
```

---

### 1. Transport & Federation — [`sm-bridge`](https://github.com/Sharathvc23/sm-bridge)

> Exposing enterprise agents to a federated network should not require rewriting an entire database or implementing complex sync protocols from scratch.

A reference implementation for NANDA-compatible registry endpoints and Quilt-style delta synchronization. Drop-in FastAPI router, DID/handle parsing, thread-safe delta store, and a protocol-based converter for integrating with any internal data model.

`pip install git+https://github.com/Sharathvc23/sm-bridge.git`

---

### 2. Base Identity — [`sm-model-provenance`](https://github.com/Sharathvc23/sm-model-provenance)

> Agents need a standardized way to broadcast who they are and what model powers them, without heavy dependencies in constrained edge environments.

A zero-dependency Python dataclass capturing core model identity (model ID, provider, version, governance tier). Omit-when-empty serialization keeps payloads compact. Maps into the JSON shapes required by NANDA AgentFacts and decision envelopes.

`pip install git+https://github.com/Sharathvc23/sm-model-provenance.git`

---

### 3. Metadata & Lifecycle — [`sm-model-card`](https://github.com/Sharathvc23/sm-model-card)

> Enterprise environments require structured documentation of an AI's capabilities, training metrics, and deployment lifecycle.

A unified model card schema for federated registries. Covers LoRA adapters, edge ONNX, federated learning, and heuristic models under a single validated dataclass. Four-state lifecycle (shadow → ready → deprecated → archived) with transition guards.

`pip install git+https://github.com/Sharathvc23/sm-model-card.git`

---

### 4. Cryptographic Verification — [`sm-model-integrity-layer`](https://github.com/Sharathvc23/sm-model-integrity-layer)

> In a decentralized network, systems must mathematically verify an agent hasn't been compromised in transit or loaded with unauthorized model weights.

An additive integrity gate. Offline SHA-256 weight hashing, HMAC-SHA256 attestation, model lineage tracking, and 6 built-in governance policies. Prevents base-swapping attacks. Zero runtime dependencies.

`pip install git+https://github.com/Sharathvc23/sm-model-integrity-layer.git`

---

### 5. Execution & Compliance — [`sm-model-governance`](https://github.com/Sharathvc23/sm-model-governance)

> AI cannot autonomously execute high-stakes actions without a legally defensible audit trail and verifiable oversight.

Three-plane ML governance (Training → Approval → Serving). Ed25519 cryptographic signatures, M-of-N multi-party quorum, time-bounded approvals, and autonomous drift detection with auto-revocation. Designed for aerospace and defense compliance frameworks.

`pip install git+https://github.com/Sharathvc23/sm-model-governance.git`

---

### 6. Capability Restriction — sm-airlock

Attribute-level sandbox that restricts what agent plugins can access through allowlist-based access control, rate limiting, and effect staging with commit/discard semantics.

### 7. Decision Staging — sm-enclave

Speculative execution sandbox that stages agent side effects in isolated contexts with irreversibility gating, priority-ordered atomic commit, and parallel branch execution with winner/loser finalization.

---

## Design Principles

| Principle | How |
|-----------|-----|
| **Zero dependencies** | All core libraries use only the Python standard library. Crypto and database backends are optional extras. |
| **Protocol-based** | Extension points use `@runtime_checkable` protocols — no forced inheritance, no vendor lock-in. |
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
| sm-airlock | 0.1.0 | 84 | None |
| sm-enclave | 0.1.0 | 84 | None |
| **Total** | | **544** | |


---

**Sharath Chandra** — [stellarminds.ai](https://stellarminds.ai) — Research Contribution to [Project NANDA](https://projectnanda.org)
