# 💡 Longest Substring Without Repeating Characters - Solution Deep Dive

## 🧠 Thought Process
Use a dynamic sliding window `[left ... right]` and a hash map `char_index` storing `{character: latest_index_seen}`:
- Expand `right` from 0 to `len(s) - 1`.
- If `s[right]` is already in `char_index` and its recorded position is $\ge left$:
  - A duplicate exists inside our active window! Jump `left = char_index[s[right]] + 1`.
- Update `char_index[s[right]] = right`.
- Calculate window size: `right - left + 1` and update `max_len`.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N)$ — Each character is inspected by `right` once; `left` only moves forward.
- **Space Complexity**: $O(\min(N, \Sigma))$ — Where $\Sigma$ is the character set size (at most 128 ASCII chars).
