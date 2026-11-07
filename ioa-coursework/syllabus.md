# Syllabus — Internet of AI Agents

## Prerequisites

- Python 3.11+
- Public-key cryptography fundamentals (Ed25519, SHA-256, hash chains)
- HTTP APIs and JSON
- Comfort reading protocol specifications

---

## Module Map

### Module 01 — Why an Internet of Agents

**Learning outcomes:** Articulate why agent-to-agent infrastructure is a distinct problem from agent-to-human UX. Identify the five infrastructure gaps (discovery, identity, trust, delegation, accountability). Map the Project NANDA ecosystem to those gaps.

### Module 02 — Identity and Discovery

**Learning outcomes:** Construct a `did:key` identity for an agent. Describe the NANDA Index data model and AgentFacts schema. Query a registry endpoint and parse the response. Explain the difference between resolution and discovery.

### Module 03 — Registries in Practice

**Learning outcomes:** Stand up a minimal org-server. Register an agent with AgentFacts. Implement Quilt delta sync between two registries. Evaluate the tradeoffs of centralized vs federated registry topologies.

### Module 04 — Trust and Verification

**Learning outcomes:** Sign and verify a payload with Ed25519. Build and verify a hash chain. Generate and validate a conformance badge. Explain what offline verification means and why it matters.

### Module 05 — Authority and Delegation

**Learning outcomes:** Issue a Delegated Authority Token (DAT) with scope, duration, and budget constraints. Evaluate a three-valued authorization verdict. Distinguish "may" (authority) from "did" (receipt). Chain delegations and verify the full chain.

### Module 06 — Accountability Infrastructure

**Learning outcomes:** Mint an Agency Receipt. Wrap a pre-action verdict in an Attested Action Envelope. Explain SCITT transparency log semantics. Construct a Portable Agent Reputation Credential.

### Module 07 — Open Problems

**Learning outcomes:** Identify at least three unsolved problems in agent governance. Evaluate proposed approaches to discovery integrity (multi-source corroboration). Reason about multi-principal delegation conflicts. Propose a research direction and defend it.

### Module 08 — Capstone: Sovereign Agent

**Learning outcomes:** Build a minimal agent that: discovers peers via a registry, authenticates with `did:key`, obtains a delegation token, performs an authorized action, mints a receipt, and submits it to a transparency log. Defend the design in a written report.
