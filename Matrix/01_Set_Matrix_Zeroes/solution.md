# 💡 Set Matrix Zeroes - Solution Deep Dive

## 🧠 Thought Process (In-Place $O(1)$ Space)
Use the first row and first column of the matrix itself as markers!
Track whether the first row or first column originally had zeroes using two boolean flags.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(M \times N)$
- **Space Complexity**: $O(1)$ in-place!
