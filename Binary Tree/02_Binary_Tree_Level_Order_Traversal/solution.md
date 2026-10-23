# 💡 Binary Tree Level Order Traversal - Solution Deep Dive

## 🧠 Thought Process (BFS with Queue)
Use `collections.deque`:
For each level, record `len(queue)`. Pop that many nodes, record their values, and enqueue their children.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N)$
- **Space Complexity**: $O(N)$ (max width of tree).
