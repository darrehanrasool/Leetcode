# 📖 Valid Parentheses (LeetCode #20)

- **Difficulty**: Easy
- **Asked By**: Meta (Facebook - Top 5), Google, Amazon, Microsoft
- **Frequency**: ⭐⭐⭐⭐⭐

## 💡 Real-Life Analogy
Nesting Russian dolls or opening and closing quotation marks in English:
Every time you open an outer bracket `(`, you must close it with matching `)`.
If you open an inner bracket `[`, you must close the inner bracket `]` *before* you can close the outer `)`.
The last bracket opened must be the first bracket closed!

## 📋 Problem Statement
Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

### Examples
- **Input**: `s = "()[]{}"` -> `true`
- **Input**: `s = "(]"` -> `false`
- **Input**: `s = "([{}])"` -> `true`
