"""
Problem: Max Points on a Line (LeetCode #149)
Slope Hash Map
Time Complexity: O(N^2)
Space Complexity: O(N)
"""

from collections import defaultdict
import math
from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n

        max_pts = 1
        for i in range(n):
            slopes = defaultdict(int)
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx, dy = x2 - x1, y2 - y1
                g = math.gcd(dx, dy)
                dx //= g
                dy //= g
                if dx < 0 or (dx == 0 and dy < 0):
                    dx, dy = -dx, -dy
                slope = (dx, dy)
                slopes[slope] += 1
                max_pts = max(max_pts, slopes[slope] + 1)

        return max_pts

if __name__ == "__main__":
    sol = Solution()
    assert sol.maxPoints([[1,1],[2,2],[3,3]]) == 3
    assert sol.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]) == 4
    print("✅ All Max Points on a Line tests passed!")
