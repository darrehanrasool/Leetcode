# 💡 Rotting Oranges - Solution Deep Dive

## 🧠 Thought Process (Multi-Source BFS)
1. Count fresh oranges and add all rotten orange coordinates `(r, c)` to a queue.
2. If fresh == 0, return 0.
3. While queue and fresh > 0:
   - For each orange at current minute:
     - Check 4 neighbors (up, down, left, right).
     - If neighbor is fresh, rot it, decrement fresh, enqueue neighbor.
   - Increment minutes elapsed.
4. Return minutes if fresh == 0 else -1.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(M \times N)$
- **Space Complexity**: $O(M \times N)$
