"""
Problem: Spiral Matrix (LeetCode #54)
4 Boundary Pointer Shrink
Time Complexity: O(M * N)
Space Complexity: O(1) auxiliary
"""

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix:
            return res

        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # 1. Traverse top row
            for c in range(left, right + 1):
                res.append(matrix[top][c])
            top += 1

            # 2. Traverse right column
            for r in range(top, bottom + 1):
                res.append(matrix[r][right])
            right -= 1

            # 3. Traverse bottom row if valid
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    res.append(matrix[bottom][c])
                bottom -= 1

            # 4. Traverse left column if valid
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    res.append(matrix[r][left])
                left += 1

        return res

if __name__ == "__main__":
    sol = Solution()
    assert sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5]
    assert sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1,2,3,4,8,12,11,10,9,5,6,7]
    print("✅ All Spiral Matrix tests passed!")
