# 💡 Maximum Depth of Binary Tree - Solution Deep Dive

## 🧠 Thought Process (Recursion DFS)
The maximum depth of any tree is:
$$\text{depth} = 1 + \max(\text{depth}(node.left), \text{depth}(node.right))$$
Base case: `if not root: return 0`.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N)$
- **Space Complexity**: $O(H)$ where $H$ is tree height (recursion stack).
