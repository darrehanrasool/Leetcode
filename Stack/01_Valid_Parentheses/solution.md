# 💡 Valid Parentheses - Solution Deep Dive

## 🧠 Thought Process
Use a stack and a dictionary mapping closing brackets to their matching opening brackets:
`matching = {')': '(', '}': '{', ']': '['}`
- For each character `char` in `s`:
  - If `char in matching` (it's a closing bracket):
    - Pop the top of the stack (if empty, assign a dummy mismatch).
    - If popped element doesn't match `matching[char]`, return `False`.
  - Else (it's an opening bracket):
    - Push onto stack.
- After loop, return `True` only if stack is empty!

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N)$
- **Space Complexity**: $O(N)$
