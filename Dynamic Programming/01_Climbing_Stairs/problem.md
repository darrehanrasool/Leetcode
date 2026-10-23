# 📖 Climbing Stairs (LeetCode #70)

- **Difficulty**: Easy
- **Asked By**: Google, Apple, Amazon
- **Frequency**: ⭐⭐⭐⭐⭐

## 💡 Real-Life Analogy
You can climb 1 or 2 steps at a time.
To reach step `n`, you either took a 1-step jump from step `n-1` OR a 2-step jump from step `n-2`.
Therefore: `ways(n) = ways(n-1) + ways(n-2)`. Fibonacci sequence!
