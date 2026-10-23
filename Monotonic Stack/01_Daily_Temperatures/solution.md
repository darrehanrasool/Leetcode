# 💡 Daily Temperatures - Solution Deep Dive

## 🧠 Thought Process
Maintain a stack of indices `stack` where temperatures are strictly decreasing.
For each day `curr_day, curr_temp`:
- While stack is non-empty and `curr_temp > temperatures[stack[-1]]`:
  - `prev_day = stack.pop()`
  - `answer[prev_day] = curr_day - prev_day`
- Push `curr_day` onto stack.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N)$ — Each index pushed and popped at most once.
- **Space Complexity**: $O(N)$ for stack.
