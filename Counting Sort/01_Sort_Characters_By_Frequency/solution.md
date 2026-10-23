# 💡 Sort Colors - Solution Deep Dive

## 🧠 Dutch National Flag (3 Pointers)
- `low`: boundary for 0s
- `mid`: current scanner
- `high`: boundary for 2s
If `nums[mid] == 0`: swap with `low`, `low += 1`, `mid += 1`.
If `nums[mid] == 1`: `mid += 1`.
If `nums[mid] == 2`: swap with `high`, `high -= 1`.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N)$
- **Space Complexity**: $O(1)$
