#!/usr/bin/env python3
"""
Generator script for Batch 1:
- Two Pointers
- Sliding Window
- String
- Hash Table
- Hash Function
- Prefix Sum
"""

import os

def create_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Created: {path}")

# =====================================================================
# 1. TWO POINTERS
# =====================================================================

two_pointers_readme = """# 🎯 Topic: Two Pointers (Python DSA from Scratch)

## 🌟 1. Real-Life Analogy: What is the Two Pointers Technique?
Imagine two people walking toward each other on opposite ends of a narrow hallway:
- Person **L** (Left pointer) starts at the very beginning (index 0).
- Person **R** (Right pointer) starts at the very end (index N - 1).
- Based on what they see or want, one steps forward, or the other steps backward, or both step inward until they meet in the middle.

```
Start:
  L                                       R
 [ 1 ,   2 ,   3 ,   4 ,   5 ,   6 ,   7 ,   8 ]
   ─────────────────>         <─────────────────
```

Another variation is **Fast & Slow Pointers** (Hare and Tortoise), like a sports runner (moves 2 steps) and a walker (moves 1 step) to detect cycles or find the midpoint of a track.

## 🤖 2. Why AI Engineers Care
- **Embedding Alignment & Similarity Matching**: Comparing pairs of sequences or finding optimal thresholds.
- **Data Filtering & Cleaning**: Removing invalid tokens or nulls in-place without copying large memory buffers ($O(1)$ space).
- **Sequence Palindromes & Symmetric Embeddings**: In genomics and bio-sequence transformers (AlphaFold, ESM-2), palindromic hairpin loop detection is done via two-pointer convergence.

## ⚙️ 3. Time & Space Complexity Advantage
- **Without Two Pointers**: Nested loops testing every pair $\\rightarrow O(N^2)$ Time.
- **With Two Pointers**: Pointers only move inward, visiting each element at most once $\\rightarrow O(N)$ Time and **$O(1)$ Auxiliary Space**!

## 📚 Problems in this Directory
1. `01_Valid_Palindrome` (Easy - Google, Meta)
2. `02_Two_Sum_II_Input_Array_Is_Sorted` (Medium - Amazon, Meta)
3. `03_3Sum` (Medium - Meta #1 asked, Google, Apple)
4. `04_Container_With_Most_Water` (Medium - Google, Meta, Startups)
"""

# Two Pointers - 01_Valid_Palindrome
tp_p1_prob = """# 📖 Valid Palindrome (LeetCode #125)

- **Difficulty**: Easy
- **Asked By**: Meta (Facebook - High Frequency), Google, Microsoft, Amazon, Apple
- **Frequency**: ⭐⭐⭐⭐⭐

## 💡 Real-Life Analogy
A palindrome is a phrase that reads the same forwards and backwards, ignoring spaces and punctuation.
Like the word **"RACECAR"** or the famous phrase:
> *"A man, a plan, a canal: Panama!"*

If you place your left finger at the first letter **'A'** and your right finger at the last letter **'a'**, and move both inward skipping spaces and colons, your fingers will always point to identical letters!

## 📋 Problem Statement
A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

### Examples
- **Input**: `s = "A man, a plan, a canal: Panama"`
- **Output**: `true`
- **Explanation**: "amanaplanacanalpanama" is a palindrome.

- **Input**: `s = "race a car"`
- **Output**: `false`
- **Explanation**: "raceacar" is not a palindrome.

## 🎨 Visual Diagram
```
"A   m a n ,   a   p l a n ,   a   c a n a l :   P a n a m a"
 L ────────────────────────────────────────────────────────> R
 L='a', R='a' -> Match! Both move inward.
```

## ⚠️ Constraints & Edge Cases
- `1 <= s.length <= 2 * 10^5`
- `s` consists only of printable ASCII characters.
- **Empty string or string with only symbols** (e.g. `", . :"`): After cleaning, it is empty `""`, which is considered a valid palindrome (`true`).
"""

tp_p1_sol_md = """# 💡 Valid Palindrome - Solution Deep Dive

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
"""

tp_p1_sol_py = '''"""
Problem: Valid Palindrome (LeetCode #125)
Two Pointers In-Place Approach
Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize left pointer at the start and right pointer at the end
        left = 0
        right = len(s) - 1

        while left < right:
            # Skip non-alphanumeric characters on the left side
            while left < right and not s[left].isalnum():
                left += 1

            # Skip non-alphanumeric characters on the right side
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare characters ignoring case
            if s[left].lower() != s[right].lower():
                return False

            # Move both pointers inward
            left += 1
            right -= 1

        return True

if __name__ == "__main__":
    sol = Solution()
    t1 = "A man, a plan, a canal: Panama"
    t2 = "race a car"
    t3 = " "
    assert sol.isPalindrome(t1) is True
    assert sol.isPalindrome(t2) is False
    assert sol.isPalindrome(t3) is True
    print("✅ All Valid Palindrome tests passed!")
'''

# Two Pointers - 02_Two_Sum_II
tp_p2_prob = """# 📖 Two Sum II - Input Array Is Sorted (LeetCode #167)

- **Difficulty**: Medium
- **Asked By**: Amazon, Meta, Google, Apple
- **Frequency**: ⭐⭐⭐⭐⭐

## 💡 Real-Life Analogy
Imagine numbers on a sorted ruler:
`numbers = [2, 7, 11, 15]`, `target = 9`.
- Left finger at minimum number `2`.
- Right finger at maximum number `15`.
- Current sum = `2 + 15 = 17`. Too big! How do we make the sum smaller? Move the right finger to a smaller number.
- Next sum = `2 + 11 = 13`. Still too big! Move right finger left again.
- Next sum = `2 + 7 = 9`. Perfect match!

## 📋 Problem Statement
Given a **1-indexed** array of integers `numbers` that is already **sorted in non-decreasing order**, find two numbers such that they add up to a specific `target` number.

Return the indices of the two numbers, `index1` and `index2`, added by one as an integer array `[index1, index2]` of length 2.

**Constraint**: You must use only **$O(1)$ extra space**.

### Examples
- **Input**: `numbers = [2, 7, 11, 15]`, `target = 9`
- **Output**: `[1, 2]`
"""

tp_p2_sol_md = """# 💡 Two Sum II - Solution Deep Dive

## 🧠 Thought Process
Because the array is already **sorted**, we don't need a hash map ($O(N)$ space):
- If `numbers[left] + numbers[right] > target`: The sum is too large. Since all numbers to the right are even larger, the only way to decrease the sum is `right -= 1`.
- If `numbers[left] + numbers[right] < target`: The sum is too small. The only way to increase the sum is `left += 1`.
- If equal: We found our answer! Return `[left + 1, right + 1]` (1-indexed).

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N)$ — Pointers move inward by 1 at each step.
- **Space Complexity**: $O(1)$ — Only two integer pointers used.
"""

tp_p2_sol_py = '''"""
Problem: Two Sum II - Input Array Is Sorted (LeetCode #167)
Two Pointers Inward Convergence
Time Complexity: O(N)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                # 1-indexed response required by problem
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1  # Need a larger sum
            else:
                right -= 1  # Need a smaller sum

        return []

if __name__ == "__main__":
    sol = Solution()
    assert sol.twoSum([2, 7, 11, 15], 9) == [1, 2]
    assert sol.twoSum([2, 3, 4], 6) == [1, 3]
    assert sol.twoSum([-1, 0], -1) == [1, 2]
    print("✅ All Two Sum II tests passed!")
'''

# Two Pointers - 03_3Sum
tp_p3_prob = """# 📖 3Sum (LeetCode #15)

- **Difficulty**: Medium
- **Asked By**: Meta (Top 3 most asked), Google, Amazon, Microsoft, Apple
- **Frequency**: ⭐⭐⭐⭐⭐

## 💡 Real-Life Analogy
You are organizing a 3-person committee where their skill budget must balance out to 0:
$a + b + c = 0$.
To avoid duplicate committees, you first line up all candidates by rank (sort them).
You fix candidate $a$, then use Two Pointers to find complementary pairs $b$ and $c$ such that $b + c = -a$.

## 📋 Problem Statement
Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must **not contain duplicate triplets**.

### Examples
- **Input**: `nums = [-1, 0, 1, 2, -1, -4]`
- **Output**: `[[-1, -1, 2], [-1, 0, 1]]`
"""

tp_p3_sol_md = """# 💡 3Sum - Solution Deep Dive

## 🧠 Thought Process
1. **Sort the array**: Allows us to use Two Pointers and easily skip duplicate values.
2. **Iterate with index `i`**: For each `nums[i]`:
   - If `nums[i] > 0`: Stop early! Since the array is sorted, three positive numbers can never sum to 0.
   - If `i > 0 and nums[i] == nums[i - 1]`: Skip to avoid duplicate triplets.
   - Set `left = i + 1`, `right = len(nums) - 1`.
   - While `left < right`:
     - `total = nums[i] + nums[left] + nums[right]`
     - If `total == 0`: record triplet, then advance `left` and `right` skipping any duplicates.
     - If `total < 0`: `left += 1`.
     - If `total > 0`: `right -= 1`.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N^2)$ — Sorting takes $O(N \\log N)$, outer loop runs $N$ times with an $O(N)$ two-pointer scan.
- **Space Complexity**: $O(1)$ auxiliary space (ignoring sorting and output array).
"""

tp_p3_sol_py = '''"""
Problem: 3Sum (LeetCode #15)
Sorting + Two Pointers
Time Complexity: O(N^2)
Space Complexity: O(1) auxiliary
"""

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n - 2):
            # If current element is positive, sum of three positive numbers cannot be zero
            if nums[i] > 0:
                break

            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])

                    # Skip duplicate values for the second element
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicate values for the third element
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return res

if __name__ == "__main__":
    sol = Solution()
    assert sol.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert sol.threeSum([0, 1, 1]) == []
    assert sol.threeSum([0, 0, 0]) == [[0, 0, 0]]
    print("✅ All 3Sum tests passed!")
'''

# Two Pointers - 04_Container_With_Most_Water
tp_p4_prob = """# 📖 Container With Most Water (LeetCode #11)

- **Difficulty**: Medium
- **Asked By**: Google, Meta, Amazon, Adobe
- **Frequency**: ⭐⭐⭐⭐⭐

## 💡 Real-Life Analogy
Imagine two vertical wooden posts holding water between them:
The water level is limited by the **shorter post** (water spills over the lower edge).
$$\\text{Area} = \\min(\\text{height}_1, \\text{height}_2) \\times \\text{distance}$$
To find the biggest tank, start with posts at maximum distance (left=0, right=N-1).
To have any chance of finding a bigger container, you MUST replace the shorter post with a taller one!

## 📋 Problem Statement
Given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i`-th line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the **maximum amount of water** a container can store.

### Examples
- **Input**: `height = [1, 8, 6, 2, 5, 4, 8, 3, 7]`
- **Output**: `49`
- **Explanation**: Lines at index 1 (height 8) and index 8 (height 7) hold `min(8, 7) * (8 - 1) = 7 * 7 = 49`.
"""

tp_p4_sol_md = """# 💡 Container With Most Water - Solution Deep Dive

## 🧠 Thought Process & Invariant
Start with maximum width: `left = 0`, `right = len(height) - 1`.
At each step:
$$\\text{Current Area} = \\min(\\text{height}[left], \\text{height}[right]) \\times (right - left)$$
Which pointer should we move?
- The width will decrease by 1 regardless of which pointer moves.
- Moving the taller post will NEVER increase the area because the height is bottle-necked by the shorter post.
- Therefore, the ONLY move that could potentially yield a larger area is moving the **shorter pointer inward**!

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N)$ — Single pass inward.
- **Space Complexity**: $O(1)$ — Only tracking max area and two pointers.
"""

tp_p4_sol_py = '''"""
Problem: Container With Most Water (LeetCode #11)
Two Pointers Greedy Squeeze
Time Complexity: O(N)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            width = right - left
            h = min(height[left], height[right])
            current_water = width * h
            max_water = max(max_water, current_water)

            # Greedily move the shorter boundary inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water

if __name__ == "__main__":
    sol = Solution()
    assert sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert sol.maxArea([1, 1]) == 1
    print("✅ All Container With Most Water tests passed!")
'''

print("Writing Two Pointers files...")
create_file("Two Pointers/README.md", two_pointers_readme)
create_file("Two Pointers/01_Valid_Palindrome/problem.md", tp_p1_prob)
create_file("Two Pointers/01_Valid_Palindrome/solution.md", tp_p1_sol_md)
create_file("Two Pointers/01_Valid_Palindrome/solution.py", tp_p1_sol_py)

create_file("Two Pointers/02_Two_Sum_II_Input_Array_Is_Sorted/problem.md", tp_p2_prob)
create_file("Two Pointers/02_Two_Sum_II_Input_Array_Is_Sorted/solution.md", tp_p2_sol_md)
create_file("Two Pointers/02_Two_Sum_II_Input_Array_Is_Sorted/solution.py", tp_p2_sol_py)

create_file("Two Pointers/03_3Sum/problem.md", tp_p3_prob)
create_file("Two Pointers/03_3Sum/solution.md", tp_p3_sol_md)
create_file("Two Pointers/03_3Sum/solution.py", tp_p3_sol_py)

create_file("Two Pointers/04_Container_With_Most_Water/problem.md", tp_p4_prob)
create_file("Two Pointers/04_Container_With_Most_Water/solution.md", tp_p4_sol_md)
create_file("Two Pointers/04_Container_With_Most_Water/solution.py", tp_p4_sol_py)

# =====================================================================
# 2. SLIDING WINDOW
# =====================================================================

sliding_window_readme = """# 🪟 Topic: Sliding Window (Python DSA from Scratch)

## 🌟 1. Real-Life Analogy: What is a Sliding Window?
Imagine a **magnifying glass** or a **moving camera frame** scanning across a film strip:
- The window has a `left` edge and a `right` edge: `[left ... right]`.
- As the camera moves right, new objects enter the frame.
- If the frame becomes invalid (e.g. too noisy or contains duplicate items), we shrink the frame by sliding the `left` edge forward.

## 🤖 2. Why AI Engineers Care
- **Token Context Windows in LLMs**: Sliding context windows are how LLMs process documents longer than their context length (e.g. 8K tokens window sliding over a 100K token book).
- **Time Series Feature Engineering**: Moving averages, rolling volatility, and rolling standard deviation over financial or sensor metrics.
- **Convolution in CNNs**: A convolutional kernel sliding over pixel matrices is a 2D sliding window!

## 📚 Problems in this Directory
1. `01_Longest_Substring_Without_Repeating_Characters` (Medium - Google, Meta, Amazon)
2. `02_Minimum_Window_Substring` (Hard - Meta, Google, Airbnb)
"""

sw_p1_prob = """# 📖 Longest Substring Without Repeating Characters (LeetCode #3)

- **Difficulty**: Medium
- **Asked By**: Google, Meta (Facebook), Amazon, Microsoft, Apple
- **Frequency**: ⭐⭐⭐⭐⭐

## 💡 Real-Life Analogy
Imagine typing on a keyboard, and you want to see what is the longest uninterrupted string of letters you can type before you hit a letter you already typed in the current word.
Whenever you hit a repeated letter, you slide your starting marker forward past the first occurrence of that letter!

## 📋 Problem Statement
Given a string `s`, find the length of the **longest substring** without repeating characters.

### Examples
- **Input**: `s = "abcabcbb"`
- **Output**: `3` ("abc")
- **Input**: `s = "bbbbb"`
- **Output**: `1` ("b")
- **Input**: `s = "pwwkew"`
- **Output**: `3` ("wke")
"""

sw_p1_sol_md = """# 💡 Longest Substring Without Repeating Characters - Solution Deep Dive

## 🧠 Thought Process
Use a dynamic sliding window `[left ... right]` and a hash map `char_index` storing `{character: latest_index_seen}`:
- Expand `right` from 0 to `len(s) - 1`.
- If `s[right]` is already in `char_index` and its recorded position is $\\ge left$:
  - A duplicate exists inside our active window! Jump `left = char_index[s[right]] + 1`.
- Update `char_index[s[right]] = right`.
- Calculate window size: `right - left + 1` and update `max_len`.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N)$ — Each character is inspected by `right` once; `left` only moves forward.
- **Space Complexity**: $O(\\min(N, \\Sigma))$ — Where $\\Sigma$ is the character set size (at most 128 ASCII chars).
"""

sw_p1_sol_py = '''"""
Problem: Longest Substring Without Repeating Characters (LeetCode #3)
Sliding Window with Hash Map Index Tracking
Time Complexity: O(N)
Space Complexity: O(min(N, M))
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        left = 0
        max_length = 0

        for right, char in enumerate(s):
            # If char was seen inside the current window, move left past its previous index
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1

            char_index[char] = right
            max_length = max(max_length, right - left + 1)

        return max_length

if __name__ == "__main__":
    sol = Solution()
    assert sol.lengthOfLongestSubstring("abcabcbb") == 3
    assert sol.lengthOfLongestSubstring("bbbbb") == 1
    assert sol.lengthOfLongestSubstring("pwwkew") == 3
    assert sol.lengthOfLongestSubstring("") == 0
    print("✅ All Longest Substring Without Repeating Characters tests passed!")
'''

sw_p2_prob = """# 📖 Minimum Window Substring (LeetCode #76)

- **Difficulty**: Hard
- **Asked By**: Meta (Top Hard question), Google, Amazon, Airbnb
- **Frequency**: ⭐⭐⭐⭐⭐

## 💡 Real-Life Analogy
Imagine searching through a long text message (`s = "ADOBECODEBANC"`) to find the shortest snippet that contains all the letters needed for an anagram recipe (`t = "ABC"`).
- You expand your window to the right until all ingredients A, B, and C are present.
- Once you have all ingredients, you shrink the window from the left to discard unnecessary fluff, recording the minimum valid window size!

## 📋 Problem Statement
Given two strings `s` and `t` of lengths `m` and `n` respectively, return the **minimum window substring** of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such substring, return the empty string `""`.

### Examples
- **Input**: `s = "ADOBECODEBANC"`, `t = "ABC"`
- **Output**: `"BANC"`
"""

sw_p2_sol_md = """# 💡 Minimum Window Substring - Solution Deep Dive

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
"""

sw_p2_sol_py = '''"""
Problem: Minimum Window Substring (LeetCode #76)
Sliding Window with Frequency Map & Have/Need Matching
Time Complexity: O(M + N)
Space Complexity: O(M + N)
"""

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        target_counts = Counter(t)
        window_counts = {}
        have, need = 0, len(target_counts)

        res, res_len = [-1, -1], float("inf")
        left = 0

        for right, char in enumerate(s):
            window_counts[char] = window_counts.get(char, 0) + 1

            if char in target_counts and window_counts[char] == target_counts[char]:
                have += 1

            # When window has all characters, shrink from left
            while have == need:
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                # Pop left character
                left_char = s[left]
                window_counts[left_char] -= 1
                if left_char in target_counts and window_counts[left_char] < target_counts[left_char]:
                    have -= 1
                left += 1

        l, r = res
        return s[l:r + 1] if res_len != float("inf") else ""

if __name__ == "__main__":
    sol = Solution()
    assert sol.minWindow("ADOBECODEBANC", "ABC") == "BANC"
    assert sol.minWindow("a", "a") == "a"
    assert sol.minWindow("a", "aa") == ""
    print("✅ All Minimum Window Substring tests passed!")
'''

print("Writing Sliding Window files...")
create_file("Sliding Window/README.md", sliding_window_readme)
create_file("Sliding Window/01_Longest_Substring_Without_Repeating_Characters/problem.md", sw_p1_prob)
create_file("Sliding Window/01_Longest_Substring_Without_Repeating_Characters/solution.md", sw_p1_sol_md)
create_file("Sliding Window/01_Longest_Substring_Without_Repeating_Characters/solution.py", sw_p1_sol_py)

create_file("Sliding Window/02_Minimum_Window_Substring/problem.md", sw_p2_prob)
create_file("Sliding Window/02_Minimum_Window_Substring/solution.md", sw_p2_sol_md)
create_file("Sliding Window/02_Minimum_Window_Substring/solution.py", sw_p2_sol_py)

# =====================================================================
# 3. STRING
# =====================================================================

string_readme = """# 🔤 Topic: String (Python DSA from Scratch)

## 🌟 1. Real-Life Analogy: What is a String?
A string is an immutable sequence of characters (letters, numbers, symbols) like text on a printed page. In Python, strings cannot be modified in place: modifying `s[0] = 'a'` creates an entirely new string!

## 🤖 2. Why AI Engineers Care
- **Tokenization & Prompt Engineering**: NLP begins with string parsing, unicode normalization, and regex splitting.
- **Text Embeddings & Generation**: LLMs take strings in, convert to token integer arrays, and decode output back to strings.

## 📚 Problems in this Directory
1. `01_Valid_Anagram` (Easy - Meta, Amazon)
2. `02_Group_Anagrams` (Medium - Meta, Google, Amazon)
3. `03_Longest_Palindromic_Substring` (Medium - Google, Amazon, Microsoft)
"""

str_p1_prob = """# 📖 Valid Anagram (LeetCode #242)

- **Difficulty**: Easy
- **Asked By**: Meta, Amazon, Google, Bloomberg
- **Frequency**: ⭐⭐⭐⭐⭐

## 💡 Real-Life Analogy
An anagram is rearranging the letters of a word to produce another word using all original letters exactly once:
e.g. `"anagram"` and `"nagaram"`.
If you count every letter in both words, the frequency counts must match identically!

## 📋 Problem Statement
Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

### Examples
- **Input**: `s = "anagram"`, `t = "nagaram"` -> `true`
- **Input**: `s = "rat"`, `t = "car"` -> `false`
"""

str_p1_sol_md = """# 💡 Valid Anagram - Solution Deep Dive

## 🧠 Thought Process
1. If `len(s) != len(t)`, they cannot be anagrams $\\rightarrow$ return `False`.
2. Count letter occurrences using a hash map or array of size 26 (for lowercase English).
3. If counts match, return `True`.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N)$ where $N = len(s)$.
- **Space Complexity**: $O(1)$ because the alphabet size is bounded by 26 characters.
"""

str_p1_sol_py = '''"""
Problem: Valid Anagram (LeetCode #242)
Frequency Counting with Hash Map
Time Complexity: O(N)
Space Complexity: O(1)
"""

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)

if __name__ == "__main__":
    sol = Solution()
    assert sol.isAnagram("anagram", "nagaram") is True
    assert sol.isAnagram("rat", "car") is False
    print("✅ All Valid Anagram tests passed!")
'''

str_p2_prob = """# 📖 Group Anagrams (LeetCode #49)

- **Difficulty**: Medium
- **Asked By**: Meta, Google, Amazon, Apple
- **Frequency**: ⭐⭐⭐⭐⭐

## 💡 Real-Life Analogy
Sorting words into buckets by their "letter recipe":
Words `"eat"`, `"tea"`, `"ate"` all have 1 'a', 1 'e', 1 't'.
If we sort their letters alphabetically, they all equal `"aet"`. We can use `"aet"` as the dictionary key and store all matching words in that bucket!

## 📋 Problem Statement
Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

### Examples
- **Input**: `strs = ["eat","tea","tan","ate","nat","bat"]`
- **Output**: `[["bat"],["nat","tan"],["ate","eat","tea"]]`
"""

str_p2_sol_md = """# 💡 Group Anagrams - Solution Deep Dive

## 🧠 Thought Process
- Initialize `buckets = collections.defaultdict(list)`
- For each word:
  - Canonical Key: `tuple(sorted(word))` or character count tuple of length 26.
  - Append word to `buckets[key]`.
- Return `list(buckets.values())`.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N \\cdot K \\log K)$ where $N$ is number of strings, $K$ is max length of string.
- **Space Complexity**: $O(N \\cdot K)$ to store grouped words.
"""

str_p2_sol_py = '''"""
Problem: Group Anagrams (LeetCode #49)
Categorize by Sorted String Key
Time Complexity: O(N * K log K)
Space Complexity: O(N * K)
"""

from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for word in strs:
            # Canonical key is sorted characters of the word
            sorted_key = "".join(sorted(word))
            anagram_map[sorted_key].append(word)

        return list(anagram_map.values())

if __name__ == "__main__":
    sol = Solution()
    res = sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    # Sort results for deterministic assertion
    sorted_res = sorted([sorted(group) for group in res])
    expected = sorted([["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])
    assert sorted_res == expected
    print("✅ All Group Anagrams tests passed!")
'''

str_p3_prob = """# 📖 Longest Palindromic Substring (LeetCode #5)

- **Difficulty**: Medium
- **Asked By**: Google, Amazon, Microsoft, Meta
- **Frequency**: ⭐⭐⭐⭐⭐

## 💡 Real-Life Analogy
Finding the longest symmetric phrase in a text.
Instead of checking all pairs, expand outward from the center of every character like ripples in water!

## 📋 Problem Statement
Given a string `s`, return the **longest palindromic substring** in `s`.

### Examples
- **Input**: `s = "babad"` -> `Output: "bab"` (or `"aba"`)
- **Input**: `s = "cbbd"` -> `Output: "bb"`
"""

str_p3_sol_md = """# 💡 Longest Palindromic Substring - Solution Deep Dive

## 🧠 Thought Process
Every palindrome has a center:
1. **Odd length** (e.g. `"racecar"`): center is `'e'`.
2. **Even length** (e.g. `"noon"`): center is between the two `'o'`s.
For each index `i`, expand outward to find longest odd and even palindromes!

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N^2)$ — $2N$ centers, each expands at most $O(N)$.
- **Space Complexity**: $O(1)$ auxiliary space.
"""

str_p3_sol_py = '''"""
Problem: Longest Palindromic Substring (LeetCode #5)
Expand Around Center Approach
Time Complexity: O(N^2)
Space Complexity: O(1)
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start, end = 0, 0

        def expand_around_center(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Length is (right - 1) - (left + 1) + 1 = right - left - 1
            return right - left - 1

        for i in range(len(s)):
            len_odd = expand_around_center(i, i)
            len_even = expand_around_center(i, i + 1)
            max_len = max(len_odd, len_even)

            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end + 1]

if __name__ == "__main__":
    sol = Solution()
    assert sol.longestPalindrome("babad") in ["bab", "aba"]
    assert sol.longestPalindrome("cbbd") == "bb"
    assert sol.longestPalindrome("a") == "a"
    print("✅ All Longest Palindromic Substring tests passed!")
'''

print("Writing String files...")
create_file("String/README.md", string_readme)
create_file("String/01_Valid_Anagram/problem.md", str_p1_prob)
create_file("String/01_Valid_Anagram/solution.md", str_p1_sol_md)
create_file("String/01_Valid_Anagram/solution.py", str_p1_sol_py)

create_file("String/02_Group_Anagrams/problem.md", str_p2_prob)
create_file("String/02_Group_Anagrams/solution.md", str_p2_sol_md)
create_file("String/02_Group_Anagrams/solution.py", str_p2_sol_py)

create_file("String/03_Longest_Palindromic_Substring/problem.md", str_p3_prob)
create_file("String/03_Longest_Palindromic_Substring/solution.md", str_p3_sol_md)
create_file("String/03_Longest_Palindromic_Substring/solution.py", str_p3_sol_py)

# =====================================================================
# 4. HASH TABLE & HASH FUNCTION
# =====================================================================

hash_table_readme = """# 🗄️ Topic: Hash Table & Hash Function (Python DSA from Scratch)

## 🌟 1. Real-Life Analogy: What is a Hash Table?
Think of a **library catalog** or an **addressed coat check**:
You hand over your coat (the Key), the worker hashes your ticket number to a specific hook (Bucket), and when you return, they fetch your coat in **$O(1)$ constant time**!

## 🤖 2. Why AI Engineers Care
- **Embedding Tables (`torch.nn.Embedding`)**: Lookups of word/token IDs to vector representations are backed by hash tables.
- **Feature Stores & Vector DB IDs**: Key-value fast lookups for prompt caching and user context retrieval.

## 📚 Problems in this Directory
1. `01_Ransom_Note` (Easy - Amazon, Google)
2. `02_Design_HashMap` (Easy/Medium - Google, Meta, Microsoft)
"""

ht_p1_prob = """# 📖 Ransom Note (LeetCode #383)

- **Difficulty**: Easy
- **Asked By**: Amazon, Google, Apple
- **Frequency**: ⭐⭐⭐⭐

## 💡 Real-Life Analogy
Constructing a ransom letter from magazine clippings:
Can you form the word `"cat"` if your magazine has `"a"`, `"b"`, `"c"`, `"t"`?
Yes, because the magazine has at least as many of each letter as your note requires.

## 📋 Problem Statement
Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed by using the letters from `magazine` and `false` otherwise.

Each letter in `magazine` can only be used once in `ransomNote`.
"""

ht_p1_sol_md = """# 💡 Ransom Note - Solution Deep Dive

## 🧠 Thought Process
Count letters in `magazine` with a hash map.
For each char in `ransomNote`:
- If count in magazine is 0, return `False`.
- Otherwise decrement count.
Return `True` if all letters satisfied.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(M + N)$
- **Space Complexity**: $O(1)$ (at most 26 lowercase English letters).
"""

ht_p1_sol_py = '''"""
Problem: Ransom Note (LeetCode #383)
Hash Map Frequency Matching
Time Complexity: O(M + N)
Space Complexity: O(1)
"""

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_counts = Counter(magazine)

        for char in ransomNote:
            if mag_counts[char] <= 0:
                return False
            mag_counts[char] -= 1

        return True

if __name__ == "__main__":
    sol = Solution()
    assert sol.canConstruct("a", "b") is False
    assert sol.canConstruct("aa", "ab") is False
    assert sol.canConstruct("aa", "aab") is True
    print("✅ All Ransom Note tests passed!")
'''

ht_p2_prob = """# 📖 Design HashMap (LeetCode #706)

- **Difficulty**: Easy / Medium
- **Asked By**: Google, Meta, Microsoft, Amazon
- **Frequency**: ⭐⭐⭐⭐⭐

## 💡 Real-Life Analogy
Building your own dictionary from scratch using an array of buckets and separate chaining for collisions!

## 📋 Problem Statement
Design a HashMap without using any built-in hash table libraries:
- `put(key, value)`: Insert key-value pair.
- `get(key)`: Return value associated with key, or -1 if not found.
- `remove(key)`: Remove mapping for key.
"""

ht_p2_sol_md = """# 💡 Design HashMap - Solution Deep Dive

## 🧠 Architecture
- **Modulo Hash Function**: `hash_idx = key % BUCKET_SIZE` (prime number like 1009 to distribute evenly).
- **Collision Resolution**: Separate chaining using a list of `[key, value]` pairs at each bucket.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(1)$ average for put, get, remove.
- **Space Complexity**: $O(K)$ where $K$ is number of unique keys.
"""

ht_p2_sol_py = '''"""
Problem: Design HashMap (LeetCode #706)
Bucket Array with Chaining
Time Complexity: O(1) average per operation
Space Complexity: O(N)
"""

class MyHashMap:
    def __init__(self):
        self.size = 1009  # Prime number for uniform distribution
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        idx = self._hash(key)
        bucket = self.buckets[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key: int) -> int:
        idx = self._hash(key)
        bucket = self.buckets[idx]
        for k, v in bucket:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        bucket = self.buckets[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return

if __name__ == "__main__":
    h = MyHashMap()
    h.put(1, 1)
    h.put(2, 2)
    assert h.get(1) == 1
    assert h.get(3) == -1
    h.put(2, 1)
    assert h.get(2) == 1
    h.remove(2)
    assert h.get(2) == -1
    print("✅ All Design HashMap tests passed!")
'''

print("Writing Hash Table & Hash Function files...")
create_file("Hash Table/README.md", hash_table_readme)
create_file("Hash Table/01_Ransom_Note/problem.md", ht_p1_prob)
create_file("Hash Table/01_Ransom_Note/solution.md", ht_p1_sol_md)
create_file("Hash Table/01_Ransom_Note/solution.py", ht_p1_sol_py)

create_file("Hash Table/02_Design_HashMap/problem.md", ht_p2_prob)
create_file("Hash Table/02_Design_HashMap/solution.md", ht_p2_sol_md)
create_file("Hash Table/02_Design_HashMap/solution.py", ht_p2_sol_py)

create_file("Hash Function/README.md", hash_table_readme)
create_file("Hash Function/01_Design_HashMap/problem.md", ht_p2_prob)
create_file("Hash Function/01_Design_HashMap/solution.md", ht_p2_sol_md)
create_file("Hash Function/01_Design_HashMap/solution.py", ht_p2_sol_py)

# =====================================================================
# 5. PREFIX SUM
# =====================================================================

prefix_sum_readme = """# ➕ Topic: Prefix Sum (Python DSA from Scratch)

## 🌟 1. Real-Life Analogy: What is a Prefix Sum?
Imagine keeping a **running odometer** in your car:
- At milepost 1: odometer reads 10 miles.
- At milepost 5: odometer reads 80 miles.
How far did you drive between milepost 1 and 5?
$$\\text{Distance} = 80 - 10 = 70 \\text{ miles}$$
In $O(1)$ constant time, without counting mile markers one by one!

## 🤖 2. Why AI Engineers Care
- **Integral Images in Computer Vision**: Fast box filtering and bounding box pooling in Viola-Jones and object detection.
- **Cumulative Probability Distributions**: Sampling from discrete probability distributions via cumulative sum + binary search.

## 📚 Problems in this Directory
1. `01_Range_Sum_Query_Immutable` (Easy - Meta, Amazon)
2. `02_Subarray_Sum_Equals_K` (Medium - Meta #1 asked, Google)
"""

ps_p1_prob = """# 📖 Range Sum Query - Immutable (LeetCode #303)

- **Difficulty**: Easy
- **Asked By**: Meta, Amazon, Google
- **Frequency**: ⭐⭐⭐⭐

## 📋 Problem Statement
Given an integer array `nums`, handle multiple queries of the following type:
Calculate the sum of the elements of `nums` between indices `left` and `right` inclusive where `left <= right`.
Query operation must run in **$O(1)$ time**.
"""

ps_p1_sol_md = """# 💡 Range Sum Query - Solution Deep Dive

## 🧠 Thought Process
Precompute `prefix[i] = sum(nums[0...i-1])`.
Then `sumRange(left, right) = prefix[right + 1] - prefix[left]`.

## ⏱️ Complexity Analysis
- **Precomputation**: $O(N)$
- **Query Time**: $O(1)$
- **Space Complexity**: $O(N)$
"""

ps_p1_sol_py = '''"""
Problem: Range Sum Query - Immutable (LeetCode #303)
Prefix Sum Precomputation
Precomputation: O(N), Query: O(1)
"""

from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix = [0] * (len(nums) + 1)
        for i, val in enumerate(nums):
            self.prefix[i + 1] = self.prefix[i] + val

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]

if __name__ == "__main__":
    na = NumArray([-2, 0, 3, -5, 2, -1])
    assert na.sumRange(0, 2) == 1
    assert na.sumRange(2, 5) == -1
    assert na.sumRange(0, 5) == -3
    print("✅ All Range Sum Query tests passed!")
'''

ps_p2_prob = """# 📖 Subarray Sum Equals K (LeetCode #560)

- **Difficulty**: Medium
- **Asked By**: Meta (Top 3 most asked across all tech), Google, Amazon
- **Frequency**: ⭐⭐⭐⭐⭐

## 💡 Real-Life Analogy
You are looking for stretches of transactions that total \$K.
Using running balance: if your current balance is \$100, and $K = \\$30$, have you ever previously had a balance of $\\$100 - \\$30 = \\$70$?
Every time you had \$70 in the past represents a subarray summing to \$30!

## 📋 Problem Statement
Given an array of integers `nums` and an integer `k`, return the **total number of subarrays** whose sum equals to `k`.

### Examples
- **Input**: `nums = [1, 1, 1]`, `k = 2` -> `Output: 2`
- **Input**: `nums = [1, 2, 3]`, `k = 3` -> `Output: 2`
"""

ps_p2_sol_md = """# 💡 Subarray Sum Equals K - Solution Deep Dive

## 🧠 Thought Process
Running prefix sum:
$$\\text{prefix}[j] - \\text{prefix}[i] = k \\implies \\text{prefix}[i] = \\text{prefix}[j] - k$$
We maintain a hash map `prefix_counts` recording how many times each prefix sum has occurred.
Initialize `prefix_counts = {0: 1}` (empty subarray has sum 0).

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N)$ — Single pass over array.
- **Space Complexity**: $O(N)$ for prefix count map.
"""

ps_p2_sol_py = '''"""
Problem: Subarray Sum Equals K (LeetCode #560)
Prefix Sum + Hash Map Frequency Counting
Time Complexity: O(N)
Space Complexity: O(N)
"""

from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        prefix_counts = {0: 1}  # Base case: sum of 0 occurs once initially

        for num in nums:
            current_sum += num

            # If (current_sum - k) was seen before, add its frequency
            if current_sum - k in prefix_counts:
                count += prefix_counts[current_sum - k]

            # Record frequency of current prefix sum
            prefix_counts[current_sum] = prefix_counts.get(current_sum, 0) + 1

        return count

if __name__ == "__main__":
    sol = Solution()
    assert sol.subarraySum([1, 1, 1], 2) == 2
    assert sol.subarraySum([1, 2, 3], 3) == 2
    assert sol.subarraySum([1, -1, 0], 0) == 3
    print("✅ All Subarray Sum Equals K tests passed!")
'''

print("Writing Prefix Sum files...")
create_file("Prefix Sum/README.md", prefix_sum_readme)
create_file("Prefix Sum/01_Range_Sum_Query_Immutable/problem.md", ps_p1_prob)
create_file("Prefix Sum/01_Range_Sum_Query_Immutable/solution.md", ps_p1_sol_md)
create_file("Prefix Sum/01_Range_Sum_Query_Immutable/solution.py", ps_p1_sol_py)

create_file("Prefix Sum/02_Subarray_Sum_Equals_K/problem.md", ps_p2_prob)
create_file("Prefix Sum/02_Subarray_Sum_Equals_K/solution.md", ps_p2_sol_md)
create_file("Prefix Sum/02_Subarray_Sum_Equals_K/solution.py", ps_p2_sol_py)

print("Batch 1 generated successfully!")
