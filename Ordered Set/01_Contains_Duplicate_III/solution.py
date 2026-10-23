"""
Problem: Contains Duplicate III (LeetCode #220)
Bucket / Ordered Set Window
Time Complexity: O(N)
Space Complexity: O(k)
"""

from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if valueDiff < 0:
            return False

        buckets = {}
        w = valueDiff + 1

        for i, val in enumerate(nums):
            m = val // w

            if m in buckets:
                return True
            if m - 1 in buckets and abs(val - buckets[m - 1]) <= valueDiff:
                return True
            if m + 1 in buckets and abs(val - buckets[m + 1]) <= valueDiff:
                return True

            buckets[m] = val
            if i >= indexDiff:
                del buckets[nums[i - indexDiff] // w]

        return False

if __name__ == "__main__":
    sol = Solution()
    assert sol.containsNearbyAlmostDuplicate([1,2,3,1], 3, 0) is True
    assert sol.containsNearbyAlmostDuplicate([1,5,9,1,5,9], 2, 3) is False
    print("✅ All Ordered Set tests passed!")
