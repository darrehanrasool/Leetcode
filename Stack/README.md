# 🥞 Topic: Stack (Python DSA from Scratch)

## 🌟 1. Real-Life Analogy: What is a Stack?
Think of a **stack of plates in a cafeteria** or the **Undo (Ctrl+Z) button** in a text editor:
- **LIFO (Last-In, First-Out)**: The plate placed on top last is the first plate taken off.
- `push(x)`: Place plate on top ($O(1)$).
- `pop()`: Remove plate from top ($O(1)$).
- `peek()` / `top()`: Look at the top plate without removing it ($O(1)$).

## 🤖 2. Why AI Engineers Care
- **Call Stacks & Backpropagation**: Deep learning frameworks (PyTorch Autograd) use a reverse execution tape (a stack of operations) to compute gradients in reverse mode automatic differentiation!
- **Parsing Syntax & Prompts**: Evaluating mathematical expressions, AST parsing, and validating JSON / tool-calling schemas.

## 📚 Problems in this Directory
1. `01_Valid_Parentheses` (Easy - Google, Meta, Apple)
2. `02_Min_Stack` (Medium - Amazon, Bloomberg, Meta)
3. `03_Evaluate_Reverse_Polish_Notation` (Medium - Google, LinkedIn)
