# 💡 Find Minimum in Rotated Sorted Array - Solution Deep Dive

## 🧠 Thought Process
Compare `nums[mid]` with `nums[high]`:
- If `nums[mid] > nums[high]`: The inflection pivot (minimum) must be strictly in the right half $\rightarrow$ `low = mid + 1`.
- If `nums[mid] <= nums[high]`: `mid` could be the minimum, or the minimum is in the left half $\rightarrow$ `high = mid`.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(\log N)$
- **Space Complexity**: $O(1)$
