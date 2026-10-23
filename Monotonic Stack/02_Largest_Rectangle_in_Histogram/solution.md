# 💡 Largest Rectangle in Histogram - Solution Deep Dive

## 🧠 Thought Process
Monotonic increasing stack of `(index, height)`:
When we see a bar shorter than the top of stack, the taller bar cannot extend any further to the right!
We pop the taller bar, calculate its maximum area rectangle, and record that the new shorter bar could actually extend backwards to where the popped bar started.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N)$
- **Space Complexity**: $O(N)$
