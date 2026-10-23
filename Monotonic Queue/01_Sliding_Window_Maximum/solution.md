# 💡 Sliding Window Maximum - Solution Deep Dive

## 🧠 Thought Process
Use a deque (monotonic decreasing queue of indices):
1. Remove indices from front if they fall outside the current window (`i - k`).
2. Remove elements from back of deque that are smaller than `nums[i]` (they can never be the maximum again).
3. Append `i` to deque.
4. If `i >= k - 1`, record `nums[deque[0]]` as the window max.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N)$ — Every element added and removed from deque at most once.
- **Space Complexity**: $O(K)$ for the deque.
