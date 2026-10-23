"""
Problem: Valid Parentheses (LeetCode #20)
Stack-Based Bracket Matching
Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else "#"
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0

if __name__ == "__main__":
    sol = Solution()
    assert sol.isValid("()[]{}") is True
    assert sol.isValid("(]") is False
    assert sol.isValid("([{}])") is True
    assert sol.isValid("(") is False
    print("✅ All Valid Parentheses tests passed!")
