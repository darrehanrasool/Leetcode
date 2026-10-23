# 💡 Evaluate Reverse Polish Notation - Solution Deep Dive

## 🧠 Thought Process
Iterate through tokens:
- If operator (`+`, `-`, `*`, `/`):
  - Pop operand 2 (`b`), then operand 1 (`a`).
  - Compute result (note: integer division in Python truncates toward zero: `int(a / b)`).
  - Push result to stack.
- Else: push integer to stack.
Return final element of stack.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N)$
- **Space Complexity**: $O(N)$
