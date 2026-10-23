"""
Problem: Bulb Switcher (LeetCode #319)
Math Brainteaser: Perfect Squares
"""

import math

class Solution:
    def bulbSwitch(self, n: int) -> int:
        # Only numbers with an odd number of divisors remain ON (perfect squares!)
        return int(math.isqrt(n))

if __name__ == "__main__":
    sol = Solution()
    assert sol.bulbSwitch(3) == 1
    assert sol.bulbSwitch(0) == 0
    assert sol.bulbSwitch(1) == 1
    print("✅ All Bulb Switcher tests passed!")
