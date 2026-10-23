"""
Problem: Find Minimum in Rotated Sorted Array (LeetCode #153)
Binary Search for Pivot Inflection
Time Complexity: O(log N)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1

        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid

        return nums[low]

if __name__ == "__main__":
    sol = Solution()
    assert sol.findMin([3, 4, 5, 1, 2]) == 1
    assert sol.findMin([4, 5, 6, 7, 0, 1, 2]) == 0
    assert sol.findMin([11, 13, 15, 17]) == 11
    print("✅ All Find Minimum in Rotated Sorted Array tests passed!")
