"""
Problem Name: Contains Duplicate
LeetCode Link: https://leetcode.com/problems/contains-duplicate/
Difficulty: Easy
Topic: Array / Hash Table / Hash Set
Companies: Meta (Facebook), Apple, Amazon, Adobe, Microsoft

Real-Life Analogy:
A bouncer checking guest IDs at the door. If a scanned ID is already in the
guest database (set), the alarm rings immediately.
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Optimal Hash Set Solution with Early Exit.
        Time Complexity: O(N) where N is the length of nums.
        Space Complexity: O(N) to store unique numbers in a set.
        """
        # Step 1: Create an empty hash set to record seen values.
        # Looking up or adding an element to a hash set takes O(1) time on average.
        seen = set()

        # Step 2: Iterate through each number in the array.
        for num in nums:
            # Step 3: If the number is already present in our set,
            # we have encountered a duplicate! Return True immediately.
            if num in seen:
                return True

            # Step 4: Otherwise, add the number to the set and continue.
            seen.add(num)

        # Step 5: If the loop finishes without finding any matches, all numbers are unique.
        return False

    def containsDuplicate_one_liner(self, nums: List[int]) -> bool:
        """
        Pythonic alternative using set length comparison.
        Converting a list to a set automatically discards duplicates.
        If the set is smaller than the original list, duplicates existed!
        """
        return len(nums) != len(set(nums))

    def containsDuplicate_sorting(self, nums: List[int]) -> bool:
        """
        Sorting Approach (Optimizing for Space).
        Time Complexity: O(N log N) for sorting.
        Space Complexity: O(1) auxiliary space (depending on Python's Timsort).
        """
        nums.sort()  # Sort numbers in-place
        for i in range(1, len(nums)):
            # If two adjacent elements are identical, a duplicate exists
            if nums[i] == nums[i - 1]:
                return True
        return False


# =====================================================================
# Quick Tests & Verification
# Run this script directly with: python3 solution.py
# =====================================================================
if __name__ == "__main__":
    solver = Solution()

    # Test Case 1: Has duplicates
    test1 = [1, 2, 3, 1]
    res1 = solver.containsDuplicate(test1)
    print(f"Test 1: {test1} -> Contains Duplicate: {res1}")
    assert res1 is True, f"Expected True, got {res1}"

    # Test Case 2: All unique
    test2 = [1, 2, 3, 4]
    res2 = solver.containsDuplicate(test2)
    print(f"Test 2: {test2} -> Contains Duplicate: {res2}")
    assert res2 is False, f"Expected False, got {res2}"

    # Test Case 3: Multiple duplicates
    test3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    res3 = solver.containsDuplicate(test3)
    print(f"Test 3: {test3} -> Contains Duplicate: {res3}")
    assert res3 is True, f"Expected True, got {res3}"

    # Test Case 4: Single element (always False)
    test4 = [99]
    res4 = solver.containsDuplicate(test4)
    print(f"Test 4: {test4} -> Contains Duplicate: {res4}")
    assert res4 is False, f"Expected False, got {res4}"

    print("\n✅ All tests passed successfully!")
