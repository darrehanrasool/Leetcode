"""
Problem: Group Anagrams (LeetCode #49)
Categorize by Sorted String Key
Time Complexity: O(N * K log K)
Space Complexity: O(N * K)
"""

from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for word in strs:
            # Canonical key is sorted characters of the word
            sorted_key = "".join(sorted(word))
            anagram_map[sorted_key].append(word)

        return list(anagram_map.values())

if __name__ == "__main__":
    sol = Solution()
    res = sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    # Sort results for deterministic assertion
    sorted_res = sorted([sorted(group) for group in res])
    expected = sorted([["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])
    assert sorted_res == expected
    print("✅ All Group Anagrams tests passed!")
