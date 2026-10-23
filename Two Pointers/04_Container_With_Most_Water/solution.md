# 💡 Container With Most Water - Solution Deep Dive

## 🧠 Thought Process & Invariant
Start with maximum width: `left = 0`, `right = len(height) - 1`.
At each step:
$$\text{Current Area} = \min(\text{height}[left], \text{height}[right]) \times (right - left)$$
Which pointer should we move?
- The width will decrease by 1 regardless of which pointer moves.
- Moving the taller post will NEVER increase the area because the height is bottle-necked by the shorter post.
- Therefore, the ONLY move that could potentially yield a larger area is moving the **shorter pointer inward**!

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N)$ — Single pass inward.
- **Space Complexity**: $O(1)$ — Only tracking max area and two pointers.
