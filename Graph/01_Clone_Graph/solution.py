"""
Problem: Clone Graph (LeetCode #133)
DFS Hash Map Graph Deep Copy
Time Complexity: O(V + E)
Space Complexity: O(V)
"""

from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        old_to_new = {}

        def dfs(curr):
            if curr in old_to_new:
                return old_to_new[curr]

            copy = Node(curr.val)
            old_to_new[curr] = copy

            for nei in curr.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy

        return dfs(node)

if __name__ == "__main__":
    sol = Solution()
    n1 = Node(1)
    n2 = Node(2)
    n1.neighbors.append(n2)
    n2.neighbors.append(n1)
    cloned = sol.cloneGraph(n1)
    assert cloned.val == 1
    assert cloned.neighbors[0].val == 2
    assert cloned is not n1  # Must be a distinct deep copy object!
    print("✅ All Clone Graph tests passed!")
