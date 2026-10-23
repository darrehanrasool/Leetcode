# 💡 Network Delay Time - Solution Deep Dive

## 🧠 Thought Process (Dijkstra's Algorithm with Min-Heap)
Min-heap of `(time_so_far, node)`.
Pop node with smallest elapsed time. If not yet visited, record its shortest distance and push all neighbors.
Result is max of shortest distances to all nodes.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(E \log V)$
- **Space Complexity**: $O(V + E)$
