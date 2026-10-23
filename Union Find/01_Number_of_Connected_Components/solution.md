# 💡 Number of Connected Components - Solution Deep Dive

## 🧠 Thought Process (Disjoint Set Union with Path Compression)
Start with `count = n`.
For each edge `(u, v)`:
- If `find(u) != find(v)`, union them and decrement `count -= 1`.
Return `count`.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(E \cdot \alpha(V)) \approx O(E)$
- **Space Complexity**: $O(V)$
