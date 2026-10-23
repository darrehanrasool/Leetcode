"""
Problem: Unique Paths (LeetCode #62)
Combinatorics: (m+n-2) Choose (m-1)
Time Complexity: O(m)
Space Complexity: O(1)
"""

import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.comb(m + n - 2, m - 1)

if __name__ == "__main__":
    sol = Solution()
    assert sol.uniquePaths(3, 7) == 28
    assert sol.uniquePaths(3, 2) == 3
    print("✅ All Unique Paths tests passed!")
