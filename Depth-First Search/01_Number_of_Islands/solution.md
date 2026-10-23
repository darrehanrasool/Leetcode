# 💡 Number of Islands - Solution Deep Dive

## 🧠 Thought Process (Flood Fill DFS)
Iterate through every cell `(r, c)`:
- If `grid[r][c] == '1'`:
  - Increment `islands_count`.
  - Trigger `dfs(r, c)` to sink/mark the entire island to `'0'`.
Return `islands_count`.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(M \times N)$
- **Space Complexity**: $O(M \times N)$ (worst case recursion stack).
