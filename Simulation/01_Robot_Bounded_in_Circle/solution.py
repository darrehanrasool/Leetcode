"""
Problem: Robot Bounded In Circle (LeetCode #1041)
Simulation & Cycle Detection
"""

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # Directions: North, East, South, West
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y = 0, 0
        d = 0  # North

        for char in instructions:
            if char == "G":
                dx, dy = directions[d]
                x += dx
                y += dy
            elif char == "L":
                d = (d - 1) % 4
            elif char == "R":
                d = (d + 1) % 4

        # Returns to origin OR doesn't face North
        return (x == 0 and y == 0) or (d != 0)

if __name__ == "__main__":
    sol = Solution()
    assert sol.isRobotBounded("GGLLGG") is True
    assert sol.isRobotBounded("GG") is False
    assert sol.isRobotBounded("GL") is True
    print("✅ All Robot Bounded In Circle tests passed!")
