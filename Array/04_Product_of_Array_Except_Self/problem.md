# ✖️ Product of Array Except Self (LeetCode #238)

- **Difficulty**: Medium
- **Asked By**: Meta (Facebook - Top 3 asked), Google, Amazon, Microsoft, Apple, OpenAI
- **Frequency**: ⭐⭐⭐⭐⭐ (Iconic problem testing prefix & suffix array manipulation without division)

---

## 💡 Real-Life Analogy

Imagine you are managing an ensemble team of **4 AI models** working together to rate a document:
- Each model has an accuracy score: `[1, 2, 3, 4]`.
- For each model, you want to calculate the collective power of **every other model except itself**:
  - For model 0 (score 1): Product of everyone else = $2 \times 3 \times 4 = 24$
  - For model 1 (score 2): Product of everyone else = $1 \times 3 \times 4 = 12$
  - For model 2 (score 3): Product of everyone else = $1 \times 2 \times 4 = 8$
  - For model 3 (score 4): Product of everyone else = $1 \times 2 \times 3 = 6$

**The Catch**:
Normally you'd say: *"Just multiply all numbers together ($1 \times 2 \times 3 \times 4 = 24$) and divide by the current number ($24 / 2 = 12$)."*
**BUT the interviewer bans the division operator (`/`)!**
Also, what if one or two scores are `0`? Division by zero causes a computer crash (`ZeroDivisionError`)!

How do you calculate this without ever using division?
**Split the world into two halves**:
1. Everything to the **LEFT** of the item (Prefix product)
2. Everything to the **RIGHT** of the item (Suffix product)
The answer for any spot is simply: `Left_Product * Right_Product`!

---

## 📋 Problem Statement

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

You must write an algorithm that runs in **$O(N)$** time and **without using the division operation**.

### Follow up:
Can you solve the problem in **$O(1)$ extra space complexity**? (The output array does not count as extra space for space complexity analysis).

### Examples

#### Example 1:
- **Input**: `nums = [1, 2, 3, 4]`
- **Output**: `[24, 12, 8, 6]`

#### Example 2:
- **Input**: `nums = [-1, 1, 0, -3, 3]`
- **Output**: `[0, 0, 9, 0, 0]`

---

## 🎨 Visual Diagram

```
Array:                 [   1   ,   2   ,   3   ,   4   ]
                                   ▲
                                   | (We want product except 3 at index 2)

Left of index 2:       [   1   ,   2   ]        ---> Product = 1 * 2 = 2
Right of index 2:                          [   4   ] ---> Product = 4

Total for index 2:     (Left Product) * (Right Product)
                       = 2 * 4 = 8
```

---

## ⚠️ Constraints & Edge Cases

- `2 <= nums.length <= 10^5`
- `-30 <= nums[i] <= 30`
- The product of any prefix or suffix is guaranteed to fit in a 32-bit integer.

### Crucial Edge Cases:
1. **Contains a single zero**: E.g., `[1, 2, 0, 4]` $\rightarrow$ The output at the zero index will be non-zero ($1 \times 2 \times 4 = 8$), and every other index will be `0`!
2. **Contains multiple zeros**: E.g., `[0, 2, 0, 4]` $\rightarrow$ Every single element in the output must be `0`.
3. **Negative numbers**: Watch for signs flipping (e.g. `[-1, -1, -1]`).

---

## 🙋 Clarifying Questions to Ask in an Interview

1. *"Am I allowed to use the division operator `/`?"* (The problem explicitly forbids it, but confirming this shows you read the requirements carefully).
2. *"Can the array contain zeros?"* (Yes, 0 is possible and common).
3. *"Does the return array count against the auxiliary space complexity?"* (Standard interview convention: output memory is not counted as extra auxiliary space).
