# Reinforcement Learning Trees

Efficient sum-tree and min-tree data structures for reinforcement learning workloads (e.g., prioritized experience replay buffers). Both trees are implemented with flat NumPy arrays for speed and small memory overhead.

## Features

- Sum tree with log-time updates and prefix-sum retrieval for weighted sampling.
- Min tree with log-time updates for tracking the current minimum priority.
- Simple API: just construct with a capacity, call `update`, then query with `total()`, `retrieve()`, or `min()`.
- Pure Python with a single NumPy dependency; works anywhere Python 3.9+ runs.

## Installation

```bash
pip install rltrees
```

## Quickstart

```python
import numpy as np
from rltrees import SumTree, MinTree

capacity = 8
sum_tree = SumTree(capacity)
min_tree = MinTree(capacity)

# Assign priorities/weights at specific indices
priorities = np.linspace(0.1, 0.8, capacity)
for i, p in enumerate(priorities):
    sum_tree.update(i, p)
    min_tree.update(i, p)

# Sample an index proportional to its weight
sampled_idx = sum_tree.retrieve(value=np.random.random() * sum_tree.total())

# Check the smallest priority tracked so far
lowest_priority = min_tree.min()
```

## API

- `SumTree(capacity: int)`: create a sum tree with fixed capacity.
  - `update(idx: int, value: float) -> None`: set the value at `idx`.
  - `total() -> float`: sum of all stored values.
  - `retrieve(value: float) -> int`: return the index whose prefix sum covers `value` (use `random * total()` for sampling).
- `MinTree(capacity: int)`: create a min tree with fixed capacity.
  - `update(idx: int, value: float) -> None`: set the value at `idx`.
  - `min() -> float`: smallest value stored in the tree.

All indices are zero-based and must be `< capacity`.

## Development

```bash
pip install -e ".[dev]"
```

Run your tests or scripts against the two tree classes in `rltrees/` and open issues or PRs with any findings.

## License

MIT License. See `LICENSE` for details.
