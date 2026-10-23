"""
Problem: Climbing Stairs (LeetCode #70)
Bottom-Up DP with O(1) Space
Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        one, two = 1, 2
        for _ in range(3, n + 1):
            one, two = two, one + two

        return two

if __name__ == "__main__":
    sol = Solution()
    assert sol.climbStairs(2) == 2
    assert sol.climbStairs(3) == 3
    assert sol.climbStairs(5) == 8
    print("✅ All Climbing Stairs tests passed!")
