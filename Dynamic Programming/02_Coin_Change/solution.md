# 💡 Coin Change - Solution Deep Dive

## 🧠 Thought Process (Bottom-Up Tabulation)
`dp[a]` represents the minimum coins needed to make amount `a`.
Initialize `dp = [inf] * (amount + 1)`, `dp[0] = 0`.
For each coin:
- For `a` from `coin` to `amount`:
  `dp[a] = min(dp[a], 1 + dp[a - coin])`

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(\text{amount} \times \text{len(coins)})$
- **Space Complexity**: $O(\text{amount})$
