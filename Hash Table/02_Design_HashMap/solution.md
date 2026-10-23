# 💡 Design HashMap - Solution Deep Dive

## 🧠 Architecture
- **Modulo Hash Function**: `hash_idx = key % BUCKET_SIZE` (prime number like 1009 to distribute evenly).
- **Collision Resolution**: Separate chaining using a list of `[key, value]` pairs at each bucket.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(1)$ average for put, get, remove.
- **Space Complexity**: $O(K)$ where $K$ is number of unique keys.
