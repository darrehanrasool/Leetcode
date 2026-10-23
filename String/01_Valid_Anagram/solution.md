# 💡 Valid Anagram - Solution Deep Dive

## 🧠 Thought Process
1. If `len(s) != len(t)`, they cannot be anagrams $\rightarrow$ return `False`.
2. Count letter occurrences using a hash map or array of size 26 (for lowercase English).
3. If counts match, return `True`.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N)$ where $N = len(s)$.
- **Space Complexity**: $O(1)$ because the alphabet size is bounded by 26 characters.
