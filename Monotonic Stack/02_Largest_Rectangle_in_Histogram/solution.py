"""
Problem: Largest Rectangle in Histogram (LeetCode #84)
Monotonic Increasing Stack
Time Complexity: O(N)
Space Complexity: O(N)
"""

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []  # pair: (start_index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                max_area = max(max_area, height * (i - idx))
                start = idx
            stack.append((start, h))

        # Check remaining elements extending to end of array
        for idx, height in stack:
            max_area = max(max_area, height * (len(heights) - idx))

        return max_area

if __name__ == "__main__":
    sol = Solution()
    assert sol.largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10
    assert sol.largestRectangleArea([2, 4]) == 4
    print("✅ All Largest Rectangle in Histogram tests passed!")
