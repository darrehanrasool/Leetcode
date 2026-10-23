"""
Problem: Minimum Window Substring (LeetCode #76)
Sliding Window with Frequency Map & Have/Need Matching
Time Complexity: O(M + N)
Space Complexity: O(M + N)
"""

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        target_counts = Counter(t)
        window_counts = {}
        have, need = 0, len(target_counts)

        res, res_len = [-1, -1], float("inf")
        left = 0

        for right, char in enumerate(s):
            window_counts[char] = window_counts.get(char, 0) + 1

            if char in target_counts and window_counts[char] == target_counts[char]:
                have += 1

            # When window has all characters, shrink from left
            while have == need:
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                # Pop left character
                left_char = s[left]
                window_counts[left_char] -= 1
                if left_char in target_counts and window_counts[left_char] < target_counts[left_char]:
                    have -= 1
                left += 1

        l, r = res
        return s[l:r + 1] if res_len != float("inf") else ""

if __name__ == "__main__":
    sol = Solution()
    assert sol.minWindow("ADOBECODEBANC", "ABC") == "BANC"
    assert sol.minWindow("a", "a") == "a"
    assert sol.minWindow("a", "aa") == ""
    print("✅ All Minimum Window Substring tests passed!")
