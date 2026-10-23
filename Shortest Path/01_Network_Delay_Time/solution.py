"""
Problem: Network Delay Time (LeetCode #743)
Dijkstra's Shortest Path Algorithm
Time Complexity: O(E log V)
Space Complexity: O(V + E)
"""

import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n + 1)]
        for u, v, w in times:
            adj[u].append((v, w))

        min_heap = [(0, k)]  # (time, node)
        visited = {}

        while min_heap:
            time, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited[node] = time

            for nei, weight in adj[node]:
                if nei not in visited:
                    heapq.heappush(min_heap, (time + weight, nei))

        return max(visited.values()) if len(visited) == n else -1

if __name__ == "__main__":
    sol = Solution()
    assert sol.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2) == 2
    assert sol.networkDelayTime([[1,2,1]], 2, 1) == 1
    assert sol.networkDelayTime([[1,2,1]], 2, 2) == -1
    print("✅ All Network Delay Time tests passed!")
