# 💡 Koko Eating Bananas - Solution Deep Dive

## 🧠 Thought Process (Binary Search on Answer Space)
- Range of possible speeds: `low = 1`, `high = max(piles)`.
- Helper function `can_finish(speed)`:
  $$\text{hours} = \sum \lceil \text{pile} / \text{speed} \rceil$$
- If `hours <= h`: try slower speed $\rightarrow$ `high = mid`.
- Else: too slow! Must eat faster $\rightarrow$ `low = mid + 1`.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N \log(\max(piles)))$
- **Space Complexity**: $O(1)$
