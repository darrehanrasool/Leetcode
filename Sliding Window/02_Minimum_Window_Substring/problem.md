# 📖 Minimum Window Substring (LeetCode #76)

- **Difficulty**: Hard
- **Asked By**: Meta (Top Hard question), Google, Amazon, Airbnb
- **Frequency**: ⭐⭐⭐⭐⭐

## 💡 Real-Life Analogy
Imagine searching through a long text message (`s = "ADOBECODEBANC"`) to find the shortest snippet that contains all the letters needed for an anagram recipe (`t = "ABC"`).
- You expand your window to the right until all ingredients A, B, and C are present.
- Once you have all ingredients, you shrink the window from the left to discard unnecessary fluff, recording the minimum valid window size!

## 📋 Problem Statement
Given two strings `s` and `t` of lengths `m` and `n` respectively, return the **minimum window substring** of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such substring, return the empty string `""`.

### Examples
- **Input**: `s = "ADOBECODEBANC"`, `t = "ABC"`
- **Output**: `"BANC"`
