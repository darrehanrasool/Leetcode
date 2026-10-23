# 💡 Gas Station - Solution Deep Dive

## 🧠 Thought Process
If total gas < total cost, complete circuit is impossible (return -1).
Otherwise, a unique starting index is guaranteed!
Maintain running tank: if running tank < 0, reset tank to 0 and set starting station to `i + 1`.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N)$
- **Space Complexity**: $O(1)$
