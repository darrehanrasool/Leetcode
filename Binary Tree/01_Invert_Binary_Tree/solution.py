"""
Problem: Invert Binary Tree (LeetCode #226)
Recursive Mirror Swapping
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # Swap left and right children
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    inverted = sol.invertTree(root)
    assert inverted.val == 4
    assert inverted.left.val == 7
    assert inverted.right.val == 2
    print("✅ All Invert Binary Tree tests passed!")
