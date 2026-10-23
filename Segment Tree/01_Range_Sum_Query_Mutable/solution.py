"""
Problem: Range Sum Query - Mutable (LeetCode #307)
Binary Indexed Tree (Fenwick Tree)
Update: O(log N), Query: O(log N)
"""

from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = [0] * self.n
        self.tree = [0] * (self.n + 1)
        for i, val in enumerate(nums):
            self.update(i, val)

    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        self.nums[index] = val
        i = index + 1
        while i <= self.n:
            self.tree[i] += diff
            i += (i & -i)  # Add lowest set bit

    def _query(self, i: int) -> int:
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= (i & -i)  # Clear lowest set bit
        return total

    def sumRange(self, left: int, right: int) -> int:
        return self._query(right + 1) - self._query(left)

if __name__ == "__main__":
    na = NumArray([1, 3, 5])
    assert na.sumRange(0, 2) == 9
    na.update(1, 2)
    assert na.sumRange(0, 2) == 8
    print("✅ All Fenwick / Segment Tree tests passed!")
