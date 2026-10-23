"""
Problem: Binary Tree Level Order Traversal (LeetCode #102)
Queue-Based BFS Level Order
Time Complexity: O(N)
Space Complexity: O(N)
"""

from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        q = deque([root])

        while q:
            level_size = len(q)
            current_level = []

            for _ in range(level_size):
                node = q.popleft()
                current_level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(current_level)

        return res

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert sol.levelOrder(root) == [[3], [9, 20], [15, 7]]
    print("✅ All Level Order Traversal tests passed!")
