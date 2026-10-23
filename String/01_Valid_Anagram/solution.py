"""
Problem: Valid Anagram (LeetCode #242)
Frequency Counting with Hash Map
Time Complexity: O(N)
Space Complexity: O(1)
"""

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)

if __name__ == "__main__":
    sol = Solution()
    assert sol.isAnagram("anagram", "nagaram") is True
    assert sol.isAnagram("rat", "car") is False
    print("✅ All Valid Anagram tests passed!")
