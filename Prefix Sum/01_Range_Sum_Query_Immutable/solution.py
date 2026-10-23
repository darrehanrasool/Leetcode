"""
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
