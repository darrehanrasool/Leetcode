# 💡 Min Cost to Connect All Points - Solution Deep Dive

## 🧠 Thought Process (Prim's MST Algorithm)
Start at node 0. Add all connecting Manhattan distance edges to a min-heap.
Repeatedly pop the smallest edge that connects to an unvisited point until all points are connected.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N^2 \log N)$
- **Space Complexity**: $O(N^2)$
