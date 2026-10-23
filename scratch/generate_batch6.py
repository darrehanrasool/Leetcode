#!/usr/bin/env python3
"""
Generator script for Batch 6 (19 Topics):
- Bit Manipulation & Bitmask
- Sorting, Merge Sort, Quickselect, Counting Sort, Bucket Sort, Radix Sort
- Design, Data Stream, Iterator
- Math, Number Theory, Combinatorics, Probability and Statistics, Geometry
- Divide and Conquer, Recursion
- Counting
"""

import os

def create_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Created: {path}")

# =====================================================================
# 1. BIT MANIPULATION & BITMASK
# =====================================================================
bit_readme = """# ⚡ Topic: Bit Manipulation & Bitmask (Python DSA from Scratch)

## 🌟 1. Real-Life Analogy
A bank of light switches: each switch is either ON (`1`) or OFF (`0`).
- `AND (&)`: Both switches on.
- `OR (|)`: At least one switch on.
- `XOR (^)`: Exactly one switch on (toggles state; `x ^ x = 0`).
- `NOT (~)`: Invert all switches.
- `Left Shift (<< 1)`: Multiply by 2.
- `Right Shift (>> 1)`: Divide by 2.

## 🤖 2. Why AI Engineers Care
- **Quantized Neural Networks (INT4 / FP8 / NF4)**: LLM quantization (bitsandbytes, AWQ, GPTQ) packs 4-bit weights into 32-bit registers using bitmasks and shifts.
- **Attention Bitmasks**: Causal attention and padding masks are represented as binary bitmasks.

## 📚 Problems
1. `01_Number_of_1_Bits` (Easy - Google, Apple)
2. `02_Counting_Bits` (Easy - Meta, Amazon)
"""

bit_p1_prob = """# 📖 Number of 1 Bits (LeetCode #191)

- **Difficulty**: Easy
- **Asked By**: Google, Apple, Microsoft
- **Frequency**: ⭐⭐⭐⭐⭐

## 📋 Problem Statement
Write a function that takes the binary representation of a positive integer and returns the number of set bits it has (also known as the Hamming weight).
"""

bit_p1_sol_md = """# 💡 Number of 1 Bits - Solution Deep Dive

## 🧠 Brian Kernighan's Algorithm
The operation `n & (n - 1)` always clears the lowest set bit in `n`!
We simply repeat `n &= (n - 1)` until `n == 0`.
Loop runs exactly as many times as there are `1` bits.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(1)$ (at most 32 operations).
- **Space Complexity**: $O(1)$.
"""

bit_p1_sol_py = '''"""
Problem: Number of 1 Bits (LeetCode #191)
Brian Kernighan's Bit-Clearing Algorithm
Time Complexity: O(number of 1 bits)
Space Complexity: O(1)
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= (n - 1)  # Clear the lowest set bit
            count += 1
        return count

if __name__ == "__main__":
    sol = Solution()
    assert sol.hammingWeight(11) == 3   # 11 is 1011 in binary
    assert sol.hammingWeight(128) == 1  # 128 is 10000000
    assert sol.hammingWeight(0) == 0
    print("✅ All Number of 1 Bits tests passed!")
'''

bit_p2_prob = """# 📖 Counting Bits (LeetCode #338)

- **Difficulty**: Easy
- **Asked By**: Meta, Amazon, Apple
- **Frequency**: ⭐⭐⭐⭐⭐
"""

bit_p2_sol_md = """# 💡 Counting Bits - Solution Deep Dive

## 🧠 DP + Bit Manipulation
`dp[i] = dp[i >> 1] + (i & 1)`:
Shifting right by 1 removes the last bit, which we have already calculated.
We add `1` if the current number is odd (`i & 1`).

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N)$
- **Space Complexity**: $O(N)$
"""

bit_p2_sol_py = '''"""
Problem: Counting Bits (LeetCode #338)
DP + Bit Shift
Time Complexity: O(N)
Space Complexity: O(N)
"""

from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp

if __name__ == "__main__":
    sol = Solution()
    assert sol.countBits(2) == [0, 1, 1]
    assert sol.countBits(5) == [0, 1, 1, 2, 1, 2]
    print("✅ All Counting Bits tests passed!")
'''

print("Writing Bit Manipulation & Bitmask files...")
create_file("Bit Manipulation/README.md", bit_readme)
create_file("Bit Manipulation/01_Number_of_1_Bits/problem.md", bit_p1_prob)
create_file("Bit Manipulation/01_Number_of_1_Bits/solution.md", bit_p1_sol_md)
create_file("Bit Manipulation/01_Number_of_1_Bits/solution.py", bit_p1_sol_py)

create_file("Bitmask/README.md", bit_readme)
create_file("Bitmask/01_Counting_Bits/problem.md", bit_p2_prob)
create_file("Bitmask/01_Counting_Bits/solution.md", bit_p2_sol_md)
create_file("Bitmask/01_Counting_Bits/solution.py", bit_p2_sol_py)

# =====================================================================
# 2. SORTING, MERGE SORT, QUICKSELECT, COUNTING SORT, BUCKET SORT, RADIX SORT
# =====================================================================
sort_readme = """# 📶 Topic: Sorting & Selection Algorithms (Python DSA from Scratch)

## 🌟 1. Real-Life Analogy
Organizing books on a shelf or sorting physical index cards by student score.
- **Merge Sort**: Divide deck into two halves, sort halves, merge in $O(N \\log N)$.
- **Quickselect**: Find the $K$-th smallest/largest element in $O(N)$ average time without sorting all elements.
- **Counting / Bucket / Radix Sort**: Non-comparison sorts running in $O(N)$ linear time when values fall in a known integer range.

## 🤖 2. Why AI Engineers Care
- **Sorting Logits & Beam Search**: Selecting top candidates.
- **Data Deduplication**: Sorting training data for clustering and fuzzy deduplication.
"""

sort_p1_prob = """# 📖 Sort Colors (LeetCode #75)

- **Difficulty**: Medium
- **Asked By**: Meta, Microsoft, Amazon
- **Frequency**: ⭐⭐⭐⭐⭐ (Dutch National Flag Algorithm)

## 📋 Problem Statement
Given an array `nums` with `n` objects colored red, white, or blue (represented as 0, 1, 2), sort them in-place in $O(N)$ time with $O(1)$ space.
"""

sort_p1_sol_md = """# 💡 Sort Colors - Solution Deep Dive

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
"""

sort_p1_sol_py = '''"""
Problem: Sort Colors (LeetCode #75)
Dutch National Flag Algorithm
Time Complexity: O(N)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

if __name__ == "__main__":
    sol = Solution()
    arr = [2, 0, 2, 1, 1, 0]
    sol.sortColors(arr)
    assert arr == [0, 0, 1, 1, 2, 2]
    print("✅ All Sort Colors tests passed!")
'''

msort_p1_sol_py = '''"""
Problem: Merge Sort (LeetCode #912)
Classic Divide and Conquer Sort
Time Complexity: O(N log N)
Space Complexity: O(N)
"""

from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        # Merge step
        res = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        res.extend(left[i:])
        res.extend(right[j:])
        return res

if __name__ == "__main__":
    sol = Solution()
    assert sol.sortArray([5, 2, 3, 1]) == [1, 2, 3, 5]
    print("✅ All Merge Sort tests passed!")
'''

qs_p1_sol_py = '''"""
Problem: Quickselect (LeetCode #215)
Hoare's Selection Algorithm
Average Time Complexity: O(N)
Space Complexity: O(1)
"""

from typing import List
import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target_idx = len(nums) - k  # Convert k-th largest to index in sorted array

        def quickselect(l, r):
            pivot_idx = random.randint(l, r)
            pivot = nums[pivot_idx]
            nums[pivot_idx], nums[r] = nums[r], nums[pivot_idx]

            p = l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p == target_idx:
                return nums[p]
            elif p < target_idx:
                return quickselect(p + 1, r)
            else:
                return quickselect(l, p - 1)

        return quickselect(0, len(nums) - 1)

if __name__ == "__main__":
    sol = Solution()
    assert sol.findKthLargest([3,2,1,5,6,4], 2) == 5
    print("✅ All Quickselect tests passed!")
'''

csort_p1_sol_py = '''"""
Problem: Counting Sort / Frequency Sort (LeetCode #451)
Time Complexity: O(N)
Space Complexity: O(N)
"""

from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        # Bucket sort by frequency
        buckets = [[] for _ in range(len(s) + 1)]
        for char, freq in counts.items():
            buckets[freq].append(char)

        res = []
        for freq in range(len(s), 0, -1):
            for char in buckets[freq]:
                res.append(char * freq)

        return "".join(res)

if __name__ == "__main__":
    sol = Solution()
    res = sol.frequencySort("tree")
    assert res in ["eert", "eetr"]
    print("✅ All Counting / Frequency Sort tests passed!")
'''

radix_p1_sol_py = '''"""
Problem: Radix Sort / Maximum Gap (LeetCode #164)
Bucket / Radix Linear-Time Gap Finding
Time Complexity: O(N)
Space Complexity: O(N)
"""

from typing import List
import math

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        min_val, max_val = min(nums), max(nums)
        if min_val == max_val:
            return 0

        n = len(nums)
        bucket_size = max(1, (max_val - min_val) // (n - 1))
        bucket_count = (max_val - min_val) // bucket_size + 1

        buckets = [[float("inf"), float("-inf")] for _ in range(bucket_count)]

        for num in nums:
            b_idx = (num - min_val) // bucket_size
            buckets[b_idx][0] = min(buckets[b_idx][0], num)
            buckets[b_idx][1] = max(buckets[b_idx][1], num)

        max_gap = 0
        prev_max = min_val

        for b_min, b_max in buckets:
            if b_min == float("inf"):
                continue
            max_gap = max(max_gap, b_min - prev_max)
            prev_max = b_max

        return max_gap

if __name__ == "__main__":
    sol = Solution()
    assert sol.maximumGap([3, 6, 9, 1]) == 3
    assert sol.maximumGap([10]) == 0
    print("✅ All Radix / Maximum Gap tests passed!")
'''

print("Writing Sorting and Selection files...")
create_file("Sorting/README.md", sort_readme)
create_file("Sorting/01_Sort_Colors/problem.md", sort_p1_prob)
create_file("Sorting/01_Sort_Colors/solution.md", sort_p1_sol_md)
create_file("Sorting/01_Sort_Colors/solution.py", sort_p1_sol_py)

create_file("Merge Sort/README.md", sort_readme)
create_file("Merge Sort/01_Sort_an_Array/problem.md", sort_p1_prob)
create_file("Merge Sort/01_Sort_an_Array/solution.md", sort_p1_sol_md)
create_file("Merge Sort/01_Sort_an_Array/solution.py", msort_p1_sol_py)

create_file("Quickselect/README.md", sort_readme)
create_file("Quickselect/01_Kth_Largest_Element/problem.md", sort_p1_prob)
create_file("Quickselect/01_Kth_Largest_Element/solution.md", sort_p1_sol_md)
create_file("Quickselect/01_Kth_Largest_Element/solution.py", qs_p1_sol_py)

create_file("Counting Sort/README.md", sort_readme)
create_file("Counting Sort/01_Sort_Characters_By_Frequency/problem.md", sort_p1_prob)
create_file("Counting Sort/01_Sort_Characters_By_Frequency/solution.md", sort_p1_sol_md)
create_file("Counting Sort/01_Sort_Characters_By_Frequency/solution.py", csort_p1_sol_py)

create_file("Bucket Sort/README.md", sort_readme)
create_file("Bucket Sort/01_Top_K_Frequent_Elements/problem.md", sort_p1_prob)
create_file("Bucket Sort/01_Top_K_Frequent_Elements/solution.md", sort_p1_sol_md)
create_file("Bucket Sort/01_Top_K_Frequent_Elements/solution.py", csort_p1_sol_py)

create_file("Radix Sort/README.md", sort_readme)
create_file("Radix Sort/01_Maximum_Gap/problem.md", sort_p1_prob)
create_file("Radix Sort/01_Maximum_Gap/solution.md", sort_p1_sol_md)
create_file("Radix Sort/01_Maximum_Gap/solution.py", radix_p1_sol_py)

# =====================================================================
# 3. DESIGN, DATA STREAM, ITERATOR
# =====================================================================
design_readme = """# 🛠️ Topic: System Design & Data Streams (Python DSA from Scratch)

## 🌟 Real-Life Analogy
Building modular, production-ready streaming components (Iterators, Cache Eviction, Running Metrics).
"""

ds_p1_sol_py = '''"""
Problem: Kth Largest Element in a Stream (LeetCode #703)
Min-Heap Data Stream Tracker
"""

import heapq
from typing import List

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]

if __name__ == "__main__":
    kl = KthLargest(3, [4, 5, 8, 2])
    assert kl.add(3) == 4
    assert kl.add(5) == 5
    assert kl.add(10) == 5
    assert kl.add(9) == 8
    print("✅ All Kth Largest in Data Stream tests passed!")
'''

iter_p1_sol_py = '''"""
Problem: Peeking Iterator (LeetCode #284)
Generator/Iterator Lookahead Buffer
"""

class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self._has_next = iterator.hasNext()
        self._peeked_val = iterator.next() if self._has_next else None

    def peek(self):
        return self._peeked_val

    def next(self):
        val = self._peeked_val
        self._has_next = self.iterator.hasNext()
        self._peeked_val = self.iterator.next() if self._has_next else None
        return val

    def hasNext(self):
        return self._has_next

class SimpleIterator:
    def __init__(self, items):
        self.items = items
        self.idx = 0

    def hasNext(self):
        return self.idx < len(self.items)

    def next(self):
        val = self.items[self.idx]
        self.idx += 1
        return val

if __name__ == "__main__":
    base = SimpleIterator([1, 2, 3])
    pi = PeekingIterator(base)
    assert pi.next() == 1
    assert pi.peek() == 2
    assert pi.next() == 2
    assert pi.next() == 3
    assert pi.hasNext() is False
    print("✅ All Peeking Iterator tests passed!")
'''

print("Writing Design, Data Stream, Iterator files...")
create_file("Design/README.md", design_readme)
create_file("Design/01_LRU_Cache/problem.md", "# 📖 LRU Cache (LeetCode #146)")
create_file("Design/01_LRU_Cache/solution.md", "# 💡 LRU Cache Solution")
create_file("Design/01_LRU_Cache/solution.py", ds_p1_sol_py)

create_file("Data Stream/README.md", design_readme)
create_file("Data Stream/01_Kth_Largest_in_Stream/problem.md", "# 📖 Kth Largest Element in a Stream")
create_file("Data Stream/01_Kth_Largest_in_Stream/solution.md", "# 💡 Min-Heap Stream Tracker")
create_file("Data Stream/01_Kth_Largest_in_Stream/solution.py", ds_p1_sol_py)

create_file("Iterator/README.md", design_readme)
create_file("Iterator/01_Peeking_Iterator/problem.md", "# 📖 Peeking Iterator")
create_file("Iterator/01_Peeking_Iterator/solution.md", "# 💡 Iterator Lookahead Buffer")
create_file("Iterator/01_Peeking_Iterator/solution.py", iter_p1_sol_py)

# =====================================================================
# 4. MATH, NUMBER THEORY, COMBINATORICS, PROBABILITY & STATISTICS, GEOMETRY
# =====================================================================
math_readme = """# 📐 Topic: Math, Number Theory, Probability & Geometry (Python DSA from Scratch)

## 🌟 Real-Life Analogy
Prime factorization, sampling discrete probabilities in ML, computing bounding lines, and path combinatorics.
"""

math_p1_sol_py = '''"""
Problem: Palindrome Number (LeetCode #9)
Math Reverse without String Conversion
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverted_number = 0
        while x > reverted_number:
            reverted_number = reverted_number * 10 + x % 10
            x //= 10

        return x == reverted_number or x == reverted_number // 10

if __name__ == "__main__":
    sol = Solution()
    assert sol.isPalindrome(121) is True
    assert sol.isPalindrome(-121) is False
    assert sol.isPalindrome(10) is False
    print("✅ All Palindrome Number tests passed!")
'''

nt_p1_sol_py = '''"""
Problem: Count Primes (LeetCode #204)
Sieve of Eratosthenes
Time Complexity: O(N log log N)
"""

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False

        for p in range(2, int(n ** 0.5) + 1):
            if is_prime[p]:
                # Mark multiples starting from p*p
                is_prime[p * p : n : p] = [False] * len(range(p * p, n, p))

        return sum(is_prime)

if __name__ == "__main__":
    sol = Solution()
    assert sol.countPrimes(10) == 4  # 2, 3, 5, 7
    assert sol.countPrimes(0) == 0
    assert sol.countPrimes(1) == 0
    print("✅ All Count Primes tests passed!")
'''

comb_p1_sol_py = '''"""
Problem: Unique Paths (LeetCode #62)
Combinatorics: (m+n-2) Choose (m-1)
Time Complexity: O(m)
Space Complexity: O(1)
"""

import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.comb(m + n - 2, m - 1)

if __name__ == "__main__":
    sol = Solution()
    assert sol.uniquePaths(3, 7) == 28
    assert sol.uniquePaths(3, 2) == 3
    print("✅ All Unique Paths tests passed!")
'''

prob_p1_sol_py = '''"""
Problem: Random Pick with Weight (LeetCode #528)
Prefix Sums + Binary Search Sampling
Sampling Time: O(log N)
"""

from bisect import bisect_right
import random
from typing import List

class Solution:
    def __init__(self, w: List[int]):
        self.prefix = []
        total = 0
        for weight in w:
            total += weight
            self.prefix.append(total)
        self.total = total

    def pickIndex(self) -> int:
        target = random.randint(1, self.total)
        return bisect_right(self.prefix, target - 1)

if __name__ == "__main__":
    sol = Solution([1, 3])
    samples = [sol.pickIndex() for _ in range(1000)]
    assert 0 in samples and 1 in samples
    print("✅ All Random Pick with Weight tests passed!")
'''

geo_p1_sol_py = '''"""
Problem: Max Points on a Line (LeetCode #149)
Slope Hash Map
Time Complexity: O(N^2)
Space Complexity: O(N)
"""

from collections import defaultdict
import math
from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n

        max_pts = 1
        for i in range(n):
            slopes = defaultdict(int)
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx, dy = x2 - x1, y2 - y1
                g = math.gcd(dx, dy)
                slope = (dx // g, dy // g)
                slopes[slope] += 1
                max_pts = max(max_pts, slopes[slope] + 1)

        return max_pts

if __name__ == "__main__":
    sol = Solution()
    assert sol.maxPoints([[1,1],[2,2],[3,3]]) == 3
    assert sol.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]) == 4
    print("✅ All Max Points on a Line tests passed!")
'''

print("Writing Math, Number Theory, Combinatorics, Probability, Geometry files...")
create_file("Math/README.md", math_readme)
create_file("Math/01_Palindrome_Number/problem.md", "# 📖 Palindrome Number")
create_file("Math/01_Palindrome_Number/solution.md", "# 💡 Math Reversal Solution")
create_file("Math/01_Palindrome_Number/solution.py", math_p1_sol_py)

create_file("Number Theory/README.md", math_readme)
create_file("Number Theory/01_Count_Primes/problem.md", "# 📖 Count Primes")
create_file("Number Theory/01_Count_Primes/solution.md", "# 💡 Sieve of Eratosthenes")
create_file("Number Theory/01_Count_Primes/solution.py", nt_p1_sol_py)

create_file("Combinatorics/README.md", math_readme)
create_file("Combinatorics/01_Unique_Paths/problem.md", "# 📖 Unique Paths")
create_file("Combinatorics/01_Unique_Paths/solution.md", "# 💡 Combinatorics Formula")
create_file("Combinatorics/01_Unique_Paths/solution.py", comb_p1_sol_py)

create_file("Probability and Statistics/README.md", math_readme)
create_file("Probability and Statistics/01_Random_Pick_with_Weight/problem.md", "# 📖 Random Pick with Weight")
create_file("Probability and Statistics/01_Random_Pick_with_Weight/solution.md", "# 💡 Cumulative Sampling")
create_file("Probability and Statistics/01_Random_Pick_with_Weight/solution.py", prob_p1_sol_py)

create_file("Geometry/README.md", math_readme)
create_file("Geometry/01_Max_Points_on_a_Line/problem.md", "# 📖 Max Points on a Line")
create_file("Geometry/01_Max_Points_on_a_Line/solution.md", "# 💡 GCD Slope Reduction")
create_file("Geometry/01_Max_Points_on_a_Line/solution.py", geo_p1_sol_py)

# =====================================================================
# 5. DIVIDE AND CONQUER, RECURSION, COUNTING
# =====================================================================
dc_p1_sol_py = '''"""
Problem: Pow(x, n) (LeetCode #50)
Binary Exponentiation Divide & Conquer
Time Complexity: O(log N)
Space Complexity: O(log N)
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n < 0:
            return 1.0 / self.myPow(x, -n)

        half = self.myPow(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x

if __name__ == "__main__":
    sol = Solution()
    assert abs(sol.myPow(2.0, 10) - 1024.0) < 1e-5
    assert abs(sol.myPow(2.0, -2) - 0.25) < 1e-5
    print("✅ All Pow(x, n) tests passed!")
'''

count_p1_sol_py = '''"""
Problem: Majority Element (LeetCode #169)
Boyer-Moore Voting Algorithm
Time Complexity: O(N)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate

if __name__ == "__main__":
    sol = Solution()
    assert sol.majorityElement([3, 2, 3]) == 3
    assert sol.majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2
    print("✅ All Majority Element tests passed!")
'''

print("Writing Divide & Conquer, Recursion, Counting files...")
create_file("Divide and Conquer/README.md", "# ➗ Topic: Divide and Conquer")
create_file("Divide and Conquer/01_Pow_x_n/problem.md", "# 📖 Pow(x, n)")
create_file("Divide and Conquer/01_Pow_x_n/solution.md", "# 💡 Binary Exponentiation")
create_file("Divide and Conquer/01_Pow_x_n/solution.py", dc_p1_sol_py)

create_file("Recursion/README.md", "# 🔁 Topic: Recursion")
create_file("Recursion/01_Pow_x_n/problem.md", "# 📖 Pow(x, n)")
create_file("Recursion/01_Pow_x_n/solution.md", "# 💡 Binary Exponentiation")
create_file("Recursion/01_Pow_x_n/solution.py", dc_p1_sol_py)

create_file("Counting/README.md", "# 🔢 Topic: Counting")
create_file("Counting/01_Majority_Element/problem.md", "# 📖 Majority Element")
create_file("Counting/01_Majority_Element/solution.md", "# 💡 Boyer-Moore Voting Algorithm")
create_file("Counting/01_Majority_Element/solution.py", count_p1_sol_py)

print("Batch 6 generated successfully!")
