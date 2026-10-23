# 📖 Container With Most Water (LeetCode #11)

- **Difficulty**: Medium
- **Asked By**: Google, Meta, Amazon, Adobe
- **Frequency**: ⭐⭐⭐⭐⭐

## 💡 Real-Life Analogy
Imagine two vertical wooden posts holding water between them:
The water level is limited by the **shorter post** (water spills over the lower edge).
$$\text{Area} = \min(\text{height}_1, \text{height}_2) \times \text{distance}$$
To find the biggest tank, start with posts at maximum distance (left=0, right=N-1).
To have any chance of finding a bigger container, you MUST replace the shorter post with a taller one!

## 📋 Problem Statement
Given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i`-th line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the **maximum amount of water** a container can store.

### Examples
- **Input**: `height = [1, 8, 6, 2, 5, 4, 8, 3, 7]`
- **Output**: `49`
- **Explanation**: Lines at index 1 (height 8) and index 8 (height 7) hold `min(8, 7) * (8 - 1) = 7 * 7 = 49`.
