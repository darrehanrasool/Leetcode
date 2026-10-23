"""
Problem: Random Pick Index (LeetCode #398)
Reservoir Sampling Algorithm
Time Complexity: O(N) per pick
Space Complexity: O(1) extra space
"""

import random
from typing import List

class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        chosen_idx = -1
        count = 0

        for i, val in enumerate(self.nums):
            if val == target:
                count += 1
                # Probability of picking i-th match is 1/count
                if random.randint(1, count) == 1:
                    chosen_idx = i

        return chosen_idx

if __name__ == "__main__":
    sol = Solution([1, 2, 3, 3, 3])
    picks = [sol.pick(3) for _ in range(300)]
    assert 2 in picks and 3 in picks and 4 in picks
    print("✅ All Reservoir Sampling tests passed!")
