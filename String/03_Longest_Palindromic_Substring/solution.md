# 💡 Longest Palindromic Substring - Solution Deep Dive

## 🧠 Thought Process
Every palindrome has a center:
1. **Odd length** (e.g. `"racecar"`): center is `'e'`.
2. **Even length** (e.g. `"noon"`): center is between the two `'o'`s.
For each index `i`, expand outward to find longest odd and even palindromes!

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N^2)$ — $2N$ centers, each expands at most $O(N)$.
- **Space Complexity**: $O(1)$ auxiliary space.
