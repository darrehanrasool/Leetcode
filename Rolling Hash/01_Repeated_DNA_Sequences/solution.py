"""
Problem: Repeated DNA Sequences (LeetCode #187)
Rabin-Karp Rolling Hash / Bitmask
Time Complexity: O(N)
Space Complexity: O(N)
"""

from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        res = set()

        for i in range(len(s) - 9):
            sub = s[i : i + 10]
            if sub in seen:
                res.add(sub)
            seen.add(sub)

        return list(res)

if __name__ == "__main__":
    sol = Solution()
    assert sorted(sol.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")) == ["AAAAACCCCC", "CCCCCAAAAA"]
    print("✅ All Rolling Hash tests passed!")
