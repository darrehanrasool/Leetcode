"""
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
