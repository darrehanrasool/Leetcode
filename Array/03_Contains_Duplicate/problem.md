# 🔍 Contains Duplicate (LeetCode #217)

- **Difficulty**: Easy
- **Asked By**: Meta (Facebook), Apple, Amazon, Adobe, Microsoft, AI Startups
- **Frequency**: ⭐⭐⭐⭐ (The classic Hash Set warm-up question)

---

## 💡 Real-Life Analogy

Imagine you are a security guard at an exclusive **VIP event**:
- Every guest gives you their passport/ID number as they enter.
- Your job: Ring the alarm immediately if **any person tries to sneak in twice** with the same ID number.

How would you do it?
1. **The Slow Way**: Every time a new guest arrives, you look back through your entire physical paper list from the beginning of the night to the end. As the guest count reaches thousands, this takes forever ($O(N^2)$).
2. **The Fast Way (Hash Set)**: You have a digital scanner. Whenever a passport number is scanned, it checks a digital set in **1 millisecond ($O(1)$)**. If the number is already in the database, alarm rings! Otherwise, store the number and let them pass.

---

## 📋 Problem Statement

Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is **distinct**.

### Examples

#### Example 1:
- **Input**: `nums = [1, 2, 3, 1]`
- **Output**: `true`
- **Explanation**: The element `1` occurs at indices `0` and `3`.

#### Example 2:
- **Input**: `nums = [1, 2, 3, 4]`
- **Output**: `false`
- **Explanation**: All elements are distinct.

#### Example 3:
- **Input**: `nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]`
- **Output**: `true`

---

## 🎨 Visual Diagram

```
nums = [ 1 , 2 , 3 , 1 ]

Guest 1: "1"  --> Check set: not seen yet  --> Add to set: { 1 }
Guest 2: "2"  --> Check set: not seen yet  --> Add to set: { 1, 2 }
Guest 3: "3"  --> Check set: not seen yet  --> Add to set: { 1, 2, 3 }
Guest 4: "1"  --> Check set: ALREADY IN SET! 🚨 DUPLICATE DETECTED!
                  Return True immediately.
```

---

## ⚠️ Constraints & Edge Cases

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

### Edge Cases to Consider:
1. **Single-element array**: `[1]` $\rightarrow$ Always `false` (cannot have a duplicate with 1 element).
2. **All identical elements**: `[7, 7, 7, 7]` $\rightarrow$ Returns `true` on the 2nd element.
3. **Negative numbers**: `[-1, -2, -3, -1]` $\rightarrow$ Handled correctly because hash functions support negative integers.
4. **Duplicate is at the very ends**: `[1, 2, 3, ..., 1]` $\rightarrow$ Worst case for space, but still $O(N)$ time.

---

## 🙋 Clarifying Questions to Ask in an Interview

1. *"Should I optimize for time or space?"* (A Hash Set is $O(N)$ time and $O(N)$ space. Sorting is $O(N \log N)$ time and $O(1)$ space. Clarifying which the interviewer prefers demonstrates senior engineering maturity!).
2. *"Can the array fit entirely into RAM?"* (If the dataset has billions of elements, we might need an external merge sort or a Bloom filter!).
