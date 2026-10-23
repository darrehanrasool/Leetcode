"""
Problem Name: Two Sum
LeetCode Link: https://leetcode.com/problems/two-sum/
Difficulty: Easy
Topic: Array / Hash Table
Companies: Google, Meta, OpenAI, Amazon, Apple

Real-Life Analogy:
Finding two coupons in your wallet whose values sum up to the exact price of an item.
Instead of trying every pair, as you inspect each coupon, you compute the "missing amount"
and check your notebook of previously seen coupons.
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Optimal One-Pass Hash Map Solution.
        Time Complexity: O(N) where N is the number of elements in nums.
        Space Complexity: O(N) to store up to N elements in the hash map.
        """
        # Step 1: Create a hash map (dictionary) to remember numbers we have seen.
        # Key: the number itself (int)
        # Value: the index where that number appeared in the array (int)
        seen = {}

        # Step 2: Loop through the array using enumerate to get both the index (i)
        # and the value (num) at that index.
        for i, num in enumerate(nums):
            # Step 3: Calculate the number we need to reach the target sum.
            complement = target - num

            # Step 4: Check if our missing complement was already seen earlier.
            if complement in seen:
                # We found the pair!
                # seen[complement] is the index of the previously seen number.
                # i is the current index.
                return [seen[complement], i]

            # Step 5: If not found, store the current number and its index in 'seen'
            # so future numbers can use it as their complement.
            seen[num] = i

        # Step 6: Return an empty list if no pair sums to the target
        # (Though LeetCode guarantees exactly one solution).
        return []

    def twoSum_brute_force(self, nums: List[int], target: int) -> List[int]:
        """
        Naive Brute Force Solution for Comparison.
        Time Complexity: O(N^2) due to nested loops.
        Space Complexity: O(1) as no extra memory is allocated.
        """
        n = len(nums)
        # Outer loop checks the first number
        for i in range(n):
            # Inner loop checks all numbers after the first number
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


# =====================================================================
# Quick Tests & Verification
# Run this script directly with: python3 solution.py
# =====================================================================
if __name__ == "__main__":
    solver = Solution()

    # Test Case 1: Standard case
    test1_nums = [2, 7, 11, 15]
    test1_target = 9
    result1 = solver.twoSum(test1_nums, test1_target)
    print(f"Test 1: nums={test1_nums}, target={test1_target} -> Output: {result1}")
    assert result1 == [0, 1], f"Expected [0, 1] but got {result1}"

    # Test Case 2: Numbers not sorted
    test2_nums = [3, 2, 4]
    test2_target = 6
    result2 = solver.twoSum(test2_nums, test2_target)
    print(f"Test 2: nums={test2_nums}, target={test2_target} -> Output: {result2}")
    assert result2 == [1, 2], f"Expected [1, 2] but got {result2}"

    # Test Case 3: Duplicate numbers
    test3_nums = [3, 3]
    test3_target = 6
    result3 = solver.twoSum(test3_nums, test3_target)
    print(f"Test 3: nums={test3_nums}, target={test3_target} -> Output: {result3}")
    assert result3 == [0, 1], f"Expected [0, 1] but got {result3}"

    # Test Case 4: Negative numbers
    test4_nums = [-3, 4, 3, 90]
    test4_target = 0
    result4 = solver.twoSum(test4_nums, test4_target)
    print(f"Test 4: nums={test4_nums}, target={test4_target} -> Output: {result4}")
    assert result4 == [0, 2], f"Expected [0, 2] but got {result4}"

    print("\n✅ All tests passed successfully!")
