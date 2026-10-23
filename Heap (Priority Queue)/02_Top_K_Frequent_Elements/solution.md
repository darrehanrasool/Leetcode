# 💡 Top K Frequent Elements - Solution Deep Dive

## 🧠 Thought Process
1. Count frequencies using `Counter(nums)`.
2. Push pairs `(count, num)` into a min-heap of size $K$.
3. Return all numbers remaining in the heap.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N \log K)$
- **Space Complexity**: $O(N)$
