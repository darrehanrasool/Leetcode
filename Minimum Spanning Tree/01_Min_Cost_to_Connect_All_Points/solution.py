"""
Problem: Min Cost to Connect All Points (LeetCode #1584)
Prim's Minimum Spanning Tree Algorithm
Time Complexity: O(N^2 log N)
Space Complexity: O(N)
"""

import heapq
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = set()
        min_heap = [(0, 0)]  # (cost, point_index)
        total_cost = 0

        while len(visited) < n:
            cost, u = heapq.heappop(min_heap)
            if u in visited:
                continue

            visited.add(u)
            total_cost += cost

            # Add edges to all unvisited nodes
            for v in range(n):
                if v not in visited:
                    dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    heapq.heappush(min_heap, (dist, v))

        return total_cost

if __name__ == "__main__":
    sol = Solution()
    assert sol.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]) == 20
    assert sol.minCostConnectPoints([[3,12],[-2,5],[-4,1]]) == 18
    print("✅ All Min Cost to Connect All Points tests passed!")
