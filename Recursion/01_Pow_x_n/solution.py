"""
Problem: Pow(x, n) (LeetCode #50)
Binary Exponentiation Divide & Conquer
Time Complexity: O(log N)
Space Complexity: O(log N)
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n < 0:
            return 1.0 / self.myPow(x, -n)

        half = self.myPow(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x

if __name__ == "__main__":
    sol = Solution()
    assert abs(sol.myPow(2.0, 10) - 1024.0) < 1e-5
    assert abs(sol.myPow(2.0, -2) - 0.25) < 1e-5
    print("✅ All Pow(x, n) tests passed!")
