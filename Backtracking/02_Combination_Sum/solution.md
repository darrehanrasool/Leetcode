# 💡 Combination Sum - Solution Deep Dive

## 🧠 Thought Process
Backtracking recursion where elements can be reused unlimited times.
At each index `i`:
- If `total == target`: record combination.
- If `total > target` or `i >= len(candidates)`: return.
- Include `candidates[i]` (stay at index `i`).
- Backtrack, then explore without `candidates[i]` (advance to `i + 1`).
