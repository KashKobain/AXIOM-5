"""
axiom2_distinction.py
=====================
A2 — Binary Distinction: first product of self-reference.
Every input is resolved to a binary state before further processing.
"""

from enum import Enum
from typing import Any, Tuple


class State(Enum):
    ONE = 1
    ZERO = 0


class BinaryDistinction:
    """
    A2 — Binary Distinction.
    The minimal act of self-reference produces a distinction: inside vs outside,
    1 vs 0, included vs excluded. This module enforces that every input to the
    system passes through a binary resolver before it can generate further complexity.
    """

    AXIOM_ID = "A2"
    AXIOM_NAME = "Binary Distinction"

    def __init__(self):
        self._resolve_count = 0
        self._distinction_log: list[Tuple[Any, State]] = []

    def resolve(self, value: Any) -> State:
        """
        Collapse any input to a binary State.
        Truthy → State.ONE, Falsy → State.ZERO.
        The resolution itself is logged (A4 traceability hook).
        """
        result = State.ONE if value else State.ZERO
        self._resolve_count += 1
        self._distinction_log.append((value, result))
        return result

    def distinguish(self, a: Any, b: Any) -> Tuple[State, State]:
        """Resolve two values and return their binary pair — the minimal distinction."""
        return self.resolve(a), self.resolve(b)

    def verify(self) -> bool:
        """
        A2 is ACTIVE if:
        - The resolver is callable and returns a valid State for both truthy and falsy inputs
        - The distinction log is accessible (traceability hook is live)
        """
        test_one = self.resolve(True)
        test_zero = self.resolve(False)
        test_null = self.resolve(None)
        return (
            test_one == State.ONE
            and test_zero == State.ZERO
            and test_null == State.ZERO
            and self._resolve_count > 0
        )

    def log(self) -> list:
        """Return the full distinction log for A4 traceability."""
        return list(self._distinction_log)

    def __repr__(self) -> str:
        return f"<BinaryDistinction resolutions={self._resolve_count}>"
