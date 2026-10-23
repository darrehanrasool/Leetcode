"""
Problem: Set Matrix Zeroes (LeetCode #73)
In-Place O(1) Auxiliary Space
Time Complexity: O(M * N)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        first_row_zero = any(matrix[0][c] == 0 for c in range(cols))
        first_col_zero = any(matrix[r][0] == 0 for r in range(rows))

        # Use first row and column as markers
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        # Zero out inner cells based on markers
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # Handle first row and col
        if first_row_zero:
            for c in range(cols):
                matrix[0][c] = 0
        if first_col_zero:
            for r in range(rows):
                matrix[r][0] = 0

if __name__ == "__main__":
    sol = Solution()
    m = [[1,1,1],[1,0,1],[1,1,1]]
    sol.setZeroes(m)
    assert m == [[1,0,1],[0,0,0],[1,0,1]]
    print("✅ All Set Matrix Zeroes tests passed!")
