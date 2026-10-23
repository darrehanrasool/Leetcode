"""
Problem Name: Best Time to Buy and Sell Stock
LeetCode Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Difficulty: Easy
Topic: Array / Greedy / Dynamic Programming
Companies: Google, Meta (Facebook), Amazon, Microsoft, Apple, Citadel

Real-Life Analogy:
Walking forward in time through daily asset prices. You remember the cheapest
price you have seen so far (the best day to have bought) and at every step check
how much money you would pocket if you sold right now.
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Optimal Single-Pass Greedy Solution.
        Time Complexity: O(N) where N is the length of prices.
        Space Complexity: O(1) as we only use two scalar variables.
        """
        # Step 1: Initialize min_price to infinity so any valid price will be smaller.
        min_price = float('inf')

        # Step 2: Initialize max_profit to 0 (since profit cannot be negative).
        max_profit = 0

        # Step 3: Iterate through each day's price in chronological order.
        for price in prices:
            # Case A: We found a price cheaper than our previous minimum buy price.
            # Update our minimum buy price.
            if price < min_price:
                min_price = price
            else:
                # Case B: Today's price is higher than our minimum buy price.
                # Calculate the profit if we sell today.
                current_profit = price - min_price

                # If this profit is the highest seen so far, update max_profit.
                if current_profit > max_profit:
                    max_profit = current_profit

        # Step 4: Return the maximum profit found (or 0 if no profit was possible).
        return max_profit

    def maxProfit_compact(self, prices: List[int]) -> int:
        """
        Equivalent concise Pythonic formulation often written in interviews.
        """
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit


# =====================================================================
# Quick Tests & Verification
# Run this script directly with: python3 solution.py
# =====================================================================
if __name__ == "__main__":
    solver = Solution()

    # Test Case 1: Standard profitable case
    test1 = [7, 1, 5, 3, 6, 4]
    res1 = solver.maxProfit(test1)
    print(f"Test 1: prices={test1} -> Max Profit: {res1}")
    assert res1 == 5, f"Expected 5, got {res1}"

    # Test Case 2: Strictly decreasing prices (no profit possible)
    test2 = [7, 6, 4, 3, 1]
    res2 = solver.maxProfit(test2)
    print(f"Test 2: prices={test2} -> Max Profit: {res2}")
    assert res2 == 0, f"Expected 0, got {res2}"

    # Test Case 3: Lowest price is at the very end
    test3 = [3, 8, 1]
    res3 = solver.maxProfit(test3)
    print(f"Test 3: prices={test3} -> Max Profit: {res3}")
    assert res3 == 5, f"Expected 5, got {res3}"

    # Test Case 4: Single element
    test4 = [5]
    res4 = solver.maxProfit(test4)
    print(f"Test 4: prices={test4} -> Max Profit: {res4}")
    assert res4 == 0, f"Expected 0, got {res4}"

    print("\n✅ All tests passed successfully!")
