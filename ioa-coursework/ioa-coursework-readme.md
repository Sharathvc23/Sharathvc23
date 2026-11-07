# Internet of AI Agents — Open Coursework

**An 8-module, open-source course exploring the infrastructure layer for decentralized AI agent networks. A contribution to the [Project NANDA](https://projectnanda.org) ecosystem.**

[StellarMinds.ai](https://stellarminds.ai)

---

## Modules

| # | Module | Description |
|---|--------|-------------|
| 01 | [Why an Internet of Agents](modules/01-why-an-internet-of-agents/) | The problem space: why agents need discovery, identity, trust, and accountability infrastructure |
| 02 | [Identity and Discovery](modules/02-identity-and-discovery/) | DIDs, AgentFacts, the NANDA Index, and how agents find each other |
| 03 | [Registries in Practice](modules/03-registries-in-practice/) | Quilt federation, org-servers, delta sync, and the registry operator's responsibilities |
| 04 | [Trust and Verification](modules/04-trust-and-verification/) | Ed25519 signing, hash chains, conformance badges, and offline verification |
| 05 | [Authority and Delegation](modules/05-authority-and-delegation/) | Delegated Authority Tokens, three-valued verdicts, the "may" vs "did" distinction |
| 06 | [Accountability Infrastructure](modules/06-accountability-infrastructure/) | Agency receipts, attested action envelopes, SCITT transparency logs, reputation credentials |
| 07 | [Open Problems](modules/07-open-problems/) | Unsolved questions in agent governance, discovery integrity, and multi-principal delegation |
| 08 | [Capstone: Sovereign Agent](modules/08-capstone-sovereign-agent/) | Build a minimal agent that discovers, authenticates, delegates, acts, and accounts for itself |

## Prerequisites

- Comfortable reading and writing Python 3.11+
- Familiarity with public-key cryptography concepts (signing, verification, hash functions)
- Basic understanding of HTTP APIs and JSON
- No prior knowledge of Project NANDA or agent protocols required

## Getting Started

```bash
git clone https://github.com/Sharathvc23/Sharathvc23.git
cd Sharathvc23/ioa-coursework

# Verify the scaffold
python scripts/check_links.py
bash scripts/run_examples.sh
```

Then open `modules/01-why-an-internet-of-agents/README.md` and begin.

## Repository Structure

```
ioa-coursework/
├── CLAUDE.md                 # Session rules for building this coursework
├── ioa-coursework-readme.md  # This file
├── syllabus.md               # One-page module map
├── CONTRIBUTING.md            # How to contribute
├── LICENSE                    # MIT
├── modules/
│   ├── 01-why-an-internet-of-agents/
│   ├── 02-identity-and-discovery/
│   ├── 03-registries-in-practice/
│   ├── 04-trust-and-verification/
│   ├── 05-authority-and-delegation/
│   ├── 06-accountability-infrastructure/
│   ├── 07-open-problems/
│   └── 08-capstone-sovereign-agent/
├── shared/
│   ├── glossary.md            # Canonical terms, seeded in Phase 1
│   └── diagrams/              # Mermaid and SVG sources
├── scripts/
│   ├── check_links.py         # Validates internal markdown links
│   ├── run_examples.sh        # Runs all examples/*.py files
│   └── new_journal_entry.py   # Scaffolds a dated journal entry
├── journal/                   # Append-only build log
└── .github/workflows/ci.yml  # CI: link check + example runner
```

## Journal

The [journal/](journal/) directory is an append-only build log. Each session that modifies this coursework adds at least one entry documenting what was built, what broke, and what decisions were made. See [journal/README.md](journal/README.md) for the protocol.
