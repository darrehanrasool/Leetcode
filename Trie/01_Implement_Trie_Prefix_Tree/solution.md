# 💡 Implement Trie - Solution Deep Dive

## 🧠 Thought Process
Each `TrieNode` has:
- `children`: dictionary mapping character to child `TrieNode`.
- `is_end_of_word`: boolean flag indicating if a word ends here.

## ⏱️ Complexity Analysis
- `insert`, `search`, `startsWith`: $O(L)$ time where $L$ is length of word.
- **Space Complexity**: $O(N \cdot L)$ where $N$ is number of inserted words.
