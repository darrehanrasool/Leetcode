# 💡 Merge Two Sorted Lists - Solution Deep Dive

## 🧠 Thought Process
Use a dummy head node.
Compare `list1.val` and `list2.val`:
- Attach smaller node to `curr.next`.
- Advance whichever list had the smaller node.
Attach remaining nodes at the end.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(M + N)$
- **Space Complexity**: $O(1)$ in-place pointer splicing.
