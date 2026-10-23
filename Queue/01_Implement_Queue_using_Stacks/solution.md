# 💡 Implement Queue using Stacks - Solution Deep Dive

## 🧠 Thought Process
Use two stacks:
- `in_stack`: handles incoming `push(x)`.
- `out_stack`: handles `pop()` and `peek()`.
When `out_stack` is empty, transfer all elements from `in_stack` to `out_stack`. This naturally reverses the order, turning LIFO into FIFO!

## ⏱️ Complexity Analysis
- **Amortized Time Complexity**: $O(1)$ per operation.
- **Space Complexity**: $O(N)$ to store elements.
