# 📅 Merge Intervals (LeetCode #56)

- **Difficulty**: Medium
- **Asked By**: Meta (Facebook - #1 Most Asked Question), Google, Amazon, Microsoft, Uber, Bloomberg
- **Frequency**: ⭐⭐⭐⭐⭐ (The undisputed king of Interval problems)

---

## 💡 Real-Life Analogy

Imagine you are managing an executive **conference room calendar**:
- Team A books the room from **1:00 PM to 3:00 PM** (`[1, 3]`).
- Team B books the room from **2:00 PM to 6:00 PM** (`[2, 6]`).
- Team C books the room from **8:00 PM to 10:00 PM** (`[8, 10]`).
- Team D books the room from **15:00 to 18:00 (3:00 PM to 6:00 PM)** (`[15, 18]`).

Look at Team A and Team B:
Team A starts at 1 and ends at 3. But Team B arrives at 2, before Team A even left!
They overlap! The room is occupied continuously from **1:00 PM to 6:00 PM** (`[1, 6]`).
On the other hand, the meeting from 8 to 10 has a gap, so it stays separate.

How do you automate this calendar merge?
**The Secret**: Sort all meetings by their **start time** first! Once meetings are chronologically sorted, you only ever need to compare each new meeting with the **very last merged meeting**.

---

## 📋 Problem Statement

Given an array of `intervals` where `intervals[i] = [start_i, end_i]`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

### Examples

#### Example 1:
- **Input**: `intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]`
- **Output**: `[[1, 6], [8, 10], [15, 18]]`
- **Explanation**: Since intervals `[1, 3]` and `[2, 6]` overlap, merge them into `[1, 6]`.

#### Example 2:
- **Input**: `intervals = [[1, 4], [4, 5]]`
- **Output**: `[[1, 5]]`
- **Explanation**: Intervals `[1, 4]` and `[4, 5]` are considered overlapping because they touch at `4`.

---

## 🎨 Visual Diagram

```
Timeline:   1   2   3   4   5   6   7   8   9   10  ... 15  16  17  18
[1, 3]:     [=======]
[2, 6]:         [==============]
Merged:     [==================]            (Interval [1, 6])

[8, 10]:                                [=======]   (Interval [8, 10])

[15, 18]:                                               [===========]

Final Merged Result: [[1, 6], [8, 10], [15, 18]]
```

---

## ⚠️ Constraints & Edge Cases

- `1 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= start_i <= end_i <= 10^4`

### Key Edge Cases to Watch:
1. **Touching at a single point**: E.g., `[1, 4]` and `[4, 5]` $\rightarrow$ Merges into `[1, 5]`! (Boundary touch counts as overlap).
2. **One interval completely swallows another**: E.g., `[1, 10]` and `[2, 5]` $\rightarrow$ Merges into `[1, 10]`.
3. **Unsorted input**: E.g., `[[1, 4], [0, 2]]` $\rightarrow$ MUST sort first to become `[[0, 2], [1, 4]]` $\rightarrow$ Merges to `[[0, 4]]`.
4. **Single interval**: `[[1, 5]]` $\rightarrow$ Return `[[1, 5]]`.

---

## 🙋 Clarifying Questions to Ask in an Interview

1. *"Are the intervals guaranteed to be sorted by start time upfront?"* (Never assume this! Always sort first or ask).
2. *"If two intervals touch at the exact boundary (e.g. `[1, 4]` and `[4, 5]`), do they count as overlapping?"* (Yes, per problem definition).
3. *"Can intervals have negative start/end times?"* (Standard is non-negative, but sorting handles negative numbers identically).
