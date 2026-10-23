# 💡 Number of 1 Bits - Solution Deep Dive

## 🧠 Brian Kernighan's Algorithm
The operation `n & (n - 1)` always clears the lowest set bit in `n`!
We simply repeat `n &= (n - 1)` until `n == 0`.
Loop runs exactly as many times as there are `1` bits.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(1)$ (at most 32 operations).
- **Space Complexity**: $O(1)$.
