# 💡 Search in Rotated Sorted Array - Solution Deep Dive

## 🧠 Thought Process
At index `mid`:
1. Check if `nums[low] <= nums[mid]` (Left half is sorted):
   - If `nums[low] <= target < nums[mid]`: target is in left half $\rightarrow$ `high = mid - 1`.
   - Else: search right half $\rightarrow$ `low = mid + 1`.
2. Else (Right half is sorted):
   - If `nums[mid] < target <= nums[high]`: target is in right half $\rightarrow$ `low = mid + 1`.
   - Else: search left half $\rightarrow$ `high = mid - 1`.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(\log N)$
- **Space Complexity**: $O(1)$
