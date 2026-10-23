"""
Problem Name: Maximum Subarray
LeetCode Link: https://leetcode.com/problems/maximum-subarray/
Difficulty: Medium
Topic: Array / Dynamic Programming / Divide and Conquer
Companies: Google, Meta (Facebook), ByteDance, Amazon, Microsoft, LinkedIn

Real-Life Analogy:
A company calculating its longest and highest profitable financial streak.
Whenever past operations leave you in net negative debt, you discard the past
and start a fresh streak today so the negative debt does not drag you down.
"""

from typing import List, Tuple


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Optimal Kadane's Algorithm.
        Time Complexity: O(N) where N is the length of nums.
        Space Complexity: O(1) auxiliary space.
        """
        # Step 1: Initialize max_sum with the first element.
        # We cannot initialize to 0 because if all elements are negative,
        # the answer is the largest negative number (not 0).
        max_sum = nums[0]

        # Step 2: Initialize our running sum for the current active subarray.
        current_sum = 0

        # Step 3: Iterate through every number in the array.
        for num in nums:
            # If our previous subarray accumulated a negative sum, it will only
            # reduce the sum of any future subarray. So reset it to 0!
            if current_sum < 0:
                current_sum = 0

            # Add the current number to our active subarray sum.
            current_sum += num

            # Update our all-time highest subarray sum.
            if current_sum > max_sum:
                max_sum = current_sum

        # Step 4: Return the maximum sum found.
        return max_sum

    def maxSubArray_with_indices(self, nums: List[int]) -> Tuple[int, int, int]:
        """
        Interview Bonus: Not only return the max sum, but also return
        the (start_index, end_index) of the winning subarray!
        """
        max_sum = nums[0]
        current_sum = 0
        best_start = best_end = 0
        temp_start = 0

        for i, num in enumerate(nums):
            if current_sum < 0:
                current_sum = 0
                temp_start = i  # New streak begins here

            current_sum += num

            if current_sum > max_sum:
                max_sum = current_sum
                best_start = temp_start
                best_end = i

        return max_sum, best_start, best_end


# =====================================================================
# Quick Tests & Verification
# Run this script directly with: python3 solution.py
# =====================================================================
if __name__ == "__main__":
    solver = Solution()

    # Test Case 1: Standard mixed positive and negative numbers
    test1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    res1 = solver.maxSubArray(test1)
    max_sum1, start1, end1 = solver.maxSubArray_with_indices(test1)
    print(f"Test 1: {test1}")
    print(f"  -> Max Sum: {res1}")
    print(f"  -> Subarray: nums[{start1}:{end1+1}] = {test1[start1:end1+1]}")
    assert res1 == 6, f"Expected 6, got {res1}"

    # Test Case 2: All negative numbers
    test2 = [-5, -2, -8, -1, -4]
    res2 = solver.maxSubArray(test2)
    print(f"Test 2: {test2} -> Max Sum: {res2}")
    assert res2 == -1, f"Expected -1, got {res2}"

    # Test Case 3: Single element
    test3 = [1]
    res3 = solver.maxSubArray(test3)
    print(f"Test 3: {test3} -> Max Sum: {res3}")
    assert res3 == 1, f"Expected 1, got {res3}"

    # Test Case 4: All positive numbers
    test4 = [5, 4, 1, 7, 8]
    res4 = solver.maxSubArray(test4)
    print(f"Test 4: {test4} -> Max Sum: {res4}")
    assert res4 == 25, f"Expected 25, got {res4}"

    print("\n✅ All tests passed successfully!")
