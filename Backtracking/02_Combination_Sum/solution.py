"""
Problem: Combination Sum (LeetCode #39)
Backtracking with Element Reuse
"""

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if total > target or i >= len(candidates):
                return

            # Include candidates[i]
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])

            # Backtrack
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res

if __name__ == "__main__":
    sol = Solution()
    assert sol.combinationSum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
    assert sol.combinationSum([2], 1) == []
    print("✅ All Combination Sum tests passed!")
