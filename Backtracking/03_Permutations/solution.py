"""
Problem: Permutations (LeetCode #46)
Backtracking Permutation Generation
Time Complexity: O(N * N!)
"""

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(perm, visited):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for num in nums:
                if num not in visited:
                    visited.add(num)
                    perm.append(num)
                    backtrack(perm, visited)
                    perm.pop()
                    visited.remove(num)

        backtrack([], set())
        return res

if __name__ == "__main__":
    sol = Solution()
    res = sol.permute([1, 2, 3])
    assert len(res) == 6
    print("✅ All Permutations tests passed!")
