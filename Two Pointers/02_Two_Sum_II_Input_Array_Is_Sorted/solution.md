# 💡 Two Sum II - Solution Deep Dive

## 🧠 Thought Process
Because the array is already **sorted**, we don't need a hash map ($O(N)$ space):
- If `numbers[left] + numbers[right] > target`: The sum is too large. Since all numbers to the right are even larger, the only way to decrease the sum is `right -= 1`.
- If `numbers[left] + numbers[right] < target`: The sum is too small. The only way to increase the sum is `left += 1`.
- If equal: We found our answer! Return `[left + 1, right + 1]` (1-indexed).

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N)$ — Pointers move inward by 1 at each step.
- **Space Complexity**: $O(1)$ — Only two integer pointers used.
