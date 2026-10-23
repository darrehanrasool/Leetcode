"""
Problem: 3Sum (LeetCode #15)
Sorting + Two Pointers
Time Complexity: O(N^2)
Space Complexity: O(1) auxiliary
"""

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n - 2):
            # If current element is positive, sum of three positive numbers cannot be zero
            if nums[i] > 0:
                break

            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])

                    # Skip duplicate values for the second element
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicate values for the third element
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return res

if __name__ == "__main__":
    sol = Solution()
    assert sol.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert sol.threeSum([0, 1, 1]) == []
    assert sol.threeSum([0, 0, 0]) == [[0, 0, 0]]
    print("✅ All 3Sum tests passed!")
