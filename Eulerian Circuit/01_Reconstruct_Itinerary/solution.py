"""
Problem: Reconstruct Itinerary (LeetCode #332)
Hierholzer's Eulerian Path Algorithm
Time Complexity: O(E log E)
"""

from collections import defaultdict
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[int]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            adj[src].append(dst)

        itinerary = []

        def dfs(airport):
            while adj[airport]:
                next_stop = adj[airport].pop()
                dfs(next_stop)
            itinerary.append(airport)

        dfs("JFK")
        return itinerary[::-1]

if __name__ == "__main__":
    sol = Solution()
    t = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
    assert sol.findItinerary(t) == ["JFK","MUC","LHR","SFO","SJC"]
    print("✅ All Eulerian Circuit / Itinerary tests passed!")
