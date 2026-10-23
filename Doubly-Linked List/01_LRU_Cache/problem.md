# 📖 LRU Cache (LeetCode #146)

- **Difficulty**: Medium
- **Asked By**: Google, Meta (#1 most asked system-DSA hybrid), Amazon, OpenAI
- **Frequency**: ⭐⭐⭐⭐⭐

## 💡 Real-Life Analogy
A smartphone screen showing the 3 most recently used apps.
When you open an app, it jumps to the front.
When you open a brand new app when the screen is full, the least recently used app is evicted!

## 📋 Problem Statement
Design a data structure that follows the constraints of a **Least Recently Used (LRU) cache**.
Implement the `LRUCache` class:
- `LRUCache(int capacity)`
- `get(int key)`: Return value if exists, else -1.
- `put(int key, int value)`: Update or insert. Evict LRU if capacity exceeded.
Both `get` and `put` must run in **$O(1)$ average time**.
