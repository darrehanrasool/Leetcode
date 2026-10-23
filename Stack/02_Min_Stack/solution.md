# 💡 Min Stack - Solution Deep Dive

## 🧠 Thought Process
Maintain two parallel stacks:
1. `stack`: normal values.
2. `min_stack`: keeps track of the current minimum up to that depth.
When pushing `x`, push `min(x, min_stack[-1])` to `min_stack`.
When popping, pop from both stacks.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(1)$ for all operations (`push`, `pop`, `top`, `getMin`).
- **Space Complexity**: $O(N)$ for the auxiliary min stack.
