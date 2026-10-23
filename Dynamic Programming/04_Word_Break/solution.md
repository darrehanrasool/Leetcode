# 💡 Word Break - Solution Deep Dive

## 🧠 Thought Process
`dp[i]` is True if `s[0...i]` can be segmented using dictionary words.
`dp[0] = True` (empty string).
For `i` from 1 to `len(s)`:
- For `j` from 0 to `i`:
  - If `dp[j] and s[j:i] in word_set`: `dp[i] = True; break`.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N^2 \times L)$
- **Space Complexity**: $O(N)$
