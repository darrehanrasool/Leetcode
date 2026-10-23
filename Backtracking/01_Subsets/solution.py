"""
Problem: Subsets (LeetCode #78)
Backtracking Power Set Generation
Time Complexity: O(N * 2^N)
Space Complexity: O(N)
"""

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            # Decision 1: Include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # Backtrack
            subset.pop()

            # Decision 2: Do NOT include nums[i]
            dfs(i + 1)

        dfs(0)
        return res

if __name__ == "__main__":
    sol = Solution()
    res = sol.subsets([1, 2, 3])
    assert len(res) == 8
    assert [] in res and [1, 2, 3] in res
    print("✅ All Subsets tests passed!")
