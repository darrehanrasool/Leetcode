"""
Problem: Validate Binary Search Tree (LeetCode #98)
Range Propagation DFS
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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)

        return validate(root, float("-inf"), float("inf"))

if __name__ == "__main__":
    sol = Solution()
    t1 = TreeNode(2, TreeNode(1), TreeNode(3))
    t2 = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    assert sol.isValidBST(t1) is True
    assert sol.isValidBST(t2) is False
    print("✅ All Validate BST tests passed!")
