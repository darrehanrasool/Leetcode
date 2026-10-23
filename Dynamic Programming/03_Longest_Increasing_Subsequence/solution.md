# 💡 Longest Increasing Subsequence - Solution Deep Dive

## 🧠 Approaches
1. **Dynamic Programming ($O(N^2)$)**:
   `dp[i] = 1 + max(dp[j])` for all `j < i` where `nums[j] < nums[i]`.
2. **Patience Sorting + Binary Search ($O(N \log N)$)**:
   Maintain active card piles with `bisect_left`.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N \log N)$
- **Space Complexity**: $O(N)$
