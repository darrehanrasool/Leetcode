"""
Problem: Two Sum II - Input Array Is Sorted (LeetCode #167)
Two Pointers Inward Convergence
Time Complexity: O(N)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                # 1-indexed response required by problem
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1  # Need a larger sum
            else:
                right -= 1  # Need a smaller sum

        return []

if __name__ == "__main__":
    sol = Solution()
    assert sol.twoSum([2, 7, 11, 15], 9) == [1, 2]
    assert sol.twoSum([2, 3, 4], 6) == [1, 3]
    assert sol.twoSum([-1, 0], -1) == [1, 2]
    print("✅ All Two Sum II tests passed!")
