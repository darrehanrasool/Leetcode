"""
Problem: Find the Index of the First Occurrence in a String (LeetCode #28)
KMP (Knuth-Morris-Pratt) Algorithm
Time Complexity: O(N + M)
Space Complexity: O(M)
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        # Step 1: Precompute LPS (Longest Prefix Suffix) table
        lps = [0] * len(needle)
        prev_lps, i = 0, 1
        while i < len(needle):
            if needle[i] == needle[prev_lps]:
                lps[i] = prev_lps + 1
                prev_lps += 1
                i += 1
            elif prev_lps == 0:
                lps[i] = 0
                i += 1
            else:
                prev_lps = lps[prev_lps - 1]

        # Step 2: Search haystack using LPS
        h, n = 0, 0
        while h < len(haystack):
            if haystack[h] == needle[n]:
                h += 1
                n += 1
            else:
                if n == 0:
                    h += 1
                else:
                    n = lps[n - 1]

            if n == len(needle):
                return h - len(needle)

        return -1

if __name__ == "__main__":
    sol = Solution()
    assert sol.strStr("sadbutsad", "sad") == 0
    assert sol.strStr("leetcode", "leeto") == -1
    print("✅ All KMP / String Matching tests passed!")
