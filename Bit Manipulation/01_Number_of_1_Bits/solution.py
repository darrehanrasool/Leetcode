"""
Problem: Number of 1 Bits (LeetCode #191)
Brian Kernighan's Bit-Clearing Algorithm
Time Complexity: O(number of 1 bits)
Space Complexity: O(1)
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= (n - 1)  # Clear the lowest set bit
            count += 1
        return count

if __name__ == "__main__":
    sol = Solution()
    assert sol.hammingWeight(11) == 3   # 11 is 1011 in binary
    assert sol.hammingWeight(128) == 1  # 128 is 10000000
    assert sol.hammingWeight(0) == 0
    print("✅ All Number of 1 Bits tests passed!")
