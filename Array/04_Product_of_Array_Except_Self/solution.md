# 💡 Product of Array Except Self - Solution Deep Dive

---

## 🧠 Thought Process & Mental Model

For any element at index `i`:
$$\text{Product Except Self}[i] = (\text{product of all numbers to the left of } i) \times (\text{product of all numbers to the right of } i)$$

Let's name these two pieces:
- $\text{Prefix}[i]$ = product of all elements strictly to the left of `i`
- $\text{Suffix}[i]$ = product of all elements strictly to the right of `i`

If we have both of these arrays, our answer for each index is simply:
$$\text{output}[i] = \text{Prefix}[i] \times \text{Suffix}[i]$$

---

## 🛠️ Approaches

### Approach 1: Two Separate Arrays for Prefix and Suffix ($O(N)$ Time, $O(N)$ Space)

Let `nums = [1, 2, 3, 4]`

1. **Build `prefix` array**:
   - `prefix[0] = 1` (nothing to the left of index 0)
   - `prefix[1] = prefix[0] * nums[0] = 1 * 1 = 1`
   - `prefix[2] = prefix[1] * nums[1] = 1 * 2 = 2`
   - `prefix[3] = prefix[2] * nums[2] = 2 * 3 = 6`
   - Result: `prefix = [1, 1, 2, 6]`

2. **Build `suffix` array** (walking right to left):
   - `suffix[3] = 1` (nothing to the right of index 3)
   - `suffix[2] = suffix[3] * nums[3] = 1 * 4 = 4`
   - `suffix[1] = suffix[2] * nums[2] = 4 * 3 = 12`
   - `suffix[0] = suffix[1] * nums[1] = 12 * 2 = 24`
   - Result: `suffix = [24, 12, 4, 1]`

3. **Multiply them**:
   - `answer[0] = prefix[0] * suffix[0] = 1 * 24 = 24`
   - `answer[1] = prefix[1] * suffix[1] = 1 * 12 = 12`
   - `answer[2] = prefix[2] * suffix[2] = 2 * 4 = 8`
   - `answer[3] = prefix[3] * suffix[3] = 6 * 1 = 6`
   - Result: `[24, 12, 8, 6]` 🎯

---

### Approach 2: Memory-Optimized In-Place ($O(N)$ Time, $O(1)$ Extra Space) ⭐ OPTIMAL

We can eliminate both auxiliary `prefix` and `suffix` arrays:
1. Initialize the output array `res` of size $N$ with `1`s.
2. **Pass 1 (Left to Right)**: Store the prefix products directly inside `res`.
3. **Pass 2 (Right to Left)**: Maintain a single integer variable `suffix = 1`. As we walk backwards from $N-1$ down to 0, multiply `res[i]` by `suffix`, and then update `suffix *= nums[i]`.

This gives us the exact same result while using **zero extra memory structures**!

---

## 📊 Step-by-Step Visual Trace

Input: `nums = [1, 2, 3, 4]`

```
Step 1: Left-to-Right Pass (Prefix products into res)
  Initial: res = [1, 1, 1, 1]
  prefix = 1

  i = 0: res[0] = 1, prefix becomes 1 * nums[0] = 1
  i = 1: res[1] = 1, prefix becomes 1 * nums[1] = 2
  i = 2: res[2] = 2, prefix becomes 2 * nums[2] = 6
  i = 3: res[3] = 6, prefix becomes 6 * nums[3] = 24

  State of res: [1, 1, 2, 6]

Step 2: Right-to-Left Pass (Multiply by running suffix)
  suffix = 1

  i = 3: res[3] = res[3] * suffix = 6 * 1 = 6
         suffix becomes suffix * nums[3] = 1 * 4 = 4

  i = 2: res[2] = res[2] * suffix = 2 * 4 = 8
         suffix becomes suffix * nums[2] = 4 * 3 = 12

  i = 1: res[1] = res[1] * suffix = 1 * 12 = 12
         suffix becomes suffix * nums[1] = 12 * 2 = 24

  i = 0: res[0] = res[0] * suffix = 1 * 24 = 24
         suffix becomes suffix * nums[0] = 24 * 1 = 24

Final res: [24, 12, 8, 6] 🎯
```

```mermaid
flowchart LR
    subgraph Pass 1: Left to Right
    P1["res[i] = running_prefix"] --> P2["running_prefix *= nums[i]"]
    end
    subgraph Pass 2: Right to Left
    S1["res[i] *= running_suffix"] --> S2["running_suffix *= nums[i]"]
    end
    Pass 1 --> Pass 2
```

---

## ⏱️ Complexity Analysis

- **Time Complexity**: **$O(N)$**
  - Pass 1 runs $N$ times.
  - Pass 2 runs $N$ times.
  - Total operations = $2N$, which simplifies to $O(N)$ linear time.
- **Space Complexity**: **$O(1)$ Extra Auxiliary Space**
  - We only store a single scalar variable `suffix`.
  - The `res` array is the required output return value, so by standard interview rules it does not count against auxiliary space.

---

## 🤖 AI / Machine Learning Engineer Connection

- **Attention Masking in Transformers**: In causal self-attention (e.g. GPT architectures), tokens are only allowed to attend to tokens to their *left* (prefix), masking out tokens to their right.
- **Prefix Sums / Cumulative Products in Feature Engineering**: Computing moving averages, cumulative returns, or normalized cumulative distributions without repeated $O(N^2)$ recalculations relies directly on prefix arrays.
