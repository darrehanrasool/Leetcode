# 💡 Minimum Window Substring - Solution Deep Dive

## 🧠 Thought Process
1. Count target frequencies in `t` using `Counter(t)`.
2. Track:
   - `window_counts`: frequency of characters in current window.
   - `have`: number of distinct characters meeting target count.
   - `need`: number of distinct characters in `t`.
3. Expand `right`:
   - Add `s[right]` to `window_counts`.
   - If count matches target, `have += 1`.
4. While `have == need` (valid window):
   - Check if smaller than previous best window.
   - Shrink from `left` and update `have` if required.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(M + N)$ where $M = len(s)$ and $N = len(t)$.
- **Space Complexity**: $O(M + N)$ for frequency maps.
