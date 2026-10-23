"""
Problem: Counting Bits (LeetCode #338)
DP + Bit Shift
Time Complexity: O(N)
Space Complexity: O(N)
"""

from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp

if __name__ == "__main__":
    sol = Solution()
    assert sol.countBits(2) == [0, 1, 1]
    assert sol.countBits(5) == [0, 1, 1, 2, 1, 2]
    print("✅ All Counting Bits tests passed!")
