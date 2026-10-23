# 📖 Valid Palindrome (LeetCode #125)

- **Difficulty**: Easy
- **Asked By**: Meta (Facebook - High Frequency), Google, Microsoft, Amazon, Apple
- **Frequency**: ⭐⭐⭐⭐⭐

## 💡 Real-Life Analogy
A palindrome is a phrase that reads the same forwards and backwards, ignoring spaces and punctuation.
Like the word **"RACECAR"** or the famous phrase:
> *"A man, a plan, a canal: Panama!"*

If you place your left finger at the first letter **'A'** and your right finger at the last letter **'a'**, and move both inward skipping spaces and colons, your fingers will always point to identical letters!

## 📋 Problem Statement
A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

### Examples
- **Input**: `s = "A man, a plan, a canal: Panama"`
- **Output**: `true`
- **Explanation**: "amanaplanacanalpanama" is a palindrome.

- **Input**: `s = "race a car"`
- **Output**: `false`
- **Explanation**: "raceacar" is not a palindrome.

## 🎨 Visual Diagram
```
"A   m a n ,   a   p l a n ,   a   c a n a l :   P a n a m a"
 L ────────────────────────────────────────────────────────> R
 L='a', R='a' -> Match! Both move inward.
```

## ⚠️ Constraints & Edge Cases
- `1 <= s.length <= 2 * 10^5`
- `s` consists only of printable ASCII characters.
- **Empty string or string with only symbols** (e.g. `", . :"`): After cleaning, it is empty `""`, which is considered a valid palindrome (`true`).
