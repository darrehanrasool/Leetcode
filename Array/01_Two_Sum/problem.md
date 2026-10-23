# 🎯 Two Sum (LeetCode #1)

- **Difficulty**: Easy
- **Asked By**: Google, Meta (Facebook), OpenAI, Amazon, Apple, Microsoft, Uber, Bloomberg
- **Frequency**: ⭐⭐⭐⭐⭐ (The single most asked coding interview question in tech history)

---

## 💡 Real-Life Analogy

Imagine you are standing at a **coffee shop checkout** counter:
- Your order costs **\$9** (`target = 9`).
- You reach into your wallet and pull out a handful of gift cards with values: **\$2, \$7, \$11, \$15** (`nums = [2, 7, 11, 15]`).
- The cashier tells you: *"You must pay using **exactly two** gift cards that add up to \$9."*

How would you find them?
1. **The Slow Way (Brute Force)**: You pick up the \$2 card and test it with \$7, then \$11, then \$15. Then you pick up \$7 and test with the rest.
2. **The Smart Way (Hash Map / Memory)**:
   - When you look at the **\$2** card, you immediately know: *"I need a **\$7** card to make \$9 ($9 - 2 = 7$). Let me write down in my notebook that I have a \$2 card at pocket spot 0."*
   - Next, you look at the **\$7** card. You calculate: *"I need a **\$2** card ($9 - 7 = 2$). Have I seen a \$2 card before?"*
   - You check your notebook: **YES!** It was at spot 0.
   - **BAM!** You give cards at spot 0 and spot 1 to the cashier. Done in a single look!

---

## 📋 Problem Statement

Given an array of integers `nums` and an integer `target`, return the **indices** of the two numbers such that they add up to `target`.

- You may assume that each input would have **exactly one solution**.
- You may **not** use the same element twice.
- You can return the answer in any order.

### Examples

#### Example 1:
- **Input**: `nums = [2, 7, 11, 15]`, `target = 9`
- **Output**: `[0, 1]`
- **Explanation**: Because `nums[0] + nums[1] == 2 + 7 == 9`, we return `[0, 1]`.

#### Example 2:
- **Input**: `nums = [3, 2, 4]`, `target = 6`
- **Output**: `[1, 2]`
- **Explanation**: `nums[1] + nums[2] == 2 + 4 == 6`.

#### Example 3:
- **Input**: `nums = [3, 3]`, `target = 6`
- **Output**: `[0, 1]`

---

## 🎨 Visual Diagram

```
Target = 9

Index:       0       1       2       3
Array:    [  2  ,    7  ,   11  ,   15  ]
             ▲       ▲
             |_______|
                 |
             2 + 7 = 9  ──> Return [0, 1]
```

---

## ⚠️ Constraints & Edge Cases

- `2 <= nums.length <= 10^4` (Array always has at least 2 numbers)
- `-10^9 <= nums[i] <= 10^9` (Numbers can be negative, zero, or huge)
- `-10^9 <= target <= 10^9`
- Only one valid answer exists.

### Edge Cases to Discuss with Your Interviewer:
1. **Negative numbers**: E.g., `nums = [-3, 4, 3, 90]`, `target = 0` $\rightarrow$ pair is `[-3, 3]`, returns `[0, 2]`.
2. **Duplicate values**: E.g., `nums = [3, 3]`, `target = 6` $\rightarrow$ both are index `0` and `1`.
3. **Large numbers**: Python handles arbitrarily large integers, but in languages like C++/Java you would discuss potential 32-bit integer overflow.

---

## 🙋 Clarifying Questions to Ask in an Interview

1. *"Can there be multiple pairs that sum to the target, or is a unique solution guaranteed?"* (LeetCode guarantees exactly one).
2. *"Can the array contain negative numbers or zeros?"* (Yes).
3. *"Can I use the exact same element twice (e.g. `nums[0] + nums[0]`)?"* (No, must be two distinct indices).
4. *"Can I modify the original array (e.g., sort it)?"* (Sorting changes original indices, so if you sort, you must keep track of original indices!).
