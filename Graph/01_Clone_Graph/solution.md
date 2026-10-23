# 💡 Clone Graph - Solution Deep Dive

## 🧠 Thought Process
Use a hash map `old_to_new = {}` to map each original node to its newly cloned copy.
DFS traversal:
- If `node in old_to_new`: return `old_to_new[node]`.
- Create `copy = Node(node.val)`.
- Record `old_to_new[node] = copy`.
- For each neighbor, recursively clone and append to `copy.neighbors`.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(V + E)$
- **Space Complexity**: $O(V)$
