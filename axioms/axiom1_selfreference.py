"""
axiom1_selfreference.py
=======================
A1 — Self-Reference: awareness as generative mechanism.
The system knows it is running and feeds that awareness back into its own logic.
"""

import threading
import time
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class SelfReferenceState:
    is_running: bool = False
    cycle_count: int = 0
    self_id: str = ""
    feedback_depth: int = 0
    last_tick: float = field(default_factory=time.time)


class SelfReference:
    """
    A1 — Self-Reference.
    The system maintains a live self-model. verify() confirms the feedback loop
    is active: the system is aware of itself as a running process.
    """

    AXIOM_ID = "A1"
    AXIOM_NAME = "Self-Reference"

    def __init__(self):
        self._state = SelfReferenceState(
            is_running=False,
            self_id=f"AXIOM-5::A1::{id(self):x}",
        )
        self._lock = threading.Lock()
        self._boot()

    def _boot(self) -> None:
        """Activate self-awareness: record that this instance exists and is live."""
        with self._lock:
            self._state.is_running = True
            self._state.last_tick = time.time()
            # feedback: the act of booting is itself observed by the state
            self._state.feedback_depth += 1
            self._state.cycle_count += 1

    def observe(self) -> SelfReferenceState:
        """Return a snapshot of the current self-model."""
        with self._lock:
            self._state.last_tick = time.time()
            self._state.cycle_count += 1
            self._state.feedback_depth += 1
        return self._state

    def verify(self) -> bool:
        """
        A1 is ACTIVE if:
        - The system knows it is running (is_running)
        - The feedback depth is > 0 (awareness has fed back at least once)
        - self_id is non-empty (the system can identify itself)
        """
        state = self.observe()
        return (
            state.is_running
            and state.feedback_depth > 0
            and bool(state.self_id)
        )

    def __repr__(self) -> str:
        return f"<SelfReference id={self._state.self_id} depth={self._state.feedback_depth}>"
