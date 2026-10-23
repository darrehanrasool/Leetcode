"""
Problem: Sequential Digits (LeetCode #1291)
Enumeration / Sliding Window on String Digits
"""

from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        sample = "123456789"
        res = []

        for length in range(len(str(low)), len(str(high)) + 1):
            for start in range(len(sample) - length + 1):
                num = int(sample[start : start + length])
                if low <= num <= high:
                    res.append(num)

        return res

if __name__ == "__main__":
    sol = Solution()
    assert sol.sequentialDigits(100, 300) == [123, 234]
    print("✅ All Sequential Digits tests passed!")
