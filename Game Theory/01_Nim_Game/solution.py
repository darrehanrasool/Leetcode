"""
Problem: Nim Game (LeetCode #292)
Game Theory Modular Arithmetic
"""

class Solution:
    def canWinNim(self, n: int) -> bool:
        # If n is a multiple of 4, the second player can always win!
        return n % 4 != 0

if __name__ == "__main__":
    sol = Solution()
    assert sol.canWinNim(4) is False
    assert sol.canWinNim(1) is True
    assert sol.canWinNim(2) is True
    print("✅ All Nim Game tests passed!")
