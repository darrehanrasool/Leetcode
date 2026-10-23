"""
Problem: Course Schedule II (LeetCode #210)
Kahn's Topological Sort Ordering
Time Complexity: O(V + E)
Space Complexity: O(V + E)
"""

from collections import deque
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses

        for crs, pre in prerequisites:
            adj[pre].append(crs)
            in_degree[crs] += 1

        q = deque([i for i in range(numCourses) if in_degree[i] == 0])
        order = []

        while q:
            node = q.popleft()
            order.append(node)
            for nei in adj[node]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)

        return order if len(order) == numCourses else []

if __name__ == "__main__":
    sol = Solution()
    assert sol.findOrder(2, [[1, 0]]) == [0, 1]
    assert sol.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]) in [[0, 1, 2, 3], [0, 2, 1, 3]]
    assert sol.findOrder(2, [[1, 0], [0, 1]]) == []
    print("✅ All Course Schedule II tests passed!")
