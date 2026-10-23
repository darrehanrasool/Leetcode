# 💡 Reverse Linked List - Solution Deep Dive

## 🧠 Thought Process
Use three pointers: `prev`, `curr`, `nxt`:
- `prev = None`
- `curr = head`
While `curr`:
- Save `nxt = curr.next`
- Reverse pointer: `curr.next = prev`
- Advance: `prev = curr`, `curr = nxt`
Return `prev` (new head).

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N)$
- **Space Complexity**: $O(1)$ in-place.
