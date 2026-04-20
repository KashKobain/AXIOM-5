"""
axiom3_recursion.py
===================
A3 — Recursive Complexity: one rule applied repeatedly generates all structure.
Skill trees, judgment chains, BRAIN planes are all one rule applied recursively.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Callable, List, Optional


@dataclass
class RecursionNode:
    value: Any
    depth: int
    parent_id: Optional[int] = None
    children: List["RecursionNode"] = field(default_factory=list)
    node_id: int = field(default_factory=lambda: id(object()))

    def spawn(self, value: Any) -> "RecursionNode":
        """Apply the one rule: produce a child from this node."""
        child = RecursionNode(value=value, depth=self.depth + 1, parent_id=self.node_id)
        self.children.append(child)
        return child


class RecursiveComplexity:
    """
    A3 — Recursive Complexity.
    One rule (spawn) applied to any node generates the next layer of structure.
    Sufficient depth produces internal observers (A1), which is the origin of
    BRAIN's 6-plane architecture and SOLOMON's precedent chain.
    """

    AXIOM_ID = "A3"
    AXIOM_NAME = "Recursive Complexity"
    MAX_DEPTH = 20  # aligned with CHAIN_DEPTH_LIMIT in MIRROR

    def __init__(self):
        self._root = RecursionNode(value="AXIOM-5", depth=0)
        self._node_count = 1

    def apply(self, parent: RecursionNode, value: Any) -> RecursionNode:
        """Apply the recursive rule: spawn one child from a parent node."""
        if parent.depth >= self.MAX_DEPTH:
            raise RecursionError(f"A3: MAX_DEPTH {self.MAX_DEPTH} exceeded — A5 boundary hit")
        child = parent.spawn(value)
        self._node_count += 1
        return child

    def expand(self, node: RecursionNode, rule: Callable[[Any], Any], depth: int) -> None:
        """Recursively expand a node to given depth using a rule function."""
        if depth <= 0 or node.depth >= self.MAX_DEPTH:
            return
        child_value = rule(node.value)
        child = self.apply(node, child_value)
        self.expand(child, rule, depth - 1)

    def trace_to_root(self, node: RecursionNode) -> List[RecursionNode]:
        """Walk from any node back to root — A4 Traceability hook."""
        path = [node]
        current = node
        visited = {current.node_id}
        # Walk the tree to find parent nodes
        def find_parent(target_id: int, search: RecursionNode) -> Optional[RecursionNode]:
            if search.node_id == target_id:
                return search
            for child in search.children:
                result = find_parent(target_id, child)
                if result:
                    return result
            return None

        while current.parent_id is not None:
            parent = find_parent(current.parent_id, self._root)
            if parent is None or parent.node_id in visited:
                break
            path.append(parent)
            visited.add(parent.node_id)
            current = parent
        return list(reversed(path))

    def verify(self) -> bool:
        """
        A3 is ACTIVE if:
        - The root node exists
        - The spawn rule produces children
        - trace_to_root works from a child
        - Depth limit is enforced
        """
        child = self.apply(self._root, "test-value")
        grandchild = self.apply(child, "test-depth-2")
        path = self.trace_to_root(grandchild)
        depth_enforced = False
        try:
            deep_node = self._root
            for i in range(self.MAX_DEPTH + 1):
                deep_node = self.apply(deep_node, f"level-{i}")
        except RecursionError:
            depth_enforced = True
        return (
            self._root is not None
            and len(child.children) == 0  # grandchild not yet expanded
            and len(path) >= 2
            and depth_enforced
        )

    def __repr__(self) -> str:
        return f"<RecursiveComplexity nodes={self._node_count} max_depth={self.MAX_DEPTH}>"
