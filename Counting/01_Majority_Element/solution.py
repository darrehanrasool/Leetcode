"""
Problem: Majority Element (LeetCode #169)
Boyer-Moore Voting Algorithm
Time Complexity: O(N)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate

if __name__ == "__main__":
    sol = Solution()
    assert sol.majorityElement([3, 2, 3]) == 3
    assert sol.majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2
    print("✅ All Majority Element tests passed!")
