"""
Problem: Ransom Note (LeetCode #383)
Hash Map Frequency Matching
Time Complexity: O(M + N)
Space Complexity: O(1)
"""

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_counts = Counter(magazine)

        for char in ransomNote:
            if mag_counts[char] <= 0:
                return False
            mag_counts[char] -= 1

        return True

if __name__ == "__main__":
    sol = Solution()
    assert sol.canConstruct("a", "b") is False
    assert sol.canConstruct("aa", "ab") is False
    assert sol.canConstruct("aa", "aab") is True
    print("✅ All Ransom Note tests passed!")
