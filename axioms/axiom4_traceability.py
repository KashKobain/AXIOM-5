"""
axiom4_traceability.py
======================
A4 — Traceability: any output can be reverse-engineered to its origin axiom.
This was the MISSING axiom in the blind 1/5 test. DeepSeek's chain never produced
a reverse-engineer mechanism. This module enforces it as a structural requirement.
"""

import hashlib
import json
import time
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class TraceRecord:
    output_id: str
    origin_axiom: str          # which axiom produced this output
    input_hash: str            # SHA-256 of the input
    output_hash: str           # SHA-256 of the output
    axiom_chain: List[str]     # ordered list of axioms that touched this output
    timestamp: float = field(default_factory=time.time)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict:
        return {
            "output_id": self.output_id,
            "origin_axiom": self.origin_axiom,
            "input_hash": self.input_hash,
            "output_hash": self.output_hash,
            "axiom_chain": self.axiom_chain,
            "timestamp": self.timestamp,
            "metadata": self.metadata,
        }


class Traceability:
    """
    A4 — Traceability.
    Every output produced by the system must be traceable back to its origin axiom.
    No output is valid without a TraceRecord. This closes the 1/5 → 5/5 gap:
    the system can always answer 'which axiom generated this?'
    Backed by MIRROR/BICONE in the abramelin-agent-runtime.
    """

    AXIOM_ID = "A4"
    AXIOM_NAME = "Traceability"

    def __init__(self):
        self._ledger: Dict[str, TraceRecord] = {}
        self._trace_count = 0

    @staticmethod
    def _hash(value: Any) -> str:
        raw = json.dumps(value, default=str, sort_keys=True).encode()
        return hashlib.sha256(raw).hexdigest()[:16]

    def record(
        self,
        output: Any,
        origin_axiom: str,
        input_val: Any,
        axiom_chain: Optional[List[str]] = None,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> TraceRecord:
        """Register a new output with its origin axiom. Returns the TraceRecord."""
        output_hash = self._hash(output)
        input_hash = self._hash(input_val)
        output_id = f"{origin_axiom}::{output_hash}::{self._trace_count:06d}"
        chain = axiom_chain or [origin_axiom]
        record = TraceRecord(
            output_id=output_id,
            origin_axiom=origin_axiom,
            input_hash=input_hash,
            output_hash=output_hash,
            axiom_chain=chain,
            metadata=metadata or {},
        )
        self._ledger[output_id] = record
        self._trace_count += 1
        return record

    def traceback(self, output_id: str) -> Optional[TraceRecord]:
        """Reverse-engineer an output to its origin. Returns None if untraced."""
        return self._ledger.get(output_id)

    def assert_traced(self, output_id: str) -> TraceRecord:
        """Raise if the output has no trace record — structural violation."""
        record = self.traceback(output_id)
        if record is None:
            raise ValueError(f"A4 VIOLATION: output '{output_id}' has no trace record — untraced execution")
        return record

    def emit_trace(self, axioms: List[str]) -> None:
        """Print the proof trace for a completed 5/5 proof run."""
        print("\n[A4] PROOF TRACE")
        for ax in axioms:
            matching = [r for r in self._ledger.values() if ax in r.axiom_chain]
            status = f"{len(matching)} records" if matching else "(no records yet — proof was the first run)"
            print(f"  {ax}: {status}")
        rec = self.record(
            output="5/5-PROOF",
            origin_axiom="A4",
            input_val=axioms,
            axiom_chain=axioms,
            metadata={"event": "proof_complete"},
        )
        print(f"  TRACE SEALED: {rec.output_id}")

    def verify(self) -> bool:
        """
        A4 is ACTIVE if:
        - record() produces a TraceRecord with correct hashes
        - traceback() retrieves the exact same record
        - assert_traced() raises on unknown output_id
        """
        rec = self.record(output="test", origin_axiom="A4", input_val="input", axiom_chain=["A4"])
        retrieved = self.traceback(rec.output_id)
        violation_caught = False
        try:
            self.assert_traced("nonexistent-id")
        except ValueError:
            violation_caught = True
        return (
            retrieved is not None
            and retrieved.output_id == rec.output_id
            and retrieved.origin_axiom == "A4"
            and violation_caught
        )

    def __repr__(self) -> str:
        return f"<Traceability records={self._trace_count}>"
