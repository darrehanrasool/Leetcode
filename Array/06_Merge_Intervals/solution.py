"""
Problem Name: Merge Intervals
LeetCode Link: https://leetcode.com/problems/merge-intervals/
Difficulty: Medium
Topic: Array / Sorting / Intervals
Companies: Meta (Facebook - #1 Most Asked Question), Google, Amazon, Microsoft, Uber

Real-Life Analogy:
Merging overlapping calendar bookings for a conference room. By sorting
meetings by start time, any meeting only needs to be checked against the
end time of the current ongoing merged meeting.
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Optimal Sorting & Single-Pass Greedy Merge Solution.
        Time Complexity: O(N log N) where N is the number of intervals.
        Space Complexity: O(N) to store the merged result.
        """
        # Edge case: If there are no intervals or just 1, nothing to merge.
        if not intervals:
            return []

        # Step 1: Sort the intervals by their start time (index 0).
        # This guarantees that for any subsequent interval, its start time
        # is greater than or equal to previous intervals' start times.
        intervals.sort(key=lambda interval: interval[0])

        # Step 2: Initialize our merged intervals list.
        # We start by placing a copy of the very first interval into the list.
        merged = [intervals[0].copy()]

        # Step 3: Iterate through the remaining intervals starting from index 1.
        for current_start, current_end in intervals[1:]:
            # Get the end time of the latest interval in our merged list.
            last_merged_start, last_merged_end = merged[-1]

            # Case A: Overlap exists!
            # If the current interval starts BEFORE or AT the same time the previous
            # interval finishes (current_start <= last_merged_end), they must merge.
            if current_start <= last_merged_end:
                # Extend the end of the previous interval to whichever ends later.
                merged[-1][1] = max(last_merged_end, current_end)
            else:
                # Case B: No overlap exists.
                # The current interval starts after the previous one finishes.
                # Append it as a new distinct interval.
                merged.append([current_start, current_end])

        # Step 4: Return the merged intervals list.
        return merged


# =====================================================================
# Quick Tests & Verification
# Run this script directly with: python3 solution.py
# =====================================================================
if __name__ == "__main__":
    solver = Solution()

    # Test Case 1: Standard overlapping intervals
    test1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
    res1 = solver.merge(test1)
    print(f"Test 1: {test1} -> Merged: {res1}")
    assert res1 == [[1, 6], [8, 10], [15, 18]], f"Expected [[1, 6], [8, 10], [15, 18]], got {res1}"

    # Test Case 2: Touching at boundaries
    test2 = [[1, 4], [4, 5]]
    res2 = solver.merge(test2)
    print(f"Test 2: {test2} -> Merged: {res2}")
    assert res2 == [[1, 5]], f"Expected [[1, 5]], got {res2}"

    # Test Case 3: Completely enclosed / swallowed interval
    test3 = [[1, 10], [2, 3], [4, 8]]
    res3 = solver.merge(test3)
    print(f"Test 3: {test3} -> Merged: {res3}")
    assert res3 == [[1, 10]], f"Expected [[1, 10]], got {res3}"

    # Test Case 4: Unsorted intervals input
    test4 = [[2, 6], [1, 3], [8, 10], [15, 18]]
    res4 = solver.merge(test4)
    print(f"Test 4: {test4} -> Merged: {res4}")
    assert res4 == [[1, 6], [8, 10], [15, 18]], f"Expected [[1, 6], [8, 10], [15, 18]], got {res4}"

    print("\n✅ All tests passed successfully!")
