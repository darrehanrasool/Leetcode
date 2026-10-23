# 💡 Validate Binary Search Tree - Solution Deep Dive

## 🧠 Thought Process (Range Propagation)
Every node must be bounded by valid minimum and maximum thresholds:
- Root is bounded by `(-inf, +inf)`.
- Left child is bounded by `(min_val, root.val)`.
- Right child is bounded by `(root.val, max_val)`.
If any node violates its range, return `False`.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N)$
- **Space Complexity**: $O(H)$
