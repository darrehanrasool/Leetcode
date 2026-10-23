# 💡 Ransom Note - Solution Deep Dive

## 🧠 Thought Process
Count letters in `magazine` with a hash map.
For each char in `ransomNote`:
- If count in magazine is 0, return `False`.
- Otherwise decrement count.
Return `True` if all letters satisfied.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(M + N)$
- **Space Complexity**: $O(1)$ (at most 26 lowercase English letters).
