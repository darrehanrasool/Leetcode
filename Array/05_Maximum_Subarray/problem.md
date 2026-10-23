# 🚀 Maximum Subarray (LeetCode #53)

- **Difficulty**: Medium
- **Asked By**: Google, Meta (Facebook), ByteDance (TikTok), Amazon, Microsoft, LinkedIn
- **Frequency**: ⭐⭐⭐⭐⭐ (The quintessential continuous subarray problem — introduces Kadane's Algorithm)

---

## 💡 Real-Life Analogy

Imagine you are running a startup business, tracking your **daily net profit / loss** over several days:
`[-2, 1, -3, 4, -1, 2, 1, -5, 4]`
- Some days you make profit (positive numbers like `+4`, `+2`), and some days you burn cash (negative numbers like `-2`, `-3`).
- You want to present to your investors the **single best uninterrupted winning streak** in company history. That is: a contiguous sequence of days that yields the highest cumulative profit.

### The Golden Rule of Streaks (Kadane's Intuition):
If your past business streak has accumulated a **net negative debt** (e.g. running total is `< 0`), should you carry that baggage forward into today?
**NO!** A negative past will only drag down today's profit.
Whenever your running balance drops below `0`, you declare bankruptcy on the past streak and **start a brand new streak starting today**!

---

## 📋 Problem Statement

Given an integer array `nums`, find the **subarray** with the largest sum, and return its **sum**.

A **subarray** is a **contiguous** (unbroken) non-empty sequence of elements within an array.

### Examples

#### Example 1:
- **Input**: `nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]`
- **Output**: `6`
- **Explanation**: The subarray `[4, -1, 2, 1]` has the largest sum = `4 + (-1) + 2 + 1 = 6`.

#### Example 2:
- **Input**: `nums = [1]`
- **Output**: `1`
- **Explanation**: The subarray `[1]` has the largest sum = `1`.

#### Example 3:
- **Input**: `nums = [5, 4, -1, 7, 8]`
- **Output**: `23`
- **Explanation**: The subarray `[5, 4, -1, 7, 8]` has the largest sum = `23` (the entire array).

---

## 🎨 Visual Diagram

```
Index:    0    1    2    3    4    5    6    7    8
nums:  [ -2 ,  1 , -3 ,  4 , -1 ,  2 ,  1 , -5 ,  4 ]
                         ▲                   ▲
                         |___________________|
                                   |
                  Subarray: [4, -1, 2, 1]
                  Sum: 4 + (-1) + 2 + 1 = 6 (Max!)
```

---

## ⚠️ Constraints & Edge Cases

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

### Key Edge Cases to Watch:
1. **All negative numbers**: E.g., `nums = [-5, -2, -8, -1]`
   - If all numbers are negative, you cannot return `0` because a subarray must be **non-empty**!
   - The correct answer is the least negative number: `-1`.
2. **Single element array**: `nums = [-3]` $\rightarrow$ returns `-3`.
3. **All positive numbers**: E.g., `[1, 2, 3]` $\rightarrow$ returns sum of all elements (`6`).

---

## 🙋 Clarifying Questions to Ask in an Interview

1. *"Can the subarray be empty, or must it contain at least one element?"* (LeetCode specifies non-empty, which means if all elements are negative, the answer is the largest negative number, not 0!).
2. *"Do you want the maximum sum itself, or the starting and ending indices of the subarray?"* (Usually just the sum, but knowing how to track indices impresses interviewers!).
