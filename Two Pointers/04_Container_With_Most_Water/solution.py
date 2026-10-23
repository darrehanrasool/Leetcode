"""
Problem: Container With Most Water (LeetCode #11)
Two Pointers Greedy Squeeze
Time Complexity: O(N)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            width = right - left
            h = min(height[left], height[right])
            current_water = width * h
            max_water = max(max_water, current_water)

            # Greedily move the shorter boundary inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water

if __name__ == "__main__":
    sol = Solution()
    assert sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert sol.maxArea([1, 1]) == 1
    print("✅ All Container With Most Water tests passed!")
