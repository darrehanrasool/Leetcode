# 💡 Jump Game - Solution Deep Dive

## 🧠 Thought Process
Walk backwards from final goal:
Set `goal = len(nums) - 1`.
For `i` from `len(nums) - 2` down to 0:
- If `i + nums[i] >= goal`: we can reach goal from `i`! Shift `goal = i`.
Return `goal == 0`.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N)$
- **Space Complexity**: $O(1)$
