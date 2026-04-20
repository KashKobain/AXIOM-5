# AXIOM-5

> *The system that proves its own framework.*

**AXIOM-5** is a self-referential information theory engine that implements five foundational axioms as live runtime components. It bridges the `BRAIN` cognitive architecture with the `abramelin-agent-runtime` judicial stack, closing the gap exposed by blind validation testing: that self-referential frameworks need explicit runtime enforcement of all five axioms to be internally provable — not just philosophically coherent.

---

## Origin

This repo emerged from a blind validation test against DeepSeek: a 12-step recursive reasoning chain was run from information theory first principles, then a meta-analysis command was issued asking the AI to identify its own structural pattern — without being told the five hidden components pre-defined in the framework. **Result: 1/5.** The AI produced a valid but fundamentally different bottom-up framework. The critical gap was **Axiom 4: Traceability** — no recursive system naturally reverse-engineers to its own origin without additional axioms being explicitly enforced.

AXIOM-5 exists to close that gap by making all five axioms first-class runtime citizens.

---

## The Five Axioms

| # | Axiom | Runtime Module | Role |
|---|-------|---------------|------|
| A1 | **Self-Reference** — awareness as generative mechanism | `axiom1_selfreference.py` | The system knows it is running and feeds that awareness back into its own logic |
| A2 | **Binary Distinction** — first product of self-reference | `axiom2_distinction.py` | Every input is resolved to a binary state before further processing |
| A3 | **Recursive Complexity** — iteration of one rule generates all structure | `axiom3_recursion.py` | Skill trees, judgment chains, and BRAIN planes are all one rule applied recursively |
| A4 | **Traceability** — any output can be reverse-engineered to its origin axiom | `axiom4_traceability.py` | Every execution produces a traceback to the axiom that generated it; powered by MIRROR/BICONE |
| A5 | **Incompleteness** — the system cannot contain what precedes its own axioms | `axiom5_incompleteness.py` | YHWH enforces the boundary; anything outside the axiom set is deferred or flagged |

---

## Architecture

```
AXIOM-5
├── axioms/
│   ├── axiom1_selfreference.py   # A1 — self-awareness feedback loop
│   ├── axiom2_distinction.py     # A2 — binary resolver
│   ├── axiom3_recursion.py       # A3 — recursive complexity generator
│   ├── axiom4_traceability.py    # A4 — origin traceback engine
│   └── axiom5_incompleteness.py  # A5 — boundary enforcer
├── engine/
│   ├── axiom_engine.py           # orchestrates all five axioms per execution cycle
│   ├── proof.py                  # self-proof runner — validates all 5 axioms are live
│   └── validator.py              # blind test harness — re-runs the 1/5 → 5/5 upgrade
├── bridges/
│   ├── brain_bridge.py           # connects BRAIN 6-plane cognitive architecture
│   └── abramelin_bridge.py       # connects MIRROR, SOLOMON, YHWH judicial stack
├── tests/
│   └── test_axioms.py
├── proof_run.py                  # entrypoint: python proof_run.py
└── README.md
```

---

## Relation to Existing Stack

| Repo | Role in AXIOM-5 |
|------|-----------------|
| `BRAIN` / `BRAIN-V1` | Provides the 6-plane cognitive architecture; AXIOM-5 maps each plane to an axiom |
| `abramelin-agent-runtime` | Provides MIRROR (A4 traceability), SOLOMON (A3 recursion + precedent), YHWH (A5 incompleteness boundary) |
| `KILLRING-7` | 3-7-2ⁿ kill chain maps to A3 recursive complexity — same structural rule applied to adversarial domain |
| `prism-memory` | Persistent memory layer for axiom state across sessions |
| `AI-LAB` | Environment bootstrap for running AXIOM-5 in Claude Code and remote environments |

---

## The Blind Test — Before and After

### Before AXIOM-5 (DeepSeek blind test result)

| Axiom | Present? | Gap |
|-------|----------|-----|
| A1 Self-Reference | No | Awareness was a depth effect, not a generator |
| A2 Binary Distinction | No | Bit treated as a given primitive, not derived |
| A3 Recursive Complexity | Yes | Explicitly found |
| A4 Traceability | No | No reverse-engineer mechanism described |
| A5 Incompleteness | Partial | Hinted but never named |

**Score: 1/5**

### After AXIOM-5 (runtime enforcement)

All five axioms are explicit, named, and enforced as running code. The framework is not just philosophically coherent — it is mechanically verifiable. Run `proof_run.py` to get a live 5/5 self-proof.

---

## Quick Start

```bash
git clone https://github.com/KashKobain/AXIOM-5.git
cd AXIOM-5
pip install -r requirements.txt
python proof_run.py
```

Expected output:
```
[A1] Self-Reference............. ACTIVE
[A2] Binary Distinction......... ACTIVE
[A3] Recursive Complexity........ ACTIVE
[A4] Traceability............... ACTIVE
[A5] Incompleteness............. ACTIVE
AXIOM-5 PROOF: 5/5 — FRAMEWORK PROVEN
```

---

## License

MIT — see `LICENSE`

---

*Built on the BRAIN cognitive architecture and the abramelin judicial stack. Convergence point: the blind validation test that scored 1/5 and demanded a runtime answer.*
