"""
Problem: Top K Frequent Elements (LeetCode #347)
Frequency Map + Min-Heap
Time Complexity: O(N log K)
Space Complexity: O(N)
"""

from collections import Counter
import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        heap = []

        for num, freq in counts.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)

        return [num for freq, num in heap]

if __name__ == "__main__":
    sol = Solution()
    res = sol.topKFrequent([1, 1, 1, 2, 2, 3], 2)
    assert sorted(res) == [1, 2]
    print("✅ All Top K Frequent Elements tests passed!")
