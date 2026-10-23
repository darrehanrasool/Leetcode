# 🌲 Topic: Segment Tree & Binary Indexed Tree (Fenwick Tree) (Python DSA from Scratch)

## 🌟 1. Real-Life Analogy
A dynamic spreadsheet where cells are constantly being updated, and users frequently ask for sum totals of row ranges:
- Normal array: Update is $O(1)$, but range sum is $O(N)$.
- Prefix array: Range sum is $O(1)$, but updating a single cell requires recalculating everything in $O(N)$.
- **Segment Tree / Fenwick Tree**: Both updates AND range sum queries take **$O(\log N)$ time**!

## 🤖 2. Why AI Engineers Care
- Real-time rolling metric calculation in live feature streams.
- Dynamic rank order statistic tracking.
