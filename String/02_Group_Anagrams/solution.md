# 💡 Group Anagrams - Solution Deep Dive

## 🧠 Thought Process
- Initialize `buckets = collections.defaultdict(list)`
- For each word:
  - Canonical Key: `tuple(sorted(word))` or character count tuple of length 26.
  - Append word to `buckets[key]`.
- Return `list(buckets.values())`.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N \cdot K \log K)$ where $N$ is number of strings, $K$ is max length of string.
- **Space Complexity**: $O(N \cdot K)$ to store grouped words.
