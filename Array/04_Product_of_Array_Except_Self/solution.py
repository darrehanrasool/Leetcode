"""
Problem Name: Product of Array Except Self
LeetCode Link: https://leetcode.com/problems/product-of-array-except-self/
Difficulty: Medium
Topic: Array / Prefix Product
Companies: Meta (Facebook - Top Asked), Google, Amazon, Microsoft, OpenAI

Real-Life Analogy:
Evaluating an ensemble of experts: for each expert, calculate the collective
strength of all other experts without using division. We split the calculation
into (everything to the left) multiplied by (everything to the right).
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Optimal O(N) Time and O(1) Extra Space Solution.

        We build the answer using two passes:
        1. Forward pass: Each position stores the product of all elements to its left.
        2. Backward pass: Multiply each position by a running product of elements to its right.
        """
        n = len(nums)

        # Step 1: Create output array initialized with 1s.
        # This will hold the result and does not count as auxiliary space.
        res = [1] * n

        # Step 2: Pass 1 (Left-to-Right)
        # Calculate prefix products: res[i] will store the product of all nums[0...i-1].
        prefix = 1
        for i in range(n):
            res[i] = prefix       # Store product of all elements to the left of i
            prefix *= nums[i]     # Update prefix to include the current element

        # Step 3: Pass 2 (Right-to-Left)
        # Calculate suffix products and multiply directly into res[i].
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix      # Multiply by product of all elements to the right of i
            suffix *= nums[i]     # Update suffix to include the current element

        # Step 4: Return the combined result
        return res

    def productExceptSelf_prefix_suffix_arrays(self, nums: List[int]) -> List[int]:
        """
        Intuitive 2-Array Approach (O(N) Time, O(N) Space).
        Great to explain first in an interview before optimizing space!
        """
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n

        # Build prefix products
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        # Build suffix products
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        # Multiply prefix and suffix
        res = [prefix[i] * suffix[i] for i in range(n)]
        return res


# =====================================================================
# Quick Tests & Verification
# Run this script directly with: python3 solution.py
# =====================================================================
if __name__ == "__main__":
    solver = Solution()

    # Test Case 1: Standard positive numbers
    test1 = [1, 2, 3, 4]
    res1 = solver.productExceptSelf(test1)
    print(f"Test 1: {test1} -> Output: {res1}")
    assert res1 == [24, 12, 8, 6], f"Expected [24, 12, 8, 6], got {res1}"

    # Test Case 2: Array containing a single zero
    test2 = [-1, 1, 0, -3, 3]
    res2 = solver.productExceptSelf(test2)
    print(f"Test 2: {test2} -> Output: {res2}")
    assert res2 == [0, 0, 9, 0, 0], f"Expected [0, 0, 9, 0, 0], got {res2}"

    # Test Case 3: Array containing multiple zeros
    test3 = [0, 4, 0]
    res3 = solver.productExceptSelf(test3)
    print(f"Test 3: {test3} -> Output: {res3}")
    assert res3 == [0, 0, 0], f"Expected [0, 0, 0], got {res3}"

    print("\n✅ All tests passed successfully!")
