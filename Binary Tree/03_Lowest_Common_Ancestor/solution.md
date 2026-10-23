# 💡 Lowest Common Ancestor - Solution Deep Dive

## 🧠 Thought Process
Post-order DFS traversal:
- If current node is `p` or `q` or `None`, return `root`.
- Recurse on `left` and `right`.
- If both `left` and `right` return non-None, `root` is their Lowest Common Ancestor!
- Otherwise return whichever child returned non-None.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N)$
- **Space Complexity**: $O(H)$
