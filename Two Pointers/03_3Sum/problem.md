# 📖 3Sum (LeetCode #15)

- **Difficulty**: Medium
- **Asked By**: Meta (Top 3 most asked), Google, Amazon, Microsoft, Apple
- **Frequency**: ⭐⭐⭐⭐⭐

## 💡 Real-Life Analogy
You are organizing a 3-person committee where their skill budget must balance out to 0:
$a + b + c = 0$.
To avoid duplicate committees, you first line up all candidates by rank (sort them).
You fix candidate $a$, then use Two Pointers to find complementary pairs $b$ and $c$ such that $b + c = -a$.

## 📋 Problem Statement
Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must **not contain duplicate triplets**.

### Examples
- **Input**: `nums = [-1, 0, 1, 2, -1, -4]`
- **Output**: `[[-1, -1, 2], [-1, 0, 1]]`
