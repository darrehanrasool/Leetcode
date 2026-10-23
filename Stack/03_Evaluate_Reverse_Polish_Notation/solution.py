"""
Problem: Evaluate Reverse Polish Notation (LeetCode #150)
Stack-Based Postfix Expression Evaluation
Time Complexity: O(N)
Space Complexity: O(N)
"""

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in "+-*/":
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    # Truncate toward zero
                    stack.append(int(a / b))
            else:
                stack.append(int(token))

        return stack[0]

if __name__ == "__main__":
    sol = Solution()
    assert sol.evalRPN(["2", "1", "+", "3", "*"]) == 9
    assert sol.evalRPN(["4", "13", "5", "/", "+"]) == 6
    assert sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) == 22
    print("✅ All Evaluate Reverse Polish Notation tests passed!")
