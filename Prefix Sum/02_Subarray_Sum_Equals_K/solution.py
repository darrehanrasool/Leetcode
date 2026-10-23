"""
Problem: Subarray Sum Equals K (LeetCode #560)
Prefix Sum + Hash Map Frequency Counting
Time Complexity: O(N)
Space Complexity: O(N)
"""

from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        prefix_counts = {0: 1}  # Base case: sum of 0 occurs once initially

        for num in nums:
            current_sum += num

            # If (current_sum - k) was seen before, add its frequency
            if current_sum - k in prefix_counts:
                count += prefix_counts[current_sum - k]

            # Record frequency of current prefix sum
            prefix_counts[current_sum] = prefix_counts.get(current_sum, 0) + 1

        return count

if __name__ == "__main__":
    sol = Solution()
    assert sol.subarraySum([1, 1, 1], 2) == 2
    assert sol.subarraySum([1, 2, 3], 3) == 2
    assert sol.subarraySum([1, -1, 0], 0) == 3
    print("✅ All Subarray Sum Equals K tests passed!")
