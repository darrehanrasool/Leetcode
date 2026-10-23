# 💡 Binary Search - Solution Deep Dive

## 🧠 Thought Process
Maintain search interval `[low, high]`:
- `mid = low + (high - low) // 2` (avoids 32-bit integer overflow).
- If `nums[mid] == target`: found!
- If `nums[mid] < target`: target is in right half $\rightarrow$ `low = mid + 1`.
- If `nums[mid] > target`: target is in left half $\rightarrow$ `high = mid - 1`.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(\log N)$
- **Space Complexity**: $O(1)$
