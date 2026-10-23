# 💡 Counting Bits - Solution Deep Dive

## 🧠 DP + Bit Manipulation
`dp[i] = dp[i >> 1] + (i & 1)`:
Shifting right by 1 removes the last bit, which we have already calculated.
We add `1` if the current number is odd (`i & 1`).

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N)$
- **Space Complexity**: $O(N)$
