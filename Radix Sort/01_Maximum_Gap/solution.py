"""
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
