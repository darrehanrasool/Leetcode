#!/usr/bin/env python3
"""
Generator script for Batch 2:
- Stack
- Monotonic Stack
- Queue
- Monotonic Queue
- Linked List
- Doubly-Linked List
"""

import os

def create_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Created: {path}")

# =====================================================================
# 1. STACK
# =====================================================================

stack_readme = """# 🥞 Topic: Stack (Python DSA from Scratch)

## 🌟 1. Real-Life Analogy: What is a Stack?
Think of a **stack of plates in a cafeteria** or the **Undo (Ctrl+Z) button** in a text editor:
- **LIFO (Last-In, First-Out)**: The plate placed on top last is the first plate taken off.
- `push(x)`: Place plate on top ($O(1)$).
- `pop()`: Remove plate from top ($O(1)$).
- `peek()` / `top()`: Look at the top plate without removing it ($O(1)$).

## 🤖 2. Why AI Engineers Care
- **Call Stacks & Backpropagation**: Deep learning frameworks (PyTorch Autograd) use a reverse execution tape (a stack of operations) to compute gradients in reverse mode automatic differentiation!
- **Parsing Syntax & Prompts**: Evaluating mathematical expressions, AST parsing, and validating JSON / tool-calling schemas.

## 📚 Problems in this Directory
1. `01_Valid_Parentheses` (Easy - Google, Meta, Apple)
2. `02_Min_Stack` (Medium - Amazon, Bloomberg, Meta)
3. `03_Evaluate_Reverse_Polish_Notation` (Medium - Google, LinkedIn)
"""

st_p1_prob = """# 📖 Valid Parentheses (LeetCode #20)

- **Difficulty**: Easy
- **Asked By**: Meta (Facebook - Top 5), Google, Amazon, Microsoft
- **Frequency**: ⭐⭐⭐⭐⭐

## 💡 Real-Life Analogy
Nesting Russian dolls or opening and closing quotation marks in English:
Every time you open an outer bracket `(`, you must close it with matching `)`.
If you open an inner bracket `[`, you must close the inner bracket `]` *before* you can close the outer `)`.
The last bracket opened must be the first bracket closed!

## 📋 Problem Statement
Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

### Examples
- **Input**: `s = "()[]{}"` -> `true`
- **Input**: `s = "(]"` -> `false`
- **Input**: `s = "([{}])"` -> `true`
"""

st_p1_sol_md = """# 💡 Valid Parentheses - Solution Deep Dive

## 🧠 Thought Process
Use a stack and a dictionary mapping closing brackets to their matching opening brackets:
`matching = {')': '(', '}': '{', ']': '['}`
- For each character `char` in `s`:
  - If `char in matching` (it's a closing bracket):
    - Pop the top of the stack (if empty, assign a dummy mismatch).
    - If popped element doesn't match `matching[char]`, return `False`.
  - Else (it's an opening bracket):
    - Push onto stack.
- After loop, return `True` only if stack is empty!

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N)$
- **Space Complexity**: $O(N)$
"""

st_p1_sol_py = '''"""
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
'''

st_p2_prob = """# 📖 Min Stack (LeetCode #155)

- **Difficulty**: Medium
- **Asked By**: Amazon, Bloomberg, Meta, Microsoft
- **Frequency**: ⭐⭐⭐⭐⭐

## 💡 Real-Life Analogy
A stack of cards where every card also records the minimum card beneath it, so when someone asks "What is the minimum value in the deck?", you can answer in 1 second ($O(1)$) without searching through the deck!

## 📋 Problem Statement
Design a stack that supports `push`, `pop`, `top`, and retrieving the minimum element in **constant time $O(1)$**.
"""

st_p2_sol_md = """# 💡 Min Stack - Solution Deep Dive

## 🧠 Thought Process
Maintain two parallel stacks:
1. `stack`: normal values.
2. `min_stack`: keeps track of the current minimum up to that depth.
When pushing `x`, push `min(x, min_stack[-1])` to `min_stack`.
When popping, pop from both stacks.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(1)$ for all operations (`push`, `pop`, `top`, `getMin`).
- **Space Complexity**: $O(N)$ for the auxiliary min stack.
"""

st_p2_sol_py = '''"""
Problem: Min Stack (LeetCode #155)
Parallel Min-Tracking Stack
All operations in O(1) time
"""

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

if __name__ == "__main__":
    ms = MinStack()
    ms.push(-2)
    ms.push(0)
    ms.push(-3)
    assert ms.getMin() == -3
    ms.pop()
    assert ms.top() == 0
    assert ms.getMin() == -2
    print("✅ All Min Stack tests passed!")
'''

st_p3_prob = """# 📖 Evaluate Reverse Polish Notation (LeetCode #150)

- **Difficulty**: Medium
- **Asked By**: Google, LinkedIn, Amazon
- **Frequency**: ⭐⭐⭐⭐

## 💡 Real-Life Analogy
Post-fix calculator notation (used in compilers and HP scientific calculators):
`["2", "1", "+", "3", "*"]` -> `(2 + 1) * 3 = 9`.
When you read a number, push to stack. When you read an operator, pop two numbers, apply the operation, and push result back!
"""

st_p3_sol_md = """# 💡 Evaluate Reverse Polish Notation - Solution Deep Dive

## 🧠 Thought Process
Iterate through tokens:
- If operator (`+`, `-`, `*`, `/`):
  - Pop operand 2 (`b`), then operand 1 (`a`).
  - Compute result (note: integer division in Python truncates toward zero: `int(a / b)`).
  - Push result to stack.
- Else: push integer to stack.
Return final element of stack.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N)$
- **Space Complexity**: $O(N)$
"""

st_p3_sol_py = '''"""
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
'''

print("Writing Stack files...")
create_file("Stack/README.md", stack_readme)
create_file("Stack/01_Valid_Parentheses/problem.md", st_p1_prob)
create_file("Stack/01_Valid_Parentheses/solution.md", st_p1_sol_md)
create_file("Stack/01_Valid_Parentheses/solution.py", st_p1_sol_py)

create_file("Stack/02_Min_Stack/problem.md", st_p2_prob)
create_file("Stack/02_Min_Stack/solution.md", st_p2_sol_md)
create_file("Stack/02_Min_Stack/solution.py", st_p2_sol_py)

create_file("Stack/03_Evaluate_Reverse_Polish_Notation/problem.md", st_p3_prob)
create_file("Stack/03_Evaluate_Reverse_Polish_Notation/solution.md", st_p3_sol_md)
create_file("Stack/03_Evaluate_Reverse_Polish_Notation/solution.py", st_p3_sol_py)

# =====================================================================
# 2. MONOTONIC STACK
# =====================================================================

mono_stack_readme = """# 🪜 Topic: Monotonic Stack (Python DSA from Scratch)

## 🌟 1. Real-Life Analogy: What is a Monotonic Stack?
Imagine a line of people waiting for a movie, where taller people block the view of shorter people behind them.
A **Monotonic Stack** maintains its elements strictly in increasing or decreasing order.
When a new element arrives, we pop all elements that violate the order.
This allows us to find the **Next Greater Element** or **Previous Smaller Element** for every item in $O(N)$ time instead of $O(N^2)$!

## 🤖 2. Why AI Engineers Care
- **Span Extraction & Histogram Segmentation**: Finding bounding extents in rasterized image masks.
- **Stock & Metric Volatility Breakthroughs**: Detecting the exact breakout timestamps in financial time-series.

## 📚 Problems in this Directory
1. `01_Daily_Temperatures` (Medium - Meta, Google, Amazon)
2. `02_Largest_Rectangle_in_Histogram` (Hard - Google, Meta, Microsoft)
"""

ms_p1_prob = """# 📖 Daily Temperatures (LeetCode #739)

- **Difficulty**: Medium
- **Asked By**: Meta, Google, Amazon
- **Frequency**: ⭐⭐⭐⭐⭐

## 💡 Real-Life Analogy
Looking at the weather forecast: for each day, how many days must you wait until a warmer day arrives?
`temperatures = [73, 74, 75, 71, 69, 72, 76, 73]`
Using a monotonic decreasing stack, colder days wait on the stack until a warmer day arrives and resolves all of them at once!

## 📋 Problem Statement
Given an array of integers `temperatures` represents the daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the `i`-th day to get a warmer temperature. If there is no future day for which this is possible, keep `answer[i] == 0` instead.
"""

ms_p1_sol_md = """# 💡 Daily Temperatures - Solution Deep Dive

## 🧠 Thought Process
Maintain a stack of indices `stack` where temperatures are strictly decreasing.
For each day `curr_day, curr_temp`:
- While stack is non-empty and `curr_temp > temperatures[stack[-1]]`:
  - `prev_day = stack.pop()`
  - `answer[prev_day] = curr_day - prev_day`
- Push `curr_day` onto stack.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N)$ — Each index pushed and popped at most once.
- **Space Complexity**: $O(N)$ for stack.
"""

ms_p1_sol_py = '''"""
Problem: Daily Temperatures (LeetCode #739)
Monotonic Decreasing Stack
Time Complexity: O(N)
Space Complexity: O(N)
"""

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []  # Stores indices of temperatures

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev_idx = stack.pop()
                res[prev_idx] = i - prev_idx
            stack.append(i)

        return res

if __name__ == "__main__":
    sol = Solution()
    assert sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
    assert sol.dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
    assert sol.dailyTemperatures([30, 60, 90]) == [1, 1, 0]
    print("✅ All Daily Temperatures tests passed!")
'''

ms_p2_prob = """# 📖 Largest Rectangle in Histogram (LeetCode #84)

- **Difficulty**: Hard
- **Asked By**: Google, Meta, Amazon, Microsoft
- **Frequency**: ⭐⭐⭐⭐⭐

## 💡 Real-Life Analogy
Finding the largest billboard that can fit on a skyline of buildings with varying heights.
A building's height can extend left and right until it hits a shorter building!
"""

ms_p2_sol_md = """# 💡 Largest Rectangle in Histogram - Solution Deep Dive

## 🧠 Thought Process
Monotonic increasing stack of `(index, height)`:
When we see a bar shorter than the top of stack, the taller bar cannot extend any further to the right!
We pop the taller bar, calculate its maximum area rectangle, and record that the new shorter bar could actually extend backwards to where the popped bar started.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N)$
- **Space Complexity**: $O(N)$
"""

ms_p2_sol_py = '''"""
Problem: Largest Rectangle in Histogram (LeetCode #84)
Monotonic Increasing Stack
Time Complexity: O(N)
Space Complexity: O(N)
"""

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []  # pair: (start_index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                max_area = max(max_area, height * (i - idx))
                start = idx
            stack.append((start, h))

        # Check remaining elements extending to end of array
        for idx, height in stack:
            max_area = max(max_area, height * (len(heights) - idx))

        return max_area

if __name__ == "__main__":
    sol = Solution()
    assert sol.largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10
    assert sol.largestRectangleArea([2, 4]) == 4
    print("✅ All Largest Rectangle in Histogram tests passed!")
'''

print("Writing Monotonic Stack files...")
create_file("Monotonic Stack/README.md", mono_stack_readme)
create_file("Monotonic Stack/01_Daily_Temperatures/problem.md", ms_p1_prob)
create_file("Monotonic Stack/01_Daily_Temperatures/solution.md", ms_p1_sol_md)
create_file("Monotonic Stack/01_Daily_Temperatures/solution.py", ms_p1_sol_py)

create_file("Monotonic Stack/02_Largest_Rectangle_in_Histogram/problem.md", ms_p2_prob)
create_file("Monotonic Stack/02_Largest_Rectangle_in_Histogram/solution.md", ms_p2_sol_md)
create_file("Monotonic Stack/02_Largest_Rectangle_in_Histogram/solution.py", ms_p2_sol_py)

# =====================================================================
# 3. QUEUE & MONOTONIC QUEUE
# =====================================================================

queue_readme = """# 🚶 Topic: Queue & Monotonic Queue (Python DSA from Scratch)

## 🌟 1. Real-Life Analogy: What is a Queue?
A **checkout line at a supermarket**:
- **FIFO (First-In, First-Out)**: The first person in line is the first person served.
- `enqueue()`: Enter at the back.
- `dequeue()`: Exit from the front.

A **Monotonic Queue** maintains elements in monotonic order while supporting fast removal of elements outside an active sliding window.

## 🤖 2. Why AI Engineers Care
- **BFS (Breadth-First Search)**: Shortest path routing in graphs and search trees.
- **Asynchronous Task Workers & Message Brokers**: RabbitMQ, Celery, and Kafka pipelines consume tasks in FIFO queues.

## 📚 Problems in this Directory
1. `Queue/01_Implement_Queue_using_Stacks` (Easy - Amazon, Microsoft)
2. `Monotonic Queue/01_Sliding_Window_Maximum` (Hard - Google, Amazon, Meta)
"""

q_p1_prob = """# 📖 Implement Queue using Stacks (LeetCode #232)

- **Difficulty**: Easy
- **Asked By**: Amazon, Microsoft, Apple
- **Frequency**: ⭐⭐⭐⭐

## 📋 Problem Statement
Implement a first in first out (FIFO) queue using only two stacks.
Supported operations: `push(x)`, `pop()`, `peek()`, `empty()`.
"""

q_p1_sol_md = """# 💡 Implement Queue using Stacks - Solution Deep Dive

## 🧠 Thought Process
Use two stacks:
- `in_stack`: handles incoming `push(x)`.
- `out_stack`: handles `pop()` and `peek()`.
When `out_stack` is empty, transfer all elements from `in_stack` to `out_stack`. This naturally reverses the order, turning LIFO into FIFO!

## ⏱️ Complexity Analysis
- **Amortized Time Complexity**: $O(1)$ per operation.
- **Space Complexity**: $O(N)$ to store elements.
"""

q_p1_sol_py = '''"""
Problem: Implement Queue using Stacks (LeetCode #232)
Two-Stack FIFO Emulation
Amortized O(1) Time per operation
"""

class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self.peek()
        return self.out_stack.pop()

    def peek(self) -> int:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack

if __name__ == "__main__":
    q = MyQueue()
    q.push(1)
    q.push(2)
    assert q.peek() == 1
    assert q.pop() == 1
    assert q.empty() is False
    assert q.pop() == 2
    assert q.empty() is True
    print("✅ All Implement Queue using Stacks tests passed!")
'''

mq_p1_prob = """# 📖 Sliding Window Maximum (LeetCode #239)

- **Difficulty**: Hard
- **Asked By**: Google, Amazon, Meta, Citadel
- **Frequency**: ⭐⭐⭐⭐⭐

## 💡 Real-Life Analogy
A sliding scoreboard showing the highest temperature over the last $K$ hours.
A new high temperature immediately renders all smaller past temperatures irrelevant because they are both older and smaller!

## 📋 Problem Statement
You are given an array of integers `nums`, there is a sliding window of size `k` which is moving from the very left of the array to the very right.
Return the max sliding window.
"""

mq_p1_sol_md = """# 💡 Sliding Window Maximum - Solution Deep Dive

## 🧠 Thought Process
Use a deque (monotonic decreasing queue of indices):
1. Remove indices from front if they fall outside the current window (`i - k`).
2. Remove elements from back of deque that are smaller than `nums[i]` (they can never be the maximum again).
3. Append `i` to deque.
4. If `i >= k - 1`, record `nums[deque[0]]` as the window max.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N)$ — Every element added and removed from deque at most once.
- **Space Complexity**: $O(K)$ for the deque.
"""

mq_p1_sol_py = '''"""
Problem: Sliding Window Maximum (LeetCode #239)
Monotonic Deque Approach
Time Complexity: O(N)
Space Complexity: O(K)
"""

from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()  # stores indices
        res = []

        for i, num in enumerate(nums):
            # Remove indices that are out of the active window
            while q and q[0] < i - k + 1:
                q.popleft()

            # Remove smaller elements from back
            while q and nums[q[-1]] < num:
                q.pop()

            q.append(i)

            # Record max once window reaches size k
            if i >= k - 1:
                res.append(nums[q[0]])

        return res

if __name__ == "__main__":
    sol = Solution()
    assert sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]
    assert sol.maxSlidingWindow([1], 1) == [1]
    print("✅ All Sliding Window Maximum tests passed!")
'''

print("Writing Queue & Monotonic Queue files...")
create_file("Queue/README.md", queue_readme)
create_file("Queue/01_Implement_Queue_using_Stacks/problem.md", q_p1_prob)
create_file("Queue/01_Implement_Queue_using_Stacks/solution.md", q_p1_sol_md)
create_file("Queue/01_Implement_Queue_using_Stacks/solution.py", q_p1_sol_py)

create_file("Monotonic Queue/README.md", queue_readme)
create_file("Monotonic Queue/01_Sliding_Window_Maximum/problem.md", mq_p1_prob)
create_file("Monotonic Queue/01_Sliding_Window_Maximum/solution.md", mq_p1_sol_md)
create_file("Monotonic Queue/01_Sliding_Window_Maximum/solution.py", mq_p1_sol_py)

# =====================================================================
# 4. LINKED LIST & DOUBLY-LINKED LIST
# =====================================================================

ll_readme = """# 🔗 Topic: Linked List & Doubly-Linked List (Python DSA from Scratch)

## 🌟 1. Real-Life Analogy: What is a Linked List?
Imagine a **treasure hunt**:
- Each clue card has two things:
  1. A prize/clue (Value).
  2. The GPS address of the next clue card (Next Pointer).
Unlike an array, elements are not stored contiguously in memory; they can be scattered all across RAM!
- In a **Singly Linked List**, each node points to `next`.
- In a **Doubly Linked List**, each node points to both `next` and `prev`.

## 🤖 2. Why AI Engineers Care
- **LRU (Least Recently Used) Cache**: PyTorch, HuggingFace, and vLLM KV-cache managers use Doubly-Linked Lists combined with Hash Maps for $O(1)$ eviction of cached keys/values!
- **Dynamic Memory Allocation**: Operating system allocators (like `malloc` and CUDA memory pools) track free memory blocks using doubly linked lists.

## 📚 Problems in this Directory
1. `01_Reverse_Linked_List` (Easy - Google, Meta, Amazon)
2. `02_Merge_Two_Sorted_Lists` (Easy - Meta, Amazon, Apple)
3. `03_Linked_List_Cycle` (Easy - Amazon, Microsoft)
4. `04_LRU_Cache` (Medium - Google, Meta #1 system/DSA hybrid)
"""

ll_p1_prob = """# 📖 Reverse Linked List (LeetCode #206)

- **Difficulty**: Easy
- **Asked By**: Google, Meta, Amazon, Apple
- **Frequency**: ⭐⭐⭐⭐⭐

## 💡 Real-Life Analogy
Reversing one-way train track switches or flipping arrows on a treasure map so they lead backwards from the chest to the starting ship.

## 📋 Problem Statement
Given the `head` of a singly linked list, reverse the list, and return the reversed list.
"""

ll_p1_sol_md = """# 💡 Reverse Linked List - Solution Deep Dive

## 🧠 Thought Process
Use three pointers: `prev`, `curr`, `nxt`:
- `prev = None`
- `curr = head`
While `curr`:
- Save `nxt = curr.next`
- Reverse pointer: `curr.next = prev`
- Advance: `prev = curr`, `curr = nxt`
Return `prev` (new head).

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N)$
- **Space Complexity**: $O(1)$ in-place.
"""

ll_p1_sol_py = '''"""
Problem: Reverse Linked List (LeetCode #206)
Iterative Three-Pointer Reversal
Time Complexity: O(N)
Space Complexity: O(1)
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

def to_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

def from_list(vals):
    dummy = ListNode(0)
    curr = dummy
    for v in vals:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

if __name__ == "__main__":
    sol = Solution()
    ll = from_list([1, 2, 3, 4, 5])
    rev = sol.reverseList(ll)
    assert to_list(rev) == [5, 4, 3, 2, 1]
    print("✅ All Reverse Linked List tests passed!")
'''

ll_p2_prob = """# 📖 Merge Two Sorted Lists (LeetCode #21)

- **Difficulty**: Easy
- **Asked By**: Meta, Amazon, Apple, Microsoft
- **Frequency**: ⭐⭐⭐⭐⭐

## 📋 Problem Statement
You are given the heads of two sorted linked lists `list1` and `list2`.
Merge the two lists into one sorted list by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
"""

ll_p2_sol_md = """# 💡 Merge Two Sorted Lists - Solution Deep Dive

## 🧠 Thought Process
Use a dummy head node.
Compare `list1.val` and `list2.val`:
- Attach smaller node to `curr.next`.
- Advance whichever list had the smaller node.
Attach remaining nodes at the end.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(M + N)$
- **Space Complexity**: $O(1)$ in-place pointer splicing.
"""

ll_p2_sol_py = '''"""
Problem: Merge Two Sorted Lists (LeetCode #21)
Dummy Head Splice
Time Complexity: O(M + N)
Space Complexity: O(1)
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 if list1 else list2
        return dummy.next

def to_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

def from_list(vals):
    dummy = ListNode(0)
    curr = dummy
    for v in vals:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

if __name__ == "__main__":
    sol = Solution()
    l1 = from_list([1, 2, 4])
    l2 = from_list([1, 3, 4])
    merged = sol.mergeTwoLists(l1, l2)
    assert to_list(merged) == [1, 1, 2, 3, 4, 4]
    print("✅ All Merge Two Sorted Lists tests passed!")
'''

ll_p3_prob = """# 📖 Linked List Cycle (LeetCode #141)

- **Difficulty**: Easy
- **Asked By**: Amazon, Microsoft, Meta
- **Frequency**: ⭐⭐⭐⭐⭐

## 💡 Real-Life Analogy
Floyd's Tortoise and Hare algorithm:
Two runners running around a circular track: if there is a loop, the faster runner will eventually lap and collide with the slower runner!
"""

ll_p3_sol_md = """# 💡 Linked List Cycle - Solution Deep Dive

## 🧠 Thought Process
- `slow` advances 1 step at a time: `slow = slow.next`
- `fast` advances 2 steps at a time: `fast = fast.next.next`
- If `fast` meets `slow`, a cycle exists!
- If `fast` reaches `None`, no cycle exists.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N)$
- **Space Complexity**: $O(1)$
"""

ll_p3_sol_py = '''"""
Problem: Linked List Cycle (LeetCode #141)
Floyd\'s Cycle-Finding Algorithm (Tortoise & Hare)
Time Complexity: O(N)
Space Complexity: O(1)
"""

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

if __name__ == "__main__":
    sol = Solution()
    n1 = ListNode(3)
    n2 = ListNode(2)
    n3 = ListNode(0)
    n4 = ListNode(-4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2  # cycle back to n2
    assert sol.hasCycle(n1) is True

    n_linear = ListNode(1)
    n_linear.next = ListNode(2)
    assert sol.hasCycle(n_linear) is False
    print("✅ All Linked List Cycle tests passed!")
'''

ll_p4_prob = """# 📖 LRU Cache (LeetCode #146)

- **Difficulty**: Medium
- **Asked By**: Google, Meta (#1 most asked system-DSA hybrid), Amazon, OpenAI
- **Frequency**: ⭐⭐⭐⭐⭐

## 💡 Real-Life Analogy
A smartphone screen showing the 3 most recently used apps.
When you open an app, it jumps to the front.
When you open a brand new app when the screen is full, the least recently used app is evicted!

## 📋 Problem Statement
Design a data structure that follows the constraints of a **Least Recently Used (LRU) cache**.
Implement the `LRUCache` class:
- `LRUCache(int capacity)`
- `get(int key)`: Return value if exists, else -1.
- `put(int key, int value)`: Update or insert. Evict LRU if capacity exceeded.
Both `get` and `put` must run in **$O(1)$ average time**.
"""

ll_p4_sol_md = """# 💡 LRU Cache - Solution Deep Dive

## 🧠 Architecture
- **Hash Map**: Maps `key -> Node` for $O(1)$ lookups.
- **Doubly-Linked List**: Maintains access order with dummy `head` (Least Recently Used) and dummy `tail` (Most Recently Used).
- Moving a node to MRU or removing LRU node is $O(1)$ pointer manipulation.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(1)$ for both `get` and `put`.
- **Space Complexity**: $O(\\text{capacity})$.
"""

ll_p4_sol_py = '''"""
Problem: LRU Cache (LeetCode #146)
Hash Map + Doubly-Linked List
Time Complexity: O(1) for both get and put
Space Complexity: O(capacity)
"""

class Node:
    def __init__(self, key: int = 0, val: int = 0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # key -> Node

        # Dummy head (LRU side) and dummy tail (MRU side)
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _insert(self, node: Node) -> None:
        # Insert before tail (as most recently used)
        p = self.tail.prev
        p.next = node
        node.prev = p
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self._insert(node)

        if len(self.cache) > self.cap:
            # Evict LRU from head
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]

if __name__ == "__main__":
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    assert lru.get(1) == 1
    lru.put(3, 3)  # evicts key 2
    assert lru.get(2) == -1
    lru.put(4, 4)  # evicts key 1
    assert lru.get(1) == -1
    assert lru.get(3) == 3
    assert lru.get(4) == 4
    print("✅ All LRU Cache tests passed!")
'''

print("Writing Linked List & Doubly-Linked List files...")
create_file("Linked List/README.md", ll_readme)
create_file("Linked List/01_Reverse_Linked_List/problem.md", ll_p1_prob)
create_file("Linked List/01_Reverse_Linked_List/solution.md", ll_p1_sol_md)
create_file("Linked List/01_Reverse_Linked_List/solution.py", ll_p1_sol_py)

create_file("Linked List/02_Merge_Two_Sorted_Lists/problem.md", ll_p2_prob)
create_file("Linked List/02_Merge_Two_Sorted_Lists/solution.md", ll_p2_sol_md)
create_file("Linked List/02_Merge_Two_Sorted_Lists/solution.py", ll_p2_sol_py)

create_file("Linked List/03_Linked_List_Cycle/problem.md", ll_p3_prob)
create_file("Linked List/03_Linked_List_Cycle/solution.md", ll_p3_sol_md)
create_file("Linked List/03_Linked_List_Cycle/solution.py", ll_p3_sol_py)

create_file("Linked List/04_LRU_Cache/problem.md", ll_p4_prob)
create_file("Linked List/04_LRU_Cache/solution.md", ll_p4_sol_md)
create_file("Linked List/04_LRU_Cache/solution.py", ll_p4_sol_py)

create_file("Doubly-Linked List/README.md", ll_readme)
create_file("Doubly-Linked List/01_LRU_Cache/problem.md", ll_p4_prob)
create_file("Doubly-Linked List/01_LRU_Cache/solution.md", ll_p4_sol_md)
create_file("Doubly-Linked List/01_LRU_Cache/solution.py", ll_p4_sol_py)

print("Batch 2 generated successfully!")
