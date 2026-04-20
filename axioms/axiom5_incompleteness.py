"""
axiom5_incompleteness.py
========================
A5 — Incompleteness: the system cannot contain what precedes its own axioms.
YHWH enforces this boundary. Anything outside the axiom set is deferred or flagged.
Based on Goedel's incompleteness: no consistent formal system can prove all truths
within its own framework without referencing something outside itself.
"""

from enum import Enum
from typing import Any, List, Optional


class BoundaryVerdict(Enum):
    WITHIN = "WITHIN"       # claim is expressible inside the axiom set
    DEFERRED = "DEFERRED"   # claim references something before the axioms
    FLAGGED = "FLAGGED"     # claim violates boundary structurally


class AxiomBoundaryError(Exception):
    """Raised when a claim exceeds the system's own axiom boundary."""


class Incompleteness:
    """
    A5 — Incompleteness.
    The system has a defined axiom set {A1, A2, A3, A4, A5}.
    Any claim that requires truth from OUTSIDE this set cannot be proven
    from within it. YHWH's Torah loop enforces this: commandment → judgment
    → reflection. Reflection that hits the boundary produces a DEFERRED verdict,
    not a failure — because the boundary is itself an axiom.
    """

    AXIOM_ID = "A5"
    AXIOM_NAME = "Incompleteness"
    AXIOM_SET = frozenset({"A1", "A2", "A3", "A4", "A5"})

    def __init__(self):
        self._boundary_hits: List[dict] = []
        self._within_count = 0
        self._deferred_count = 0
        self._flagged_count = 0

    def evaluate(self, claim: Any, axiom_chain: Optional[List[str]] = None) -> BoundaryVerdict:
        """
        Evaluate whether a claim is within, deferred, or flagged.
        - WITHIN: all axioms in the chain are in AXIOM_SET
        - DEFERRED: chain references something outside AXIOM_SET (pre-axiomatic)
        - FLAGGED: claim is None, empty, or structurally invalid
        """
        if claim is None or claim == "":
            self._flagged_count += 1
            self._boundary_hits.append({"claim": claim, "verdict": BoundaryVerdict.FLAGGED})
            return BoundaryVerdict.FLAGGED

        chain = axiom_chain or []
        outside = [ax for ax in chain if ax not in self.AXIOM_SET]

        if outside:
            self._deferred_count += 1
            self._boundary_hits.append({
                "claim": claim,
                "verdict": BoundaryVerdict.DEFERRED,
                "outside_references": outside,
            })
            return BoundaryVerdict.DEFERRED

        self._within_count += 1
        return BoundaryVerdict.WITHIN

    def assert_within(self, claim: Any, axiom_chain: Optional[List[str]] = None) -> None:
        """
        Raise AxiomBoundaryError if the claim is not WITHIN the axiom set.
        Used by YHWH as the Torah commandment gate.
        """
        verdict = self.evaluate(claim, axiom_chain)
        if verdict != BoundaryVerdict.WITHIN:
            raise AxiomBoundaryError(
                f"A5 BOUNDARY: claim '{claim}' verdict={verdict.value} — "
                f"outside the axiom set or pre-axiomatic"
            )

    def boundary_report(self) -> dict:
        """Return a summary of boundary evaluations for reflection."""
        return {
            "within": self._within_count,
            "deferred": self._deferred_count,
            "flagged": self._flagged_count,
            "hits": list(self._boundary_hits),
        }

    def verify(self) -> bool:
        """
        A5 is ACTIVE if:
        - WITHIN claims pass assert_within without error
        - DEFERRED claims are correctly flagged when chain references outside the axiom set
        - FLAGGED claims are caught for None/empty
        - AxiomBoundaryError is raised on non-WITHIN claims
        """
        # WITHIN: valid claim inside axiom set
        verdict_within = self.evaluate("valid-claim", ["A1", "A2"])

        # DEFERRED: chain references something outside
        verdict_deferred = self.evaluate("outside-claim", ["A1", "EXTERNAL"])

        # FLAGGED: None claim
        verdict_flagged = self.evaluate(None)

        # AxiomBoundaryError on assert
        boundary_enforced = False
        try:
            self.assert_within("pre-axiomatic", ["GODEL", "EXTERNAL"])
        except AxiomBoundaryError:
            boundary_enforced = True

        return (
            verdict_within == BoundaryVerdict.WITHIN
            and verdict_deferred == BoundaryVerdict.DEFERRED
            and verdict_flagged == BoundaryVerdict.FLAGGED
            and boundary_enforced
        )

    def __repr__(self) -> str:
        return (
            f"<Incompleteness within={self._within_count} "
            f"deferred={self._deferred_count} flagged={self._flagged_count}>"
        )
