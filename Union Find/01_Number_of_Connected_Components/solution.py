"""
Problem: Number of Connected Components in an Undirected Graph (LeetCode #323)
Disjoint Set Union (DSU) with Path Compression & Union by Rank
Time Complexity: O(E * alpha(V))
Space Complexity: O(V)
"""

from typing import List

class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.count = n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # Already in same component

        # Union by rank
        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        self.count -= 1
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = UnionFind(n)
        for u, v in edges:
            dsu.union(u, v)
        return dsu.count

if __name__ == "__main__":
    sol = Solution()
    assert sol.countComponents(5, [[0, 1], [1, 2], [3, 4]]) == 2
    assert sol.countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) == 1
    print("✅ All Number of Connected Components tests passed!")
