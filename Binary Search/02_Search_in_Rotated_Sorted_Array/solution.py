"""
Problem: Search in Rotated Sorted Array (LeetCode #33)
Modified Binary Search
Time Complexity: O(log N)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return mid

            # Check if left half is normally sorted
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            # Otherwise, right half must be normally sorted
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1

if __name__ == "__main__":
    sol = Solution()
    assert sol.search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert sol.search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert sol.search([1], 0) == -1
    print("✅ All Search in Rotated Sorted Array tests passed!")
