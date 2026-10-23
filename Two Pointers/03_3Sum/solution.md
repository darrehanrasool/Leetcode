# 💡 3Sum - Solution Deep Dive

## 🧠 Thought Process
1. **Sort the array**: Allows us to use Two Pointers and easily skip duplicate values.
2. **Iterate with index `i`**: For each `nums[i]`:
   - If `nums[i] > 0`: Stop early! Since the array is sorted, three positive numbers can never sum to 0.
   - If `i > 0 and nums[i] == nums[i - 1]`: Skip to avoid duplicate triplets.
   - Set `left = i + 1`, `right = len(nums) - 1`.
   - While `left < right`:
     - `total = nums[i] + nums[left] + nums[right]`
     - If `total == 0`: record triplet, then advance `left` and `right` skipping any duplicates.
     - If `total < 0`: `left += 1`.
     - If `total > 0`: `right -= 1`.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N^2)$ — Sorting takes $O(N \log N)$, outer loop runs $N$ times with an $O(N)$ two-pointer scan.
- **Space Complexity**: $O(1)$ auxiliary space (ignoring sorting and output array).
