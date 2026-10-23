# 💡 LRU Cache - Solution Deep Dive

## 🧠 Architecture
- **Hash Map**: Maps `key -> Node` for $O(1)$ lookups.
- **Doubly-Linked List**: Maintains access order with dummy `head` (Least Recently Used) and dummy `tail` (Most Recently Used).
- Moving a node to MRU or removing LRU node is $O(1)$ pointer manipulation.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(1)$ for both `get` and `put`.
- **Space Complexity**: $O(\text{capacity})$.
