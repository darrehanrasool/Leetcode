"""
Problem: Gas Station (LeetCode #134)
Single-Pass Greedy Running Tank
Time Complexity: O(N)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total_tank = 0
        start = 0

        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            if total_tank < 0:
                total_tank = 0
                start = i + 1

        return start

if __name__ == "__main__":
    sol = Solution()
    assert sol.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]) == 3
    assert sol.canCompleteCircuit([2,3,4], [3,4,3]) == -1
    print("✅ All Gas Station tests passed!")
