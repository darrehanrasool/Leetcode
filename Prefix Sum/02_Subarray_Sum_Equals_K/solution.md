# 💡 Subarray Sum Equals K - Solution Deep Dive

## 🧠 Thought Process
Running prefix sum:
$$\text{prefix}[j] - \text{prefix}[i] = k \implies \text{prefix}[i] = \text{prefix}[j] - k$$
We maintain a hash map `prefix_counts` recording how many times each prefix sum has occurred.
Initialize `prefix_counts = {0: 1}` (empty subarray has sum 0).

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N)$ — Single pass over array.
- **Space Complexity**: $O(N)$ for prefix count map.
