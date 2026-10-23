"""
Problem: Course Schedule (LeetCode #207)
Kahn's In-Degree BFS Cycle Detection
Time Complexity: O(V + E)
Space Complexity: O(V + E)
"""

from collections import deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses

        for crs, pre in prerequisites:
            adj[pre].append(crs)
            in_degree[crs] += 1

        q = deque([i for i in range(numCourses) if in_degree[i] == 0])
        completed = 0

        while q:
            node = q.popleft()
            completed += 1
            for nei in adj[node]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)

        return completed == numCourses

if __name__ == "__main__":
    sol = Solution()
    assert sol.canFinish(2, [[1, 0]]) is True
    assert sol.canFinish(2, [[1, 0], [0, 1]]) is False  # Cycle!
    print("✅ All Course Schedule tests passed!")
