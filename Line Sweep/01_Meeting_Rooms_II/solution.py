"""
Problem: Meeting Rooms II (LeetCode #253)
Line Sweep / Chronological Event Sorting
Time Complexity: O(N log N)
Space Complexity: O(N)
"""

from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted([i[0] for i in intervals])
        ends = sorted([i[1] for i in intervals])

        res = 0
        count = 0
        s = e = 0

        while s < len(starts):
            if starts[s] < ends[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            res = max(res, count)

        return res

if __name__ == "__main__":
    sol = Solution()
    assert sol.minMeetingRooms([[0, 30], [5, 10], [15, 20]]) == 2
    assert sol.minMeetingRooms([[7, 10], [2, 4]]) == 1
    print("✅ All Line Sweep tests passed!")
