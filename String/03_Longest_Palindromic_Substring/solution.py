"""
Problem: Longest Palindromic Substring (LeetCode #5)
Expand Around Center Approach
Time Complexity: O(N^2)
Space Complexity: O(1)
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start, end = 0, 0

        def expand_around_center(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Length is (right - 1) - (left + 1) + 1 = right - left - 1
            return right - left - 1

        for i in range(len(s)):
            len_odd = expand_around_center(i, i)
            len_even = expand_around_center(i, i + 1)
            max_len = max(len_odd, len_even)

            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end + 1]

if __name__ == "__main__":
    sol = Solution()
    assert sol.longestPalindrome("babad") in ["bab", "aba"]
    assert sol.longestPalindrome("cbbd") == "bb"
    assert sol.longestPalindrome("a") == "a"
    print("✅ All Longest Palindromic Substring tests passed!")
