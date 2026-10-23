"""
Problem: Longest Substring Without Repeating Characters (LeetCode #3)
Sliding Window with Hash Map Index Tracking
Time Complexity: O(N)
Space Complexity: O(min(N, M))
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        left = 0
        max_length = 0

        for right, char in enumerate(s):
            # If char was seen inside the current window, move left past its previous index
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1

            char_index[char] = right
            max_length = max(max_length, right - left + 1)

        return max_length

if __name__ == "__main__":
    sol = Solution()
    assert sol.lengthOfLongestSubstring("abcabcbb") == 3
    assert sol.lengthOfLongestSubstring("bbbbb") == 1
    assert sol.lengthOfLongestSubstring("pwwkew") == 3
    assert sol.lengthOfLongestSubstring("") == 0
    print("✅ All Longest Substring Without Repeating Characters tests passed!")
