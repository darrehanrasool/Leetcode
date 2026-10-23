"""
Problem: Critical Connections in a Network (LeetCode #1192)
Tarjan's Bridge-Finding Algorithm
Time Complexity: O(V + E)
"""

from collections import defaultdict
from typing import List

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)

        discovery = [-1] * n
        lowest = [-1] * n
        bridges = []
        timer = 0

        def dfs(node, parent):
            nonlocal timer
            discovery[node] = lowest[node] = timer
            timer += 1

            for nei in adj[node]:
                if nei == parent:
                    continue
                if discovery[nei] != -1:
                    lowest[node] = min(lowest[node], discovery[nei])
                else:
                    dfs(nei, node)
                    lowest[node] = min(lowest[node], lowest[nei])
                    if lowest[nei] > discovery[node]:
                        bridges.append([node, nei])

        dfs(0, -1)
        return bridges

if __name__ == "__main__":
    sol = Solution()
    res = sol.criticalConnections(4, [[0,1],[1,2],[2,0],[1,3]])
    assert res == [[1, 3]]
    print("✅ All Strongly Connected / Critical Connections tests passed!")
