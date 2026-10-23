# 💡 Valid Palindrome - Solution Deep Dive

## 🧠 Thought Process
Instead of creating a new filtered string (which wastes $O(N)$ memory), we can use two pointers:
- `left` starts at index `0`.
- `right` starts at index `len(s) - 1`.
- While `left < right`:
  1. If `s[left]` is not alphanumeric, skip it: `left += 1`.
  2. If `s[right]` is not alphanumeric, skip it: `right -= 1`.
  3. If both are alphanumeric, compare them in lowercase:
     - If `s[left].lower() != s[right].lower()`, return `False` immediately.
     - Otherwise, move both pointers inward: `left += 1`, `right -= 1`.
- If pointers cross without mismatches, return `True`.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N)$ — Each character is visited at most once.
- **Space Complexity**: $O(1)$ — No extra string is allocated; we inspect characters directly in-place.
