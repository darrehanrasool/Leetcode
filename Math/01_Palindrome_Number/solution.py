"""
Problem: Palindrome Number (LeetCode #9)
Math Reverse without String Conversion
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverted_number = 0
        while x > reverted_number:
            reverted_number = reverted_number * 10 + x % 10
            x //= 10

        return x == reverted_number or x == reverted_number // 10

if __name__ == "__main__":
    sol = Solution()
    assert sol.isPalindrome(121) is True
    assert sol.isPalindrome(-121) is False
    assert sol.isPalindrome(10) is False
    print("✅ All Palindrome Number tests passed!")
