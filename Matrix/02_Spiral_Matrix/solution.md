# 💡 Spiral Matrix - Solution Deep Dive

## 🧠 Thought Process (4 Boundary Pointers)
Maintain `top`, `bottom`, `left`, `right`.
Traverse:
1. Top row: `left` to `right`, then `top += 1`.
2. Right col: `top` to `bottom`, then `right -= 1`.
3. Bottom row: `right` to `left`, then `bottom -= 1`.
4. Left col: `bottom` to `top`, then `left += 1`.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(M \times N)$
- **Space Complexity**: $O(1)$ auxiliary space.
