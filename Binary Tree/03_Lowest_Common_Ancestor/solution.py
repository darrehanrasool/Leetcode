"""
Problem: Lowest Common Ancestor of a Binary Tree (LeetCode #236)
Post-Order Recursive Search
Time Complexity: O(N)
Space Complexity: O(H)
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If p and q found in left and right subtrees, root is LCA
        if left and right:
            return root

        return left if left else right

if __name__ == "__main__":
    sol = Solution()
    r = TreeNode(3)
    p = TreeNode(5)
    q = TreeNode(1)
    r.left = p
    r.right = q
    assert sol.lowestCommonAncestor(r, p, q) == r
    print("✅ All Lowest Common Ancestor tests passed!")
