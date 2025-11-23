import numpy


class MinTree:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.tree_size = 2 * capacity - 1
        self.tree = numpy.full(self.tree_size, float("inf"), dtype=numpy.float32)

    def _propagate(self, idx) -> None:
        parent = (idx - 1) // 2
        while parent >= 0:
            self.tree[parent] = min(
                self.tree[parent * 2 + 1], self.tree[parent * 2 + 2]
            )
            parent = (parent - 1) // 2

    def update(self, idx, value) -> None:
        tree_idx = idx + self.capacity - 1
        self.tree[tree_idx] = value
        self._propagate(tree_idx)

    def min(self) -> float:
        return self.tree[0]
