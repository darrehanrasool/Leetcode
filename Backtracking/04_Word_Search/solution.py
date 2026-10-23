"""
Problem: Word Search (LeetCode #79)
Grid Backtracking
Time Complexity: O(M * N * 4^L)
"""

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
                return False

            temp = board[r][c]
            board[r][c] = "#"  # Mark visited in-place

            found = (dfs(r + 1, c, i + 1) or
                     dfs(r - 1, c, i + 1) or
                     dfs(r, c + 1, i + 1) or
                     dfs(r, c - 1, i + 1))

            board[r][c] = temp  # Backtrack
            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False

if __name__ == "__main__":
    sol = Solution()
    b = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    assert sol.exist(b, "ABCCED") is True
    assert sol.exist(b, "SEE") is True
    assert sol.exist(b, "ABCB") is False
    print("✅ All Word Search tests passed!")
