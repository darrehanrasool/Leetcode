"""
Problem: Valid Palindrome (LeetCode #125)
Two Pointers In-Place Approach
Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize left pointer at the start and right pointer at the end
        left = 0
        right = len(s) - 1

        while left < right:
            # Skip non-alphanumeric characters on the left side
            while left < right and not s[left].isalnum():
                left += 1

            # Skip non-alphanumeric characters on the right side
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare characters ignoring case
            if s[left].lower() != s[right].lower():
                return False

            # Move both pointers inward
            left += 1
            right -= 1

        return True

if __name__ == "__main__":
    sol = Solution()
    t1 = "A man, a plan, a canal: Panama"
    t2 = "race a car"
    t3 = " "
    assert sol.isPalindrome(t1) is True
    assert sol.isPalindrome(t2) is False
    assert sol.isPalindrome(t3) is True
    print("✅ All Valid Palindrome tests passed!")
