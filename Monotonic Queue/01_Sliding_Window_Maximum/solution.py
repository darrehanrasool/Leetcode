"""
Problem: Sliding Window Maximum (LeetCode #239)
Monotonic Deque Approach
Time Complexity: O(N)
Space Complexity: O(K)
"""

from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()  # stores indices
        res = []

        for i, num in enumerate(nums):
            # Remove indices that are out of the active window
            while q and q[0] < i - k + 1:
                q.popleft()

            # Remove smaller elements from back
            while q and nums[q[-1]] < num:
                q.pop()

            q.append(i)

            # Record max once window reaches size k
            if i >= k - 1:
                res.append(nums[q[0]])

        return res

if __name__ == "__main__":
    sol = Solution()
    assert sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]
    assert sol.maxSlidingWindow([1], 1) == [1]
    print("✅ All Sliding Window Maximum tests passed!")
