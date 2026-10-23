# 💡 Design Add and Search Words - Solution Deep Dive

## 🧠 Thought Process
Trie with DFS backtracking for wildcard `.` matching:
If character is `.` (dot), we branch recursively into all available children at that node.
