"""
Problem: Binary Search (LeetCode #704)
Classic Iterative Binary Search
Time Complexity: O(log N)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1

if __name__ == "__main__":
    sol = Solution()
    assert sol.search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert sol.search([-1, 0, 3, 5, 9, 12], 2) == -1
    print("✅ All Binary Search tests passed!")
