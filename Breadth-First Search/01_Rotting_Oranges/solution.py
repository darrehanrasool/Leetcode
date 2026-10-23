"""
Problem: Rotting Oranges (LeetCode #994)
Multi-Source BFS
Time Complexity: O(M * N)
Space Complexity: O(M * N)
"""

from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        # Step 1: Scan grid for initial state
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        minutes = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Step 2: Multi-source BFS level by level
        while q and fresh > 0:
            minutes += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))

        return minutes if fresh == 0 else -1

if __name__ == "__main__":
    sol = Solution()
    assert sol.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]) == 4
    assert sol.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]) == -1
    assert sol.orangesRotting([[0,2]]) == 0
    print("✅ All Rotting Oranges tests passed!")
