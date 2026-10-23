"""
Problem: Maximum Depth of Binary Tree (LeetCode #104)
DFS Recursion
Time Complexity: O(N)
Space Complexity: O(H)
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

if __name__ == "__main__":
    sol = Solution()
    # Tree: [3, 9, 20, None, None, 15, 7]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))
    assert sol.maxDepth(root) == 3
    print("✅ All Maximum Depth tests passed!")
