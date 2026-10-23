"""
Problem: Koko Eating Bananas (LeetCode #875)
Binary Search on Answer Range
Time Complexity: O(N log(max(P)))
Space Complexity: O(1)
"""

import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        while low < high:
            speed = low + (high - low) // 2

            # Total hours needed at this eating speed
            hours = sum(math.ceil(pile / speed) for pile in piles)

            if hours <= h:
                high = speed  # Could be optimal, or can eat slower
            else:
                low = speed + 1  # Too slow, must speed up

        return low

if __name__ == "__main__":
    sol = Solution()
    assert sol.minEatingSpeed([3, 6, 7, 11], 8) == 4
    assert sol.minEatingSpeed([30, 11, 23, 4, 20], 5) == 30
    assert sol.minEatingSpeed([30, 11, 23, 4, 20], 6) == 23
    print("✅ All Koko Eating Bananas tests passed!")
