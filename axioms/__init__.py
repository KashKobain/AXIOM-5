# axioms package
from .axiom1_selfreference import SelfReference
from .axiom2_distinction import BinaryDistinction
from .axiom3_recursion import RecursiveComplexity
from .axiom4_traceability import Traceability
from .axiom5_incompleteness import Incompleteness

__all__ = [
    "SelfReference",
    "BinaryDistinction",
    "RecursiveComplexity",
    "Traceability",
    "Incompleteness",
]
