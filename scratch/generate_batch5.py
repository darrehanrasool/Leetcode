#!/usr/bin/env python3
"""
Generator script for Batch 5:
- Dynamic Programming & Memoization
- Backtracking
- Greedy
- Matrix
"""

import os

def create_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Created: {path}")

# =====================================================================
# 1. DYNAMIC PROGRAMMING & MEMOIZATION
# =====================================================================

dp_readme = """# 🧩 Topic: Dynamic Programming & Memoization (Python DSA from Scratch)

## 🌟 1. Real-Life Analogy: What is Dynamic Programming?
Write down `"1 + 1 + 1 + 1 + 1 = 5"` on a piece of paper.
Now add another `+ 1` to the right: `"1 + 1 + 1 + 1 + 1 + 1"`.
How do you know the answer is 6?
Did you count all the ones from the beginning? **NO!** You remembered that the previous part was 5, and added 1!
$$\\text{Dynamic Programming} = \\text{Remembering the past to solve the future (Smart Recursion)}$$
- **Memoization (Top-Down)**: Normal recursion + cache dictionary.
- **Tabulation (Bottom-Up)**: Iterative array loop from base cases upward.

## 🤖 2. Why AI Engineers Care
- **Viterbi Algorithm & Hidden Markov Models (HMMs)**: Decoding sequence states in speech recognition and bioinformatics.
- **Beam Search & Sequence Decoding**: Calculating token likelihood paths with cumulative logits in LLMs.
- **Reinforcement Learning (Bellman Equation)**: Value iteration and Q-learning are pure dynamic programming!

## 📚 Problems in this Directory
1. `01_Climbing_Stairs` (Easy - Google, Apple)
2. `02_Coin_Change` (Medium - Meta, Amazon)
3. `03_Longest_Increasing_Subsequence` (Medium - Google, Microsoft)
4. `04_Word_Break` (Medium - Meta, Amazon)
"""

dp_p1_prob = """# 📖 Climbing Stairs (LeetCode #70)

- **Difficulty**: Easy
- **Asked By**: Google, Apple, Amazon
- **Frequency**: ⭐⭐⭐⭐⭐

## 💡 Real-Life Analogy
You can climb 1 or 2 steps at a time.
To reach step `n`, you either took a 1-step jump from step `n-1` OR a 2-step jump from step `n-2`.
Therefore: `ways(n) = ways(n-1) + ways(n-2)`. Fibonacci sequence!
"""

dp_p1_sol_md = """# 💡 Climbing Stairs - Solution Deep Dive

## 🧠 Thought Process
Base cases:
- `step 1`: 1 way
- `step 2`: 2 ways
Iterate up to `n`, maintaining only two variables `one` and `two`.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N)$
- **Space Complexity**: $O(1)$
"""

dp_p1_sol_py = '''"""
Problem: Climbing Stairs (LeetCode #70)
Bottom-Up DP with O(1) Space
Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        one, two = 1, 2
        for _ in range(3, n + 1):
            one, two = two, one + two

        return two

if __name__ == "__main__":
    sol = Solution()
    assert sol.climbStairs(2) == 2
    assert sol.climbStairs(3) == 3
    assert sol.climbStairs(5) == 8
    print("✅ All Climbing Stairs tests passed!")
'''

dp_p2_prob = """# 📖 Coin Change (LeetCode #322)

- **Difficulty**: Medium
- **Asked By**: Meta, Amazon, Microsoft
- **Frequency**: ⭐⭐⭐⭐⭐ (The canonical Unbounded Knapsack problem)
"""

dp_p2_sol_md = """# 💡 Coin Change - Solution Deep Dive

## 🧠 Thought Process (Bottom-Up Tabulation)
`dp[a]` represents the minimum coins needed to make amount `a`.
Initialize `dp = [inf] * (amount + 1)`, `dp[0] = 0`.
For each coin:
- For `a` from `coin` to `amount`:
  `dp[a] = min(dp[a], 1 + dp[a - coin])`

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(\\text{amount} \\times \\text{len(coins)})$
- **Space Complexity**: $O(\\text{amount})$
"""

dp_p2_sol_py = '''"""
Problem: Coin Change (LeetCode #322)
Bottom-Up Tabulation
Time Complexity: O(amount * len(coins))
Space Complexity: O(amount)
"""

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for a in range(coin, amount + 1):
                dp[a] = min(dp[a], 1 + dp[a - coin])

        return dp[amount] if dp[amount] != float("inf") else -1

if __name__ == "__main__":
    sol = Solution()
    assert sol.coinChange([1, 2, 5], 11) == 3
    assert sol.coinChange([2], 3) == -1
    assert sol.coinChange([1], 0) == 0
    print("✅ All Coin Change tests passed!")
'''

dp_p3_prob = """# 📖 Longest Increasing Subsequence (LeetCode #300)

- **Difficulty**: Medium
- **Asked By**: Google, Microsoft, Meta
- **Frequency**: ⭐⭐⭐⭐⭐
"""

dp_p3_sol_md = """# 💡 Longest Increasing Subsequence - Solution Deep Dive

## 🧠 Approaches
1. **Dynamic Programming ($O(N^2)$)**:
   `dp[i] = 1 + max(dp[j])` for all `j < i` where `nums[j] < nums[i]`.
2. **Patience Sorting + Binary Search ($O(N \\log N)$)**:
   Maintain active card piles with `bisect_left`.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N \\log N)$
- **Space Complexity**: $O(N)$
"""

dp_p3_sol_py = '''"""
Problem: Longest Increasing Subsequence (LeetCode #300)
Patience Sorting with Binary Search
Time Complexity: O(N log N)
Space Complexity: O(N)
"""

from bisect import bisect_left
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []

        for x in nums:
            idx = bisect_left(tails, x)
            if idx == len(tails):
                tails.append(x)
            else:
                tails[idx] = x

        return len(tails)

if __name__ == "__main__":
    sol = Solution()
    assert sol.lengthOfLIS([10,9,2,5,3,7,101,18]) == 4
    assert sol.lengthOfLIS([0,1,0,3,2,3]) == 4
    assert sol.lengthOfLIS([7,7,7,7,7,7,7]) == 1
    print("✅ All Longest Increasing Subsequence tests passed!")
'''

dp_p4_prob = """# 📖 Word Break (LeetCode #139)

- **Difficulty**: Medium
- **Asked By**: Meta, Amazon, Apple
- **Frequency**: ⭐⭐⭐⭐⭐
"""

dp_p4_sol_md = """# 💡 Word Break - Solution Deep Dive

## 🧠 Thought Process
`dp[i]` is True if `s[0...i]` can be segmented using dictionary words.
`dp[0] = True` (empty string).
For `i` from 1 to `len(s)`:
- For `j` from 0 to `i`:
  - If `dp[j] and s[j:i] in word_set`: `dp[i] = True; break`.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N^2 \\times L)$
- **Space Complexity**: $O(N)$
"""

dp_p4_sol_py = '''"""
Problem: Word Break (LeetCode #139)
Dynamic Programming with Hash Set
Time Complexity: O(N^2)
Space Complexity: O(N)
"""

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break

        return dp[n]

if __name__ == "__main__":
    sol = Solution()
    assert sol.wordBreak("leetcode", ["leet", "code"]) is True
    assert sol.wordBreak("applepenapple", ["apple", "pen"]) is True
    assert sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) is False
    print("✅ All Word Break tests passed!")
'''

print("Writing Dynamic Programming & Memoization files...")
create_file("Dynamic Programming/README.md", dp_readme)
create_file("Dynamic Programming/01_Climbing_Stairs/problem.md", dp_p1_prob)
create_file("Dynamic Programming/01_Climbing_Stairs/solution.md", dp_p1_sol_md)
create_file("Dynamic Programming/01_Climbing_Stairs/solution.py", dp_p1_sol_py)

create_file("Dynamic Programming/02_Coin_Change/problem.md", dp_p2_prob)
create_file("Dynamic Programming/02_Coin_Change/solution.md", dp_p2_sol_md)
create_file("Dynamic Programming/02_Coin_Change/solution.py", dp_p2_sol_py)

create_file("Dynamic Programming/03_Longest_Increasing_Subsequence/problem.md", dp_p3_prob)
create_file("Dynamic Programming/03_Longest_Increasing_Subsequence/solution.md", dp_p3_sol_md)
create_file("Dynamic Programming/03_Longest_Increasing_Subsequence/solution.py", dp_p3_sol_py)

create_file("Dynamic Programming/04_Word_Break/problem.md", dp_p4_prob)
create_file("Dynamic Programming/04_Word_Break/solution.md", dp_p4_sol_md)
create_file("Dynamic Programming/04_Word_Break/solution.py", dp_p4_sol_py)

create_file("Memoization/README.md", dp_readme)
create_file("Memoization/01_Climbing_Stairs/problem.md", dp_p1_prob)
create_file("Memoization/01_Climbing_Stairs/solution.md", dp_p1_sol_md)
create_file("Memoization/01_Climbing_Stairs/solution.py", dp_p1_sol_py)

# =====================================================================
# 2. BACKTRACKING
# =====================================================================

bt_readme = """# 🔄 Topic: Backtracking (Python DSA from Scratch)

## 🌟 1. Real-Life Analogy: What is Backtracking?
Solving a **maze with a ball of yarn**:
- At every fork in the road, make a choice and unwind yarn.
- If you hit a dead end, rewind the yarn (undo your decision) and try the other fork!
$$\\text{Backtracking Pattern}: \\quad \\text{Choose} \\rightarrow \\text{Explore} \\rightarrow \\text{Unchoose (Backtrack)}$$

## 🤖 2. Why AI Engineers Care
- **Prompt Tree Search & Reasoning Chains (MCTS / Tree-of-Thoughts)**: Exploring different reasoning trajectories and pruning invalid chains of thought.
- **Combinatorial Hyperparameter Tuning**: Generating all valid feature set permutations.

## 📚 Problems in this Directory
1. `01_Subsets` (Medium - Meta, Google)
2. `02_Combination_Sum` (Medium - Meta, Airbnb)
3. `03_Permutations` (Medium - Meta, Amazon)
4. `04_Word_Search` (Medium - Amazon, Bloomberg)
"""

bt_p1_prob = """# 📖 Subsets (LeetCode #78)

- **Difficulty**: Medium
- **Asked By**: Meta, Google, Amazon
- **Frequency**: ⭐⭐⭐⭐⭐ (The canonical Power Set problem)
"""

bt_p1_sol_md = """# 💡 Subsets - Solution Deep Dive

## 🧠 Thought Process
For each element, we have a binary choice: include it or exclude it!
Tree has depth $N$ and $2^N$ leaves.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N \\times 2^N)$
- **Space Complexity**: $O(N)$
"""

bt_p1_sol_py = '''"""
Problem: Subsets (LeetCode #78)
Backtracking Power Set Generation
Time Complexity: O(N * 2^N)
Space Complexity: O(N)
"""

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            # Decision 1: Include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # Backtrack
            subset.pop()

            # Decision 2: Do NOT include nums[i]
            dfs(i + 1)

        dfs(0)
        return res

if __name__ == "__main__":
    sol = Solution()
    res = sol.subsets([1, 2, 3])
    assert len(res) == 8
    assert [] in res and [1, 2, 3] in res
    print("✅ All Subsets tests passed!")
'''

bt_p2_prob = """# 📖 Combination Sum (LeetCode #39)

- **Difficulty**: Medium
- **Asked By**: Meta, Airbnb, Google
- **Frequency**: ⭐⭐⭐⭐⭐
"""

bt_p2_sol_md = """# 💡 Combination Sum - Solution Deep Dive

## 🧠 Thought Process
Backtracking recursion where elements can be reused unlimited times.
At each index `i`:
- If `total == target`: record combination.
- If `total > target` or `i >= len(candidates)`: return.
- Include `candidates[i]` (stay at index `i`).
- Backtrack, then explore without `candidates[i]` (advance to `i + 1`).
"""

bt_p2_sol_py = '''"""
Problem: Combination Sum (LeetCode #39)
Backtracking with Element Reuse
"""

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if total > target or i >= len(candidates):
                return

            # Include candidates[i]
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])

            # Backtrack
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res

if __name__ == "__main__":
    sol = Solution()
    assert sol.combinationSum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
    assert sol.combinationSum([2], 1) == []
    print("✅ All Combination Sum tests passed!")
'''

bt_p3_prob = """# 📖 Permutations (LeetCode #46)

- **Difficulty**: Medium
- **Asked By**: Meta, Amazon, Microsoft
- **Frequency**: ⭐⭐⭐⭐⭐
"""

bt_p3_sol_md = """# 💡 Permutations - Solution Deep Dive

## 🧠 Thought Process
Use a boolean visited array or set.
Explore all unused numbers at each level.
"""

bt_p3_sol_py = '''"""
Problem: Permutations (LeetCode #46)
Backtracking Permutation Generation
Time Complexity: O(N * N!)
"""

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(perm, visited):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for num in nums:
                if num not in visited:
                    visited.add(num)
                    perm.append(num)
                    backtrack(perm, visited)
                    perm.pop()
                    visited.remove(num)

        backtrack([], set())
        return res

if __name__ == "__main__":
    sol = Solution()
    res = sol.permute([1, 2, 3])
    assert len(res) == 6
    print("✅ All Permutations tests passed!")
'''

bt_p4_prob = """# 📖 Word Search (LeetCode #79)

- **Difficulty**: Medium
- **Asked By**: Amazon, Bloomberg, Meta
- **Frequency**: ⭐⭐⭐⭐⭐
"""

bt_p4_sol_md = """# 💡 Word Search - Solution Deep Dive

## 🧠 Thought Process (Grid DFS with In-Place Visited Marking)
For each matching start letter:
- Temporarily mark cell as visited: `board[r][c] = "#"`.
- Recursively explore 4 directions for `word[idx + 1]`.
- Restore cell: `board[r][c] = char`.
"""

bt_p4_sol_py = '''"""
Problem: Word Search (LeetCode #79)
Grid Backtracking
Time Complexity: O(M * N * 4^L)
"""

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
                return False

            temp = board[r][c]
            board[r][c] = "#"  # Mark visited in-place

            found = (dfs(r + 1, c, i + 1) or
                     dfs(r - 1, c, i + 1) or
                     dfs(r, c + 1, i + 1) or
                     dfs(r, c - 1, i + 1))

            board[r][c] = temp  # Backtrack
            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False

if __name__ == "__main__":
    sol = Solution()
    b = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    assert sol.exist(b, "ABCCED") is True
    assert sol.exist(b, "SEE") is True
    assert sol.exist(b, "ABCB") is False
    print("✅ All Word Search tests passed!")
'''

print("Writing Backtracking files...")
create_file("Backtracking/README.md", bt_readme)
create_file("Backtracking/01_Subsets/problem.md", bt_p1_prob)
create_file("Backtracking/01_Subsets/solution.md", bt_p1_sol_md)
create_file("Backtracking/01_Subsets/solution.py", bt_p1_sol_py)

create_file("Backtracking/02_Combination_Sum/problem.md", bt_p2_prob)
create_file("Backtracking/02_Combination_Sum/solution.md", bt_p2_sol_md)
create_file("Backtracking/02_Combination_Sum/solution.py", bt_p2_sol_py)

create_file("Backtracking/03_Permutations/problem.md", bt_p3_prob)
create_file("Backtracking/03_Permutations/solution.md", bt_p3_sol_md)
create_file("Backtracking/03_Permutations/solution.py", bt_p3_sol_py)

create_file("Backtracking/04_Word_Search/problem.md", bt_p4_prob)
create_file("Backtracking/04_Word_Search/solution.md", bt_p4_sol_md)
create_file("Backtracking/04_Word_Search/solution.py", bt_p4_sol_py)

# =====================================================================
# 3. GREEDY
# =====================================================================

greedy_readme = """# 💰 Topic: Greedy Algorithms (Python DSA from Scratch)

## 🌟 1. Real-Life Analogy
A Greedy algorithm makes the **locally optimal choice at each step**, hoping to find the global optimum:
Like giving change in coins: always give the largest possible coin denomination first!

## 🤖 2. Why AI Engineers Care
- **Greedy Decoding in LLMs (`temperature = 0`)**: Always selecting `argmax` of token logits at each step.
- **Loss Reduction**: Gradient descent is essentially a continuous greedy step along the steepest negative gradient!

## 📚 Problems in this Directory
1. `01_Jump_Game` (Medium - Amazon, Meta)
2. `02_Gas_Station` (Medium - Google, Meta)
"""

gr_p1_prob = """# 📖 Jump Game (LeetCode #55)

- **Difficulty**: Medium
- **Asked By**: Amazon, Meta, Google
- **Frequency**: ⭐⭐⭐⭐⭐
"""

gr_p1_sol_md = """# 💡 Jump Game - Solution Deep Dive

## 🧠 Thought Process
Walk backwards from final goal:
Set `goal = len(nums) - 1`.
For `i` from `len(nums) - 2` down to 0:
- If `i + nums[i] >= goal`: we can reach goal from `i`! Shift `goal = i`.
Return `goal == 0`.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N)$
- **Space Complexity**: $O(1)$
"""

gr_p1_sol_py = '''"""
Problem: Jump Game (LeetCode #55)
Greedy Backward Goal Shift
Time Complexity: O(N)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return goal == 0

if __name__ == "__main__":
    sol = Solution()
    assert sol.canJump([2, 3, 1, 1, 4]) is True
    assert sol.canJump([3, 2, 1, 0, 4]) is False
    print("✅ All Jump Game tests passed!")
'''

gr_p2_prob = """# 📖 Gas Station (LeetCode #134)

- **Difficulty**: Medium
- **Asked By**: Google, Meta
- **Frequency**: ⭐⭐⭐⭐⭐
"""

gr_p2_sol_md = """# 💡 Gas Station - Solution Deep Dive

## 🧠 Thought Process
If total gas < total cost, complete circuit is impossible (return -1).
Otherwise, a unique starting index is guaranteed!
Maintain running tank: if running tank < 0, reset tank to 0 and set starting station to `i + 1`.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N)$
- **Space Complexity**: $O(1)$
"""

gr_p2_sol_py = '''"""
Problem: Gas Station (LeetCode #134)
Single-Pass Greedy Running Tank
Time Complexity: O(N)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total_tank = 0
        start = 0

        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            if total_tank < 0:
                total_tank = 0
                start = i + 1

        return start

if __name__ == "__main__":
    sol = Solution()
    assert sol.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]) == 3
    assert sol.canCompleteCircuit([2,3,4], [3,4,3]) == -1
    print("✅ All Gas Station tests passed!")
'''

print("Writing Greedy files...")
create_file("Greedy/README.md", greedy_readme)
create_file("Greedy/01_Jump_Game/problem.md", gr_p1_prob)
create_file("Greedy/01_Jump_Game/solution.md", gr_p1_sol_md)
create_file("Greedy/01_Jump_Game/solution.py", gr_p1_sol_py)

create_file("Greedy/02_Gas_Station/problem.md", gr_p2_prob)
create_file("Greedy/02_Gas_Station/solution.md", gr_p2_sol_md)
create_file("Greedy/02_Gas_Station/solution.py", gr_p2_sol_py)

# =====================================================================
# 4. MATRIX
# =====================================================================

matrix_readme = """# 🔲 Topic: Matrix (Python DSA from Scratch)

## 🌟 1. Real-Life Analogy
A spreadsheet grid or a 2D digital image of pixels: `matrix[row][col]`.

## 🤖 2. Why AI Engineers Care
- **2D Tensors, Image Processing & Attention Weight Matrices**: Self-attention matrices ($Q K^T / \\sqrt{d_k}$) in transformers are square 2D matrices.
- **Kernel Convolutions & Striding**: Navigating 2D row/col coordinates.

## 📚 Problems in this Directory
1. `01_Set_Matrix_Zeroes` (Medium - Meta, Amazon)
2. `02_Spiral_Matrix` (Medium - Microsoft, Apple, Google)
"""

mat_p1_prob = """# 📖 Set Matrix Zeroes (LeetCode #73)

- **Difficulty**: Medium
- **Asked By**: Meta, Amazon, Microsoft
- **Frequency**: ⭐⭐⭐⭐⭐
"""

mat_p1_sol_md = """# 💡 Set Matrix Zeroes - Solution Deep Dive

## 🧠 Thought Process (In-Place $O(1)$ Space)
Use the first row and first column of the matrix itself as markers!
Track whether the first row or first column originally had zeroes using two boolean flags.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(M \\times N)$
- **Space Complexity**: $O(1)$ in-place!
"""

mat_p1_sol_py = '''"""
Problem: Set Matrix Zeroes (LeetCode #73)
In-Place O(1) Auxiliary Space
Time Complexity: O(M * N)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        first_row_zero = any(matrix[0][c] == 0 for c in range(cols))
        first_col_zero = any(matrix[r][0] == 0 for r in range(rows))

        # Use first row and column as markers
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        # Zero out inner cells based on markers
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # Handle first row and col
        if first_row_zero:
            for c in range(cols):
                matrix[0][c] = 0
        if first_col_zero:
            for r in range(rows):
                matrix[r][0] = 0

if __name__ == "__main__":
    sol = Solution()
    m = [[1,1,1],[1,0,1],[1,1,1]]
    sol.setZeroes(m)
    assert m == [[1,0,1],[0,0,0],[1,0,1]]
    print("✅ All Set Matrix Zeroes tests passed!")
'''

mat_p2_prob = """# 📖 Spiral Matrix (LeetCode #54)

- **Difficulty**: Medium
- **Asked By**: Microsoft, Apple, Google, Meta
- **Frequency**: ⭐⭐⭐⭐⭐
"""

mat_p2_sol_md = """# 💡 Spiral Matrix - Solution Deep Dive

## 🧠 Thought Process (4 Boundary Pointers)
Maintain `top`, `bottom`, `left`, `right`.
Traverse:
1. Top row: `left` to `right`, then `top += 1`.
2. Right col: `top` to `bottom`, then `right -= 1`.
3. Bottom row: `right` to `left`, then `bottom -= 1`.
4. Left col: `bottom` to `top`, then `left += 1`.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(M \\times N)$
- **Space Complexity**: $O(1)$ auxiliary space.
"""

mat_p2_sol_py = '''"""
Problem: Spiral Matrix (LeetCode #54)
4 Boundary Pointer Shrink
Time Complexity: O(M * N)
Space Complexity: O(1) auxiliary
"""

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix:
            return res

        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # 1. Traverse top row
            for c in range(left, right + 1):
                res.append(matrix[top][c])
            top += 1

            # 2. Traverse right column
            for r in range(top, bottom + 1):
                res.append(matrix[r][right])
            right -= 1

            # 3. Traverse bottom row if valid
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    res.append(matrix[bottom][c])
                bottom -= 1

            # 4. Traverse left column if valid
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    res.append(matrix[r][left])
                left += 1

        return res

if __name__ == "__main__":
    sol = Solution()
    assert sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5]
    assert sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1,2,3,4,8,12,11,10,9,5,6,7]
    print("✅ All Spiral Matrix tests passed!")
'''

print("Writing Matrix files...")
create_file("Matrix/README.md", matrix_readme)
create_file("Matrix/01_Set_Matrix_Zeroes/problem.md", mat_p1_prob)
create_file("Matrix/01_Set_Matrix_Zeroes/solution.md", mat_p1_sol_md)
create_file("Matrix/01_Set_Matrix_Zeroes/solution.py", mat_p1_sol_py)

create_file("Matrix/02_Spiral_Matrix/problem.md", mat_p2_prob)
create_file("Matrix/02_Spiral_Matrix/solution.md", mat_p2_sol_md)
create_file("Matrix/02_Spiral_Matrix/solution.py", mat_p2_sol_py)

print("Batch 5 generated successfully!")
