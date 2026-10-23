#!/usr/bin/env python3
"""
Generator script for Batch 3:
- Binary Search
- Tree & Binary Tree
- Binary Search Tree
- Heap (Priority Queue)
- Trie
"""

import os

def create_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Created: {path}")

# =====================================================================
# 1. BINARY SEARCH
# =====================================================================

bs_readme = """# 🎯 Topic: Binary Search (Python DSA from Scratch)

## 🌟 1. Real-Life Analogy: What is Binary Search?
Looking up a word in a **printed physical dictionary** (e.g. 100,000 words):
You don't start at page 1 reading word by word.
You open the exact middle of the book.
- If your word starts with 'M' and you see 'T', you tear the entire right half of the book away!
- In just **17 page flips**, you can find any single word in a 100,000-page book ($2^{17} > 100,000$)!
This is **$O(\\log N)$ logarithmic time**.

## 🤖 2. Why AI Engineers Care
- **Binary Search on the Answer Range**: Hyperparameter optimization, finding learning rate boundaries, or determining minimum GPU batch sizes before Out-Of-Memory (OOM).
- **Quantization & Threshold Tuning**: Finding the exact classification threshold to meet a target false positive rate (Precision-Recall curve search).

## 📚 Problems in this Directory
1. `01_Binary_Search` (Easy - Google, Meta)
2. `02_Search_in_Rotated_Sorted_Array` (Medium - Meta, Google, Amazon)
3. `03_Find_Minimum_in_Rotated_Sorted_Array` (Medium - Amazon, Microsoft)
4. `04_Koko_Eating_Bananas` (Medium - Google, Airbnb - Binary Search on Answer)
"""

bs_p1_prob = """# 📖 Binary Search (LeetCode #704)

- **Difficulty**: Easy
- **Asked By**: Google, Meta, Apple
- **Frequency**: ⭐⭐⭐⭐⭐

## 📋 Problem Statement
Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.
Must write an algorithm with **$O(\\log N)$ runtime complexity**.
"""

bs_p1_sol_md = """# 💡 Binary Search - Solution Deep Dive

## 🧠 Thought Process
Maintain search interval `[low, high]`:
- `mid = low + (high - low) // 2` (avoids 32-bit integer overflow).
- If `nums[mid] == target`: found!
- If `nums[mid] < target`: target is in right half $\\rightarrow$ `low = mid + 1`.
- If `nums[mid] > target`: target is in left half $\\rightarrow$ `high = mid - 1`.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(\\log N)$
- **Space Complexity**: $O(1)$
"""

bs_p1_sol_py = '''"""
Problem: Binary Search (LeetCode #704)
Classic Iterative Binary Search
Time Complexity: O(log N)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1

if __name__ == "__main__":
    sol = Solution()
    assert sol.search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert sol.search([-1, 0, 3, 5, 9, 12], 2) == -1
    print("✅ All Binary Search tests passed!")
'''

bs_p2_prob = """# 📖 Search in Rotated Sorted Array (LeetCode #33)

- **Difficulty**: Medium
- **Asked By**: Meta, Google, Amazon, Microsoft
- **Frequency**: ⭐⭐⭐⭐⭐

## 💡 Real-Life Analogy
A dictionary that was cut in half and swapped: `[4, 5, 6, 7, 0, 1, 2]`.
Even though it is rotated, **at least one half (left or right) is ALWAYS normally sorted!**
We inspect which half is normally sorted and check if our target falls inside that sorted range.
"""

bs_p2_sol_md = """# 💡 Search in Rotated Sorted Array - Solution Deep Dive

## 🧠 Thought Process
At index `mid`:
1. Check if `nums[low] <= nums[mid]` (Left half is sorted):
   - If `nums[low] <= target < nums[mid]`: target is in left half $\\rightarrow$ `high = mid - 1`.
   - Else: search right half $\\rightarrow$ `low = mid + 1`.
2. Else (Right half is sorted):
   - If `nums[mid] < target <= nums[high]`: target is in right half $\\rightarrow$ `low = mid + 1`.
   - Else: search left half $\\rightarrow$ `high = mid - 1`.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(\\log N)$
- **Space Complexity**: $O(1)$
"""

bs_p2_sol_py = '''"""
Problem: Search in Rotated Sorted Array (LeetCode #33)
Modified Binary Search
Time Complexity: O(log N)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return mid

            # Check if left half is normally sorted
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            # Otherwise, right half must be normally sorted
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1

if __name__ == "__main__":
    sol = Solution()
    assert sol.search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert sol.search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert sol.search([1], 0) == -1
    print("✅ All Search in Rotated Sorted Array tests passed!")
'''

bs_p3_prob = """# 📖 Find Minimum in Rotated Sorted Array (LeetCode #153)

- **Difficulty**: Medium
- **Asked By**: Amazon, Microsoft, Meta
- **Frequency**: ⭐⭐⭐⭐⭐

## 📋 Problem Statement
Given the sorted rotated array `nums` of unique elements, return the **minimum element** of this array in $O(\\log N)$ time.
"""

bs_p3_sol_md = """# 💡 Find Minimum in Rotated Sorted Array - Solution Deep Dive

## 🧠 Thought Process
Compare `nums[mid]` with `nums[high]`:
- If `nums[mid] > nums[high]`: The inflection pivot (minimum) must be strictly in the right half $\\rightarrow$ `low = mid + 1`.
- If `nums[mid] <= nums[high]`: `mid` could be the minimum, or the minimum is in the left half $\\rightarrow$ `high = mid`.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(\\log N)$
- **Space Complexity**: $O(1)$
"""

bs_p3_sol_py = '''"""
Problem: Find Minimum in Rotated Sorted Array (LeetCode #153)
Binary Search for Pivot Inflection
Time Complexity: O(log N)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1

        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid

        return nums[low]

if __name__ == "__main__":
    sol = Solution()
    assert sol.findMin([3, 4, 5, 1, 2]) == 1
    assert sol.findMin([4, 5, 6, 7, 0, 1, 2]) == 0
    assert sol.findMin([11, 13, 15, 17]) == 11
    print("✅ All Find Minimum in Rotated Sorted Array tests passed!")
'''

bs_p4_prob = """# 📖 Koko Eating Bananas (LeetCode #875)

- **Difficulty**: Medium
- **Asked By**: Google, Airbnb, Meta
- **Frequency**: ⭐⭐⭐⭐⭐ (The canonical Binary Search on the Answer problem)

## 💡 Real-Life Analogy
Finding the minimum download bandwidth speed $K$ required to finish downloading all training dataset files before a deadline $H$.
- Speed can range between $1$ (slowest) and $\\max(\\text{piles})$ (fastest).
- If speed $K$ finishes in time, test if a slower speed also works!
"""

bs_p4_sol_md = """# 💡 Koko Eating Bananas - Solution Deep Dive

## 🧠 Thought Process (Binary Search on Answer Space)
- Range of possible speeds: `low = 1`, `high = max(piles)`.
- Helper function `can_finish(speed)`:
  $$\\text{hours} = \\sum \\lceil \\text{pile} / \\text{speed} \\rceil$$
- If `hours <= h`: try slower speed $\\rightarrow$ `high = mid`.
- Else: too slow! Must eat faster $\\rightarrow$ `low = mid + 1`.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N \\log(\\max(piles)))$
- **Space Complexity**: $O(1)$
"""

bs_p4_sol_py = '''"""
Problem: Koko Eating Bananas (LeetCode #875)
Binary Search on Answer Range
Time Complexity: O(N log(max(P)))
Space Complexity: O(1)
"""

import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        while low < high:
            speed = low + (high - low) // 2

            # Total hours needed at this eating speed
            hours = sum(math.ceil(pile / speed) for pile in piles)

            if hours <= h:
                high = speed  # Could be optimal, or can eat slower
            else:
                low = speed + 1  # Too slow, must speed up

        return low

if __name__ == "__main__":
    sol = Solution()
    assert sol.minEatingSpeed([3, 6, 7, 11], 8) == 4
    assert sol.minEatingSpeed([30, 11, 23, 4, 20], 5) == 30
    assert sol.minEatingSpeed([30, 11, 23, 4, 20], 6) == 23
    print("✅ All Koko Eating Bananas tests passed!")
'''

print("Writing Binary Search files...")
create_file("Binary Search/README.md", bs_readme)
create_file("Binary Search/01_Binary_Search/problem.md", bs_p1_prob)
create_file("Binary Search/01_Binary_Search/solution.md", bs_p1_sol_md)
create_file("Binary Search/01_Binary_Search/solution.py", bs_p1_sol_py)

create_file("Binary Search/02_Search_in_Rotated_Sorted_Array/problem.md", bs_p2_prob)
create_file("Binary Search/02_Search_in_Rotated_Sorted_Array/solution.md", bs_p2_sol_md)
create_file("Binary Search/02_Search_in_Rotated_Sorted_Array/solution.py", bs_p2_sol_py)

create_file("Binary Search/03_Find_Minimum_in_Rotated_Sorted_Array/problem.md", bs_p3_prob)
create_file("Binary Search/03_Find_Minimum_in_Rotated_Sorted_Array/solution.md", bs_p3_sol_md)
create_file("Binary Search/03_Find_Minimum_in_Rotated_Sorted_Array/solution.py", bs_p3_sol_py)

create_file("Binary Search/04_Koko_Eating_Bananas/problem.md", bs_p4_prob)
create_file("Binary Search/04_Koko_Eating_Bananas/solution.md", bs_p4_sol_md)
create_file("Binary Search/04_Koko_Eating_Bananas/solution.py", bs_p4_sol_py)

# =====================================================================
# 2. TREE & BINARY TREE & BST
# =====================================================================

tree_readme = """# 🌳 Topic: Tree & Binary Tree & BST (Python DSA from Scratch)

## 🌟 1. Real-Life Analogy: What is a Tree?
A **corporate organizational chart**:
- The CEO is the **Root**.
- Vice Presidents are **Children**.
- Managers are **Internal Nodes**.
- Frontline individual contributors with no direct reports are **Leaves**.
A **Binary Tree** is where every node has at most two children (`left` and `right`).
A **Binary Search Tree (BST)** adds a golden property:
$$\\text{All nodes in Left subtree} < \\text{Current Node} < \\text{All nodes in Right subtree}$$

## 🤖 2. Why AI Engineers Care
- **Decision Trees, Random Forests, XGBoost, LightGBM**: The foundational non-neural machine learning models in tabular AI.
- **Search Trees in AlphaGo & MCTS (Monte Carlo Tree Search)**: Tree search enables LLM test-time reasoning and game evaluation.

## 📚 Problems in this Directory
1. `01_Maximum_Depth_of_Binary_Tree` (Easy - Google, Meta)
2. `02_Invert_Binary_Tree` (Easy - Google)
3. `03_Binary_Tree_Level_Order_Traversal` (Medium - Meta, Amazon)
4. `04_Lowest_Common_Ancestor` (Medium - Meta #1 asked, Google)
5. `05_Validate_Binary_Search_Tree` (Medium - Amazon, Bloomberg)
"""

tr_p1_prob = """# 📖 Maximum Depth of Binary Tree (LeetCode #104)

- **Difficulty**: Easy
- **Asked By**: Google, Meta, Apple
- **Frequency**: ⭐⭐⭐⭐⭐
"""

tr_p1_sol_md = """# 💡 Maximum Depth of Binary Tree - Solution Deep Dive

## 🧠 Thought Process (Recursion DFS)
The maximum depth of any tree is:
$$\\text{depth} = 1 + \\max(\\text{depth}(node.left), \\text{depth}(node.right))$$
Base case: `if not root: return 0`.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N)$
- **Space Complexity**: $O(H)$ where $H$ is tree height (recursion stack).
"""

tr_p1_sol_py = '''"""
Problem: Maximum Depth of Binary Tree (LeetCode #104)
DFS Recursion
Time Complexity: O(N)
Space Complexity: O(H)
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

if __name__ == "__main__":
    sol = Solution()
    # Tree: [3, 9, 20, None, None, 15, 7]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))
    assert sol.maxDepth(root) == 3
    print("✅ All Maximum Depth tests passed!")
'''

tr_p2_prob = """# 📖 Invert Binary Tree (LeetCode #226)

- **Difficulty**: Easy
- **Asked By**: Google, Meta, Amazon
- **Frequency**: ⭐⭐⭐⭐⭐ (The infamous Homebrew author interview problem)

## 💡 Real-Life Analogy
Looking at a tree in a mirror: every left branch becomes the right branch, recursively.
"""

tr_p2_sol_md = """# 💡 Invert Binary Tree - Solution Deep Dive

## 🧠 Thought Process
Swap `root.left` and `root.right`, then recursively invert both subtrees.
"""

tr_p2_sol_py = '''"""
Problem: Invert Binary Tree (LeetCode #226)
Recursive Mirror Swapping
Time Complexity: O(N)
Space Complexity: O(H)
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # Swap left and right children
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    inverted = sol.invertTree(root)
    assert inverted.val == 4
    assert inverted.left.val == 7
    assert inverted.right.val == 2
    print("✅ All Invert Binary Tree tests passed!")
'''

tr_p3_prob = """# 📖 Binary Tree Level Order Traversal (LeetCode #102)

- **Difficulty**: Medium
- **Asked By**: Meta, Amazon, Microsoft
- **Frequency**: ⭐⭐⭐⭐⭐ (The canonical Tree BFS problem)

## 💡 Real-Life Analogy
Taking a roll-call floor-by-floor in an office building:
Floor 1 (Root), then Floor 2, then Floor 3.
"""

tr_p3_sol_md = """# 💡 Binary Tree Level Order Traversal - Solution Deep Dive

## 🧠 Thought Process (BFS with Queue)
Use `collections.deque`:
For each level, record `len(queue)`. Pop that many nodes, record their values, and enqueue their children.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N)$
- **Space Complexity**: $O(N)$ (max width of tree).
"""

tr_p3_sol_py = '''"""
Problem: Binary Tree Level Order Traversal (LeetCode #102)
Queue-Based BFS Level Order
Time Complexity: O(N)
Space Complexity: O(N)
"""

from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        q = deque([root])

        while q:
            level_size = len(q)
            current_level = []

            for _ in range(level_size):
                node = q.popleft()
                current_level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(current_level)

        return res

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert sol.levelOrder(root) == [[3], [9, 20], [15, 7]]
    print("✅ All Level Order Traversal tests passed!")
'''

tr_p4_prob = """# 📖 Lowest Common Ancestor of a Binary Tree (LeetCode #236)

- **Difficulty**: Medium
- **Asked By**: Meta (Top 3 most asked), Google, Amazon
- **Frequency**: ⭐⭐⭐⭐⭐

## 💡 Real-Life Analogy
Looking at a family tree for two cousins: finding the closest shared grandparent!
"""

tr_p4_sol_md = """# 💡 Lowest Common Ancestor - Solution Deep Dive

## 🧠 Thought Process
Post-order DFS traversal:
- If current node is `p` or `q` or `None`, return `root`.
- Recurse on `left` and `right`.
- If both `left` and `right` return non-None, `root` is their Lowest Common Ancestor!
- Otherwise return whichever child returned non-None.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N)$
- **Space Complexity**: $O(H)$
"""

tr_p4_sol_py = '''"""
Problem: Lowest Common Ancestor of a Binary Tree (LeetCode #236)
Post-Order Recursive Search
Time Complexity: O(N)
Space Complexity: O(H)
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If p and q found in left and right subtrees, root is LCA
        if left and right:
            return root

        return left if left else right

if __name__ == "__main__":
    sol = Solution()
    r = TreeNode(3)
    p = TreeNode(5)
    q = TreeNode(1)
    r.left = p
    r.right = q
    assert sol.lowestCommonAncestor(r, p, q) == r
    print("✅ All Lowest Common Ancestor tests passed!")
'''

tr_p5_prob = """# 📖 Validate Binary Search Tree (LeetCode #98)

- **Difficulty**: Medium
- **Asked By**: Amazon, Bloomberg, Meta, Microsoft
- **Frequency**: ⭐⭐⭐⭐⭐

## 📋 Problem Statement
Given the `root` of a binary tree, determine if it is a valid binary search tree (BST).
"""

tr_p5_sol_md = """# 💡 Validate Binary Search Tree - Solution Deep Dive

## 🧠 Thought Process (Range Propagation)
Every node must be bounded by valid minimum and maximum thresholds:
- Root is bounded by `(-inf, +inf)`.
- Left child is bounded by `(min_val, root.val)`.
- Right child is bounded by `(root.val, max_val)`.
If any node violates its range, return `False`.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N)$
- **Space Complexity**: $O(H)$
"""

tr_p5_sol_py = '''"""
Problem: Validate Binary Search Tree (LeetCode #98)
Range Propagation DFS
Time Complexity: O(N)
Space Complexity: O(H)
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)

        return validate(root, float("-inf"), float("inf"))

if __name__ == "__main__":
    sol = Solution()
    t1 = TreeNode(2, TreeNode(1), TreeNode(3))
    t2 = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    assert sol.isValidBST(t1) is True
    assert sol.isValidBST(t2) is False
    print("✅ All Validate BST tests passed!")
'''

print("Writing Tree, Binary Tree, Binary Search Tree files...")
create_file("Tree/README.md", tree_readme)
create_file("Tree/01_Maximum_Depth_of_Binary_Tree/problem.md", tr_p1_prob)
create_file("Tree/01_Maximum_Depth_of_Binary_Tree/solution.md", tr_p1_sol_md)
create_file("Tree/01_Maximum_Depth_of_Binary_Tree/solution.py", tr_p1_sol_py)

create_file("Binary Tree/README.md", tree_readme)
create_file("Binary Tree/01_Invert_Binary_Tree/problem.md", tr_p2_prob)
create_file("Binary Tree/01_Invert_Binary_Tree/solution.md", tr_p2_sol_md)
create_file("Binary Tree/01_Invert_Binary_Tree/solution.py", tr_p2_sol_py)

create_file("Binary Tree/02_Binary_Tree_Level_Order_Traversal/problem.md", tr_p3_prob)
create_file("Binary Tree/02_Binary_Tree_Level_Order_Traversal/solution.md", tr_p3_sol_md)
create_file("Binary Tree/02_Binary_Tree_Level_Order_Traversal/solution.py", tr_p3_sol_py)

create_file("Binary Tree/03_Lowest_Common_Ancestor/problem.md", tr_p4_prob)
create_file("Binary Tree/03_Lowest_Common_Ancestor/solution.md", tr_p4_sol_md)
create_file("Binary Tree/03_Lowest_Common_Ancestor/solution.py", tr_p4_sol_py)

create_file("Binary Search Tree/README.md", tree_readme)
create_file("Binary Search Tree/01_Validate_Binary_Search_Tree/problem.md", tr_p5_prob)
create_file("Binary Search Tree/01_Validate_Binary_Search_Tree/solution.md", tr_p5_sol_md)
create_file("Binary Search Tree/01_Validate_Binary_Search_Tree/solution.py", tr_p5_sol_py)

# =====================================================================
# 3. HEAP (PRIORITY QUEUE)
# =====================================================================

heap_readme = """# 🏔️ Topic: Heap / Priority Queue (Python DSA from Scratch)

## 🌟 1. Real-Life Analogy: What is a Heap?
An **Emergency Room triage system**:
Patients don't see the doctor in order of arrival (FIFO). The patient with the most urgent condition (highest priority) is always treated first!
- **Min-Heap**: Smallest element is at the root ($O(1)$ lookup, $O(\\log K)$ insertion/removal).
- In Python: standard `heapq` module is a **Min-Heap**.

## 🤖 2. Why AI Engineers Care
- **Top-K Sampling & Beam Search in LLMs**: At every generation step, picking the top $K$ most probable next tokens uses a Min-Heap.
- **k-Nearest Neighbors (k-NN)**: Finding the closest vector embeddings to a query embedding.
- **Dijkstra's Algorithm & A* Search**: Path planning in robotics and gaming.

## 📚 Problems in this Directory
1. `01_Kth_Largest_Element_in_an_Array` (Medium - Meta, Amazon)
2. `02_Top_K_Frequent_Elements` (Medium - Meta, Google)
3. `03_Find_Median_from_Data_Stream` (Hard - Google, Amazon, Citadel)
"""

hp_p1_prob = """# 📖 Kth Largest Element in an Array (LeetCode #215)

- **Difficulty**: Medium
- **Asked By**: Meta (#1 asked), Amazon, Google
- **Frequency**: ⭐⭐⭐⭐⭐

## 📋 Problem Statement
Given an integer array `nums` and an integer `k`, return the `k`-th largest element in the array.
Must solve without sorting the entire array!
"""

hp_p1_sol_md = """# 💡 Kth Largest Element - Solution Deep Dive

## 🧠 Thought Process (Min-Heap of size K)
Maintain a min-heap of size $K$:
- For each `num` in `nums`:
  - `heappush(heap, num)`
  - If `len(heap) > k`: `heappop(heap)` (evicts the smallest).
After scanning all numbers, the root of the heap is the $K$-th largest element!

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N \\log K)$
- **Space Complexity**: $O(K)$
"""

hp_p1_sol_py = '''"""
Problem: Kth Largest Element in an Array (LeetCode #215)
Min-Heap of Size K
Time Complexity: O(N log K)
Space Complexity: O(K)
"""

import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]

if __name__ == "__main__":
    sol = Solution()
    assert sol.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
    assert sol.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    print("✅ All Kth Largest Element tests passed!")
'''

hp_p2_prob = """# 📖 Top K Frequent Elements (LeetCode #347)

- **Difficulty**: Medium
- **Asked By**: Meta, Google, Amazon
- **Frequency**: ⭐⭐⭐⭐⭐
"""

hp_p2_sol_md = """# 💡 Top K Frequent Elements - Solution Deep Dive

## 🧠 Thought Process
1. Count frequencies using `Counter(nums)`.
2. Push pairs `(count, num)` into a min-heap of size $K$.
3. Return all numbers remaining in the heap.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N \\log K)$
- **Space Complexity**: $O(N)$
"""

hp_p2_sol_py = '''"""
Problem: Top K Frequent Elements (LeetCode #347)
Frequency Map + Min-Heap
Time Complexity: O(N log K)
Space Complexity: O(N)
"""

from collections import Counter
import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        heap = []

        for num, freq in counts.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)

        return [num for freq, num in heap]

if __name__ == "__main__":
    sol = Solution()
    res = sol.topKFrequent([1, 1, 1, 2, 2, 3], 2)
    assert sorted(res) == [1, 2]
    print("✅ All Top K Frequent Elements tests passed!")
'''

hp_p3_prob = """# 📖 Find Median from Data Stream (LeetCode #295)

- **Difficulty**: Hard
- **Asked By**: Google, Amazon, Citadel, Meta
- **Frequency**: ⭐⭐⭐⭐⭐

## 💡 Real-Life Analogy
A balance scale:
- Left pan (Max-Heap): holds the smaller half of numbers.
- Right pan (Min-Heap): holds the larger half of numbers.
The median is always right at the fulcrum!
"""

hp_p3_sol_md = """# 💡 Find Median from Data Stream - Solution Deep Dive

## 🧠 Two-Heap Balance
- `small` (Max-heap, inverted signs in Python): holds smaller half.
- `large` (Min-heap): holds larger half.
Balance rule: `len(small)` equals `len(large)` or `len(large) + 1`.
Median is:
- `float(-small[0])` if odd number of elements.
- `(-small[0] + large[0]) / 2.0` if even.

## ⏱️ Complexity Analysis
- `addNum`: $O(\\log N)$
- `findMedian`: $O(1)$
- **Space Complexity**: $O(N)$
"""

hp_p3_sol_py = '''"""
Problem: Find Median from Data Stream (LeetCode #295)
Two-Heap (Max-Heap & Min-Heap) Dynamic Balancing
addNum: O(log N), findMedian: O(1)
"""

import heapq

class MedianFinder:
    def __init__(self):
        # small: max-heap (negated numbers)
        # large: min-heap
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        # Step 1: Push to max-heap
        heapq.heappush(self.small, -num)

        # Step 2: Ensure all elements in small <= large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Step 3: Size balancing (small can have at most 1 more element than large)
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0

if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    assert mf.findMedian() == 1.5
    mf.addNum(3)
    assert mf.findMedian() == 2.0
    print("✅ All Find Median from Data Stream tests passed!")
'''

print("Writing Heap files...")
create_file("Heap (Priority Queue)/README.md", heap_readme)
create_file("Heap (Priority Queue)/01_Kth_Largest_Element_in_an_Array/problem.md", hp_p1_prob)
create_file("Heap (Priority Queue)/01_Kth_Largest_Element_in_an_Array/solution.md", hp_p1_sol_md)
create_file("Heap (Priority Queue)/01_Kth_Largest_Element_in_an_Array/solution.py", hp_p1_sol_py)

create_file("Heap (Priority Queue)/02_Top_K_Frequent_Elements/problem.md", hp_p2_prob)
create_file("Heap (Priority Queue)/02_Top_K_Frequent_Elements/solution.md", hp_p2_sol_md)
create_file("Heap (Priority Queue)/02_Top_K_Frequent_Elements/solution.py", hp_p2_sol_py)

create_file("Heap (Priority Queue)/03_Find_Median_from_Data_Stream/problem.md", hp_p3_prob)
create_file("Heap (Priority Queue)/03_Find_Median_from_Data_Stream/solution.md", hp_p3_sol_md)
create_file("Heap (Priority Queue)/03_Find_Median_from_Data_Stream/solution.py", hp_p3_sol_py)

# =====================================================================
# 4. TRIE (PREFIX TREE)
# =====================================================================

trie_readme = """# 🌲 Topic: Trie (Prefix Tree) (Python DSA from Scratch)

## 🌟 1. Real-Life Analogy: What is a Trie?
**Search Autocomplete in Google Search**:
When you type `"app"`, Google instantly predicts `"apple"`, `"application"`, `"app store"`.
A Trie organizes words sharing prefixes in a tree where each branch is a letter.

## 🤖 2. Why AI Engineers Care
- **Byte-Pair Encoding (BPE) & LLM Tokenizers**: Hugging Face tokenizers (e.g. Tiktoken for GPT-4) use Trie structures to find the longest matching subword token in greedy tokenization!
- **Prompt Prefix Caching**: Radix trees / Tries are used in vLLM and SGLang for prefix caching of system prompts!

## 📚 Problems in this Directory
1. `01_Implement_Trie_Prefix_Tree` (Medium - Google, Amazon, Meta)
2. `02_Design_Add_and_Search_Words_Data_Structure` (Medium - Meta, Amazon)
"""

trie_p1_prob = """# 📖 Implement Trie (Prefix Tree) (LeetCode #208)

- **Difficulty**: Medium
- **Asked By**: Google, Amazon, Meta, Microsoft
- **Frequency**: ⭐⭐⭐⭐⭐

## 📋 Problem Statement
Implement a Trie with `insert`, `search`, and `startsWith` methods in $O(L)$ time where $L$ is word length.
"""

trie_p1_sol_md = """# 💡 Implement Trie - Solution Deep Dive

## 🧠 Thought Process
Each `TrieNode` has:
- `children`: dictionary mapping character to child `TrieNode`.
- `is_end_of_word`: boolean flag indicating if a word ends here.

## ⏱️ Complexity Analysis
- `insert`, `search`, `startsWith`: $O(L)$ time where $L$ is length of word.
- **Space Complexity**: $O(N \\cdot L)$ where $N$ is number of inserted words.
"""

trie_p1_sol_py = '''"""
Problem: Implement Trie (Prefix Tree) (LeetCode #208)
Standard Trie with TrieNode dictionary
Time Complexity: O(L) per operation
Space Complexity: O(N * L)
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end_of_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True

if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.search("app") is False
    assert trie.startsWith("app") is True
    trie.insert("app")
    assert trie.search("app") is True
    print("✅ All Implement Trie tests passed!")
'''

trie_p2_prob = """# 📖 Design Add and Search Words Data Structure (LeetCode #211)

- **Difficulty**: Medium
- **Asked By**: Meta, Amazon
- **Frequency**: ⭐⭐⭐⭐⭐
"""

trie_p2_sol_md = """# 💡 Design Add and Search Words - Solution Deep Dive

## 🧠 Thought Process
Trie with DFS backtracking for wildcard `.` matching:
If character is `.` (dot), we branch recursively into all available children at that node.
"""

trie_p2_sol_py = '''"""
Problem: Design Add and Search Words (LeetCode #211)
Trie with DFS Wildcard Backtracking
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_end = True

    def search(self, word: str) -> bool:
        def dfs(j, node):
            curr = node
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.is_end

        return dfs(0, self.root)

if __name__ == "__main__":
    wd = WordDictionary()
    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")
    assert wd.search("pad") is False
    assert wd.search("bad") is True
    assert wd.search(".ad") is True
    assert wd.search("b..") is True
    print("✅ All Design Add and Search Words tests passed!")
'''

print("Writing Trie files...")
create_file("Trie/README.md", trie_readme)
create_file("Trie/01_Implement_Trie_Prefix_Tree/problem.md", trie_p1_prob)
create_file("Trie/01_Implement_Trie_Prefix_Tree/solution.md", trie_p1_sol_md)
create_file("Trie/01_Implement_Trie_Prefix_Tree/solution.py", trie_p1_sol_py)

create_file("Trie/02_Design_Add_and_Search_Words_Data_Structure/problem.md", trie_p2_prob)
create_file("Trie/02_Design_Add_and_Search_Words_Data_Structure/solution.md", trie_p2_sol_md)
create_file("Trie/02_Design_Add_and_Search_Words_Data_Structure/solution.py", trie_p2_sol_py)

print("Batch 3 generated successfully!")
