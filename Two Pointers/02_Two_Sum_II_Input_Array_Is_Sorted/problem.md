# 📖 Two Sum II - Input Array Is Sorted (LeetCode #167)

- **Difficulty**: Medium
- **Asked By**: Amazon, Meta, Google, Apple
- **Frequency**: ⭐⭐⭐⭐⭐

## 💡 Real-Life Analogy
Imagine numbers on a sorted ruler:
`numbers = [2, 7, 11, 15]`, `target = 9`.
- Left finger at minimum number `2`.
- Right finger at maximum number `15`.
- Current sum = `2 + 15 = 17`. Too big! How do we make the sum smaller? Move the right finger to a smaller number.
- Next sum = `2 + 11 = 13`. Still too big! Move right finger left again.
- Next sum = `2 + 7 = 9`. Perfect match!

## 📋 Problem Statement
Given a **1-indexed** array of integers `numbers` that is already **sorted in non-decreasing order**, find two numbers such that they add up to a specific `target` number.

Return the indices of the two numbers, `index1` and `index2`, added by one as an integer array `[index1, index2]` of length 2.

**Constraint**: You must use only **$O(1)$ extra space**.

### Examples
- **Input**: `numbers = [2, 7, 11, 15]`, `target = 9`
- **Output**: `[1, 2]`
