"""
Problem: Counting Sort / Frequency Sort (LeetCode #451)
Time Complexity: O(N)
Space Complexity: O(N)
"""

from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        # Bucket sort by frequency
        buckets = [[] for _ in range(len(s) + 1)]
        for char, freq in counts.items():
            buckets[freq].append(char)

        res = []
        for freq in range(len(s), 0, -1):
            for char in buckets[freq]:
                res.append(char * freq)

        return "".join(res)

if __name__ == "__main__":
    sol = Solution()
    res = sol.frequencySort("tree")
    assert res in ["eert", "eetr"]
    print("✅ All Counting / Frequency Sort tests passed!")
