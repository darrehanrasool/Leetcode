# 📖 Subarray Sum Equals K (LeetCode #560)

- **Difficulty**: Medium
- **Asked By**: Meta (Top 3 most asked across all tech), Google, Amazon
- **Frequency**: ⭐⭐⭐⭐⭐

## 💡 Real-Life Analogy
You are looking for stretches of transactions that total \$K.
Using running balance: if your current balance is \$100, and $K = \$30$, have you ever previously had a balance of $\$100 - \$30 = \$70$?
Every time you had \$70 in the past represents a subarray summing to \$30!

## 📋 Problem Statement
Given an array of integers `nums` and an integer `k`, return the **total number of subarrays** whose sum equals to `k`.

### Examples
- **Input**: `nums = [1, 1, 1]`, `k = 2` -> `Output: 2`
- **Input**: `nums = [1, 2, 3]`, `k = 3` -> `Output: 2`
