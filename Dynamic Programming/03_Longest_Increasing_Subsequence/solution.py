"""
Problem: Longest Increasing Subsequence (LeetCode #300)
Patience Sorting with Binary Search
Time Complexity: O(N log N)
Space Complexity: O(N)
"""

from bisect import bisect_left
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []

        for x in nums:
            idx = bisect_left(tails, x)
            if idx == len(tails):
                tails.append(x)
            else:
                tails[idx] = x

        return len(tails)

if __name__ == "__main__":
    sol = Solution()
    assert sol.lengthOfLIS([10,9,2,5,3,7,101,18]) == 4
    assert sol.lengthOfLIS([0,1,0,3,2,3]) == 4
    assert sol.lengthOfLIS([7,7,7,7,7,7,7]) == 1
    print("✅ All Longest Increasing Subsequence tests passed!")
