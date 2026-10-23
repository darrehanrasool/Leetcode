"""
Problem: Coin Change (LeetCode #322)
Bottom-Up Tabulation
Time Complexity: O(amount * len(coins))
Space Complexity: O(amount)
"""

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for a in range(coin, amount + 1):
                dp[a] = min(dp[a], 1 + dp[a - coin])

        return dp[amount] if dp[amount] != float("inf") else -1

if __name__ == "__main__":
    sol = Solution()
    assert sol.coinChange([1, 2, 5], 11) == 3
    assert sol.coinChange([2], 3) == -1
    assert sol.coinChange([1], 0) == 0
    print("✅ All Coin Change tests passed!")
