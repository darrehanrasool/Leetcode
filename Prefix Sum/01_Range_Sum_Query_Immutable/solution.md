# 💡 Range Sum Query - Solution Deep Dive

## 🧠 Thought Process
Precompute `prefix[i] = sum(nums[0...i-1])`.
Then `sumRange(left, right) = prefix[right + 1] - prefix[left]`.

## ⏱️ Complexity Analysis
- **Precomputation**: $O(N)$
- **Query Time**: $O(1)$
- **Space Complexity**: $O(N)$
