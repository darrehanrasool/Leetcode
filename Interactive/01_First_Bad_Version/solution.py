"""
Problem: First Bad Version (LeetCode #278)
Interactive Binary Search API
"""

# Dummy mock API for testing
BAD_VERSION = 4
def isBadVersion(version: int) -> bool:
    return version >= BAD_VERSION

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low, high = 1, n
        while low < high:
            mid = low + (high - low) // 2
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1
        return low

if __name__ == "__main__":
    sol = Solution()
    assert sol.firstBadVersion(5) == 4
    print("✅ All Interactive tests passed!")
