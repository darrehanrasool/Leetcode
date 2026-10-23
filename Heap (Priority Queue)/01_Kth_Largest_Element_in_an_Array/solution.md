# 💡 Kth Largest Element - Solution Deep Dive

## 🧠 Thought Process (Min-Heap of size K)
Maintain a min-heap of size $K$:
- For each `num` in `nums`:
  - `heappush(heap, num)`
  - If `len(heap) > k`: `heappop(heap)` (evicts the smallest).
After scanning all numbers, the root of the heap is the $K$-th largest element!

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N \log K)$
- **Space Complexity**: $O(K)$
