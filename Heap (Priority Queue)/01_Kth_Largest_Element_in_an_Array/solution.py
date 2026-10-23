"""
Problem: Kth Largest Element in an Array (LeetCode #215)
Min-Heap of Size K
Time Complexity: O(N log K)
Space Complexity: O(K)
"""

import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]

if __name__ == "__main__":
    sol = Solution()
    assert sol.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
    assert sol.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    print("✅ All Kth Largest Element tests passed!")
