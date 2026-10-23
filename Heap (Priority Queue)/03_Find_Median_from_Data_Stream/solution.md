# 💡 Find Median from Data Stream - Solution Deep Dive

## 🧠 Two-Heap Balance
- `small` (Max-heap, inverted signs in Python): holds smaller half.
- `large` (Min-heap): holds larger half.
Balance rule: `len(small)` equals `len(large)` or `len(large) + 1`.
Median is:
- `float(-small[0])` if odd number of elements.
- `(-small[0] + large[0]) / 2.0` if even.

## ⏱️ Complexity Analysis
- `addNum`: $O(\log N)$
- `findMedian`: $O(1)$
- **Space Complexity**: $O(N)$
