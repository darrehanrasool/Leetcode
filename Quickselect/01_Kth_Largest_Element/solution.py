"""
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
