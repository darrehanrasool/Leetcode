# 📖 Daily Temperatures (LeetCode #739)

- **Difficulty**: Medium
- **Asked By**: Meta, Google, Amazon
- **Frequency**: ⭐⭐⭐⭐⭐

## 💡 Real-Life Analogy
Looking at the weather forecast: for each day, how many days must you wait until a warmer day arrives?
`temperatures = [73, 74, 75, 71, 69, 72, 76, 73]`
Using a monotonic decreasing stack, colder days wait on the stack until a warmer day arrives and resolves all of them at once!

## 📋 Problem Statement
Given an array of integers `temperatures` represents the daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the `i`-th day to get a warmer temperature. If there is no future day for which this is possible, keep `answer[i] == 0` instead.
