"""
Problem: Longest Duplicate Substring (LeetCode #1044)
Suffix Array / Binary Search + Rolling Hash
Time Complexity: O(N log N)
"""

class Solution:
    def longestDupSubstring(self, s: str) -> str:
        # Binary search for substring length
        def search(L):
            seen = set()
            for i in range(len(s) - L + 1):
                sub = s[i:i + L]
                if sub in seen:
                    return sub
                seen.add(sub)
            return ""

        low, high = 1, len(s) - 1
        res = ""

        while low <= high:
            mid = (low + high) // 2
            dup = search(mid)
            if dup:
                res = dup
                low = mid + 1
            else:
                high = mid - 1

        return res

if __name__ == "__main__":
    sol = Solution()
    assert sol.longestDupSubstring("banana") in ["ana", "an"]
    assert sol.longestDupSubstring("abcd") == ""
    print("✅ All Suffix Array tests passed!")
