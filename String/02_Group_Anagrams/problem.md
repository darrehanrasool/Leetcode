# 📖 Group Anagrams (LeetCode #49)

- **Difficulty**: Medium
- **Asked By**: Meta, Google, Amazon, Apple
- **Frequency**: ⭐⭐⭐⭐⭐

## 💡 Real-Life Analogy
Sorting words into buckets by their "letter recipe":
Words `"eat"`, `"tea"`, `"ate"` all have 1 'a', 1 'e', 1 't'.
If we sort their letters alphabetically, they all equal `"aet"`. We can use `"aet"` as the dictionary key and store all matching words in that bucket!

## 📋 Problem Statement
Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

### Examples
- **Input**: `strs = ["eat","tea","tan","ate","nat","bat"]`
- **Output**: `[["bat"],["nat","tan"],["ate","eat","tea"]]`
