# 📈 Best Time to Buy and Sell Stock (LeetCode #121)

- **Difficulty**: Easy
- **Asked By**: Google, Meta (Facebook), Amazon, Microsoft, Apple, Bloomberg, Citadel
- **Frequency**: ⭐⭐⭐⭐⭐ (Top 5 most frequently asked across FAANG/Big Tech)

---

## 💡 Real-Life Analogy

Imagine you have a **time machine**, but it only works in **chronological order** (forward in time):
- You have a table showing the price of Bitcoin or Apple stock on each day:
  `prices = [7, 1, 5, 3, 6, 4]`
- You are allowed to buy on **one single day** in the past and sell on a **different future day**.
- What is the maximum cash profit you could take home?

```
Day:       0       1       2       3       4       5
Price:    $7      $1      $5      $3      $6      $4
                   ▲                       ▲
                   |                       |
              Buy Here ($1)           Sell Here ($6)
                   Profit = $6 - $1 = $5 💰
```

Notice: You cannot sell before you buy! (e.g., you cannot buy at \$1 on day 1 and pretend you sold at \$7 on day 0).

---

## 📋 Problem Statement

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`-th day.

You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

Return the **maximum profit** you can achieve from this transaction. If you cannot achieve any profit, return `0`.

### Examples

#### Example 1:
- **Input**: `prices = [7, 1, 5, 3, 6, 4]`
- **Output**: `5`
- **Explanation**: Buy on day 1 (price = 1) and sell on day 4 (price = 6), profit = `6 - 1 = 5`.
  Note that buying on day 1 and selling on day 0 is not allowed because you must buy before you sell.

#### Example 2:
- **Input**: `prices = [7, 6, 4, 3, 1]`
- **Output**: `0`
- **Explanation**: In this case, the price keeps dropping every single day. No profitable transaction is possible, so maximum profit = `0`.

---

## 🎨 Visual Diagram

```
Price ($)
  8 |
  7 |   ● (Day 0: $7)
  6 |                               ● (Day 4: $6)  <--- SELL
  5 |                   ● (Day 2: $5)
  4 |                                           ● (Day 5: $4)
  3 |                           ● (Day 3: $3)
  2 |
  1 |           ● (Day 1: $1) <--- BUY
  0 +-------------------------------------------------------> Day
        0       1       2       3       4       5

  Maximum Profit Span: $6 - $1 = $5
```

---

## ⚠️ Constraints & Edge Cases

- `1 <= prices.length <= 10^5`
- `0 <= prices[i] <= 10^4`

### Key Edge Cases to Consider:
1. **Strictly decreasing prices**: e.g., `[5, 4, 3, 2, 1]` $\rightarrow$ should return `0`, never negative!
2. **Single element array**: e.g., `[5]` $\rightarrow$ cannot buy and sell on distinct days, should return `0`.
3. **Flat prices**: e.g., `[2, 2, 2, 2]` $\rightarrow$ profit is `0`.
4. **Lowest price is the very last day**: e.g., `[3, 8, 1]` $\rightarrow$ best is buy at `3` and sell at `8` (profit `5`), even though `1` is the absolute minimum, because no days exist after `1` to sell!

---

## 🙋 Clarifying Questions to Ask in an Interview

1. *"Can I buy and sell on the same day?"* (No, must be a future day; even if allowed, profit would be 0).
2. *"Can I complete multiple transactions (buy and sell multiple times)?"* (No, this is LeetCode 121 which specifies **one single transaction**. Multiple transactions is LeetCode 122).
3. *"If prices only decrease, should I return a negative loss or 0?"* (Return 0).
