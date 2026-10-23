# 💡 Word Search - Solution Deep Dive

## 🧠 Thought Process (Grid DFS with In-Place Visited Marking)
For each matching start letter:
- Temporarily mark cell as visited: `board[r][c] = "#"`.
- Recursively explore 4 directions for `word[idx + 1]`.
- Restore cell: `board[r][c] = char`.
