"""
proof_run.py
============
AXIOM-5 entrypoint. Boots all five axioms and runs the self-proof sequence.
Expected result: 5/5 — FRAMEWORK PROVEN
"""

import sys
import time
from axioms.axiom1_selfreference import SelfReference
from axioms.axiom2_distinction import BinaryDistinction
from axioms.axiom3_recursion import RecursiveComplexity
from axioms.axiom4_traceability import Traceability
from axioms.axiom5_incompleteness import Incompleteness

AXIOMS = [
    ("A1", "Self-Reference",        SelfReference),
    ("A2", "Binary Distinction",    BinaryDistinction),
    ("A3", "Recursive Complexity",  RecursiveComplexity),
    ("A4", "Traceability",          Traceability),
    ("A5", "Incompleteness",        Incompleteness),
]


def run_proof() -> int:
    print("\nAXIOM-5 :: SELF-PROOF SEQUENCE")
    print("=" * 44)
    passed = 0
    instances = []
    for tag, name, cls in AXIOMS:
        try:
            instance = cls()
            result = instance.verify()
            label = f"[{tag}] {name}"
            status = "ACTIVE" if result else "FAILED"
            print(f"{label:<35} {status}")
            if result:
                passed += 1
                instances.append(instance)
        except Exception as exc:
            print(f"[{tag}] {name:<30} ERROR: {exc}")

    print("=" * 44)
    verdict = "FRAMEWORK PROVEN" if passed == 5 else f"INCOMPLETE ({passed}/5)"
    print(f"AXIOM-5 PROOF: {passed}/5 — {verdict}")

    # A4 Traceability: emit proof trace for this run
    if passed == 5:
        tracer = next(i for i in instances if isinstance(i, Traceability))
        tracer.emit_trace(axioms=[tag for tag, _, _ in AXIOMS])

    return 0 if passed == 5 else 1


if __name__ == "__main__":
    sys.exit(run_proof())
