#!/usr/bin/env python3
"""
Generator script for Batch 4:
- Breadth-First Search
- Depth-First Search
- Graph
- Topological Sort
- Union Find
- Shortest Path
- Minimum Spanning Tree
- Eulerian Circuit
- Strongly Connected Component
"""

import os

def create_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Created: {path}")

# =====================================================================
# 1. BREADTH-FIRST SEARCH & DEPTH-FIRST SEARCH
# =====================================================================

bfs_readme = """# 🌐 Topic: Breadth-First Search & Depth-First Search (Python DSA from Scratch)

## 🌟 1. Real-Life Analogy
- **BFS (Breadth-First Search)**: Ripples expanding in a pond when a stone is dropped. Level-by-level exploration. Guarantees finding the **shortest path in unweighted graphs**!
- **DFS (Depth-First Search)**: Exploring a maze by following one path until you hit a dead end, then backtracking. Uses a call stack or recursion.

## 🤖 2. Why AI Engineers Care
- **PyTorch / TensorFlow Computation Graphs**: The forward and backward computation graph of a neural network is a Directed Acyclic Graph (DAG) traversed via DFS/Topological Sort.
- **Knowledge Graphs & Graph Neural Networks (GNNs)**: Message passing in GNNs aggregates features from 1-hop and 2-hop neighbor nodes via BFS expansion!

## 📚 Problems in this Directory
1. `Breadth-First Search/01_Rotting_Oranges` (Medium - Amazon, Google)
2. `Depth-First Search/01_Number_of_Islands` (Medium - Amazon #1, Meta, Google)
"""

bfs_p1_prob = """# 📖 Rotting Oranges (LeetCode #994)

- **Difficulty**: Medium
- **Asked By**: Amazon, Google, Microsoft, Meta
- **Frequency**: ⭐⭐⭐⭐⭐ (The canonical multi-source BFS problem)

## 💡 Real-Life Analogy
A contagious virus spreading: every minute, every infected person infects their adjacent neighbors.
Multi-source BFS starts with ALL initially infected people in the queue simultaneously!
"""

bfs_p1_sol_md = """# 💡 Rotting Oranges - Solution Deep Dive

## 🧠 Thought Process (Multi-Source BFS)
1. Count fresh oranges and add all rotten orange coordinates `(r, c)` to a queue.
2. If fresh == 0, return 0.
3. While queue and fresh > 0:
   - For each orange at current minute:
     - Check 4 neighbors (up, down, left, right).
     - If neighbor is fresh, rot it, decrement fresh, enqueue neighbor.
   - Increment minutes elapsed.
4. Return minutes if fresh == 0 else -1.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(M \\times N)$
- **Space Complexity**: $O(M \\times N)$
"""

bfs_p1_sol_py = '''"""
Problem: Rotting Oranges (LeetCode #994)
Multi-Source BFS
Time Complexity: O(M * N)
Space Complexity: O(M * N)
"""

from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        # Step 1: Scan grid for initial state
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        minutes = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Step 2: Multi-source BFS level by level
        while q and fresh > 0:
            minutes += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))

        return minutes if fresh == 0 else -1

if __name__ == "__main__":
    sol = Solution()
    assert sol.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]) == 4
    assert sol.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]) == -1
    assert sol.orangesRotting([[0,2]]) == 0
    print("✅ All Rotting Oranges tests passed!")
'''

dfs_p1_prob = """# 📖 Number of Islands (LeetCode #200)

- **Difficulty**: Medium
- **Asked By**: Amazon (#1 asked), Meta, Google, Microsoft, Apple
- **Frequency**: ⭐⭐⭐⭐⭐

## 💡 Real-Life Analogy
Satellite imaging: finding land masses surrounded by ocean.
When you spot a pixel of land `'1'`, you explore and sink all connected land pixels so you don't count the same island twice!
"""

dfs_p1_sol_md = """# 💡 Number of Islands - Solution Deep Dive

## 🧠 Thought Process (Flood Fill DFS)
Iterate through every cell `(r, c)`:
- If `grid[r][c] == '1'`:
  - Increment `islands_count`.
  - Trigger `dfs(r, c)` to sink/mark the entire island to `'0'`.
Return `islands_count`.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(M \\times N)$
- **Space Complexity**: $O(M \\times N)$ (worst case recursion stack).
"""

dfs_p1_sol_py = '''"""
Problem: Number of Islands (LeetCode #200)
Flood Fill DFS
Time Complexity: O(M * N)
Space Complexity: O(M * N)
"""

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
                return
            grid[r][c] = '0'  # Mark visited by sinking
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    dfs(r, c)

        return islands

if __name__ == "__main__":
    sol = Solution()
    g1 = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]
    assert sol.numIslands(g1) == 1

    g2 = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]
    assert sol.numIslands(g2) == 3
    print("✅ All Number of Islands tests passed!")
'''

print("Writing BFS & DFS files...")
create_file("Breadth-First Search/README.md", bfs_readme)
create_file("Breadth-First Search/01_Rotting_Oranges/problem.md", bfs_p1_prob)
create_file("Breadth-First Search/01_Rotting_Oranges/solution.md", bfs_p1_sol_md)
create_file("Breadth-First Search/01_Rotting_Oranges/solution.py", bfs_p1_sol_py)

create_file("Depth-First Search/README.md", bfs_readme)
create_file("Depth-First Search/01_Number_of_Islands/problem.md", dfs_p1_prob)
create_file("Depth-First Search/01_Number_of_Islands/solution.md", dfs_p1_sol_md)
create_file("Depth-First Search/01_Number_of_Islands/solution.py", dfs_p1_sol_py)

# =====================================================================
# 2. GRAPH & TOPOLOGICAL SORT
# =====================================================================

graph_readme = """# 🕸️ Topic: Graph & Topological Sort (Python DSA from Scratch)

## 🌟 1. Real-Life Analogy
- **Social Networks**: Users are Nodes, friendships are Edges.
- **Topological Sort**: College course prerequisites. You cannot take "Advanced Machine Learning" before "Linear Algebra" and "Calculus"!
  A topological sort produces a linear valid order of dependencies in a **Directed Acyclic Graph (DAG)**.

## 🤖 2. Why AI Engineers Care
- **Execution Ordering of PyTorch / ONNX Operators**: Deep learning models are serialized as DAGs of tensor ops. Compilers like TorchDynamo and TensorRT topologically sort nodes to schedule GPU kernel execution.
- **Cycle Detection**: Preventing deadlock loops in distributed training pipelines.

## 📚 Problems in this Directory
1. `Graph/01_Clone_Graph` (Medium - Meta, Google)
2. `Graph/02_Course_Schedule` (Medium - Google, Amazon, Meta)
3. `Topological Sort/01_Course_Schedule_II` (Medium - Google, Amazon, Meta)
"""

g_p1_prob = """# 📖 Clone Graph (LeetCode #133)

- **Difficulty**: Medium
- **Asked By**: Meta, Google, Amazon
- **Frequency**: ⭐⭐⭐⭐⭐

## 📋 Problem Statement
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph.
"""

g_p1_sol_md = """# 💡 Clone Graph - Solution Deep Dive

## 🧠 Thought Process
Use a hash map `old_to_new = {}` to map each original node to its newly cloned copy.
DFS traversal:
- If `node in old_to_new`: return `old_to_new[node]`.
- Create `copy = Node(node.val)`.
- Record `old_to_new[node] = copy`.
- For each neighbor, recursively clone and append to `copy.neighbors`.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(V + E)$
- **Space Complexity**: $O(V)$
"""

g_p1_sol_py = '''"""
Problem: Clone Graph (LeetCode #133)
DFS Hash Map Graph Deep Copy
Time Complexity: O(V + E)
Space Complexity: O(V)
"""

from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        old_to_new = {}

        def dfs(curr):
            if curr in old_to_new:
                return old_to_new[curr]

            copy = Node(curr.val)
            old_to_new[curr] = copy

            for nei in curr.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy

        return dfs(node)

if __name__ == "__main__":
    sol = Solution()
    n1 = Node(1)
    n2 = Node(2)
    n1.neighbors.append(n2)
    n2.neighbors.append(n1)
    cloned = sol.cloneGraph(n1)
    assert cloned.val == 1
    assert cloned.neighbors[0].val == 2
    assert cloned is not n1  # Must be a distinct deep copy object!
    print("✅ All Clone Graph tests passed!")
'''

g_p2_prob = """# 📖 Course Schedule (LeetCode #207)

- **Difficulty**: Medium
- **Asked By**: Google, Amazon, Meta, Microsoft
- **Frequency**: ⭐⭐⭐⭐⭐

## 📋 Problem Statement
There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [a, b]` indicates that you must take course `b` first if you want to take course `a`.
Return `true` if you can finish all courses. Otherwise, return `false` (i.e. check if a cycle exists in the dependency DAG).
"""

g_p2_sol_md = """# 💡 Course Schedule - Solution Deep Dive

## 🧠 Thought Process (Kahn's Algorithm - BFS In-Degree)
1. Build adjacency list `adj` and compute `in_degree` array for all courses.
2. Add all courses with `in_degree == 0` (no prerequisites needed) to a queue.
3. While queue:
   - Pop course, increment `taken_courses`.
   - For each neighbor, decrement its `in_degree`.
   - If neighbor's `in_degree == 0`, add to queue.
4. Return `taken_courses == numCourses`.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(V + E)$
- **Space Complexity**: $O(V + E)$
"""

g_p2_sol_py = '''"""
Problem: Course Schedule (LeetCode #207)
Kahn's In-Degree BFS Cycle Detection
Time Complexity: O(V + E)
Space Complexity: O(V + E)
"""

from collections import deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses

        for crs, pre in prerequisites:
            adj[pre].append(crs)
            in_degree[crs] += 1

        q = deque([i for i in range(numCourses) if in_degree[i] == 0])
        completed = 0

        while q:
            node = q.popleft()
            completed += 1
            for nei in adj[node]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)

        return completed == numCourses

if __name__ == "__main__":
    sol = Solution()
    assert sol.canFinish(2, [[1, 0]]) is True
    assert sol.canFinish(2, [[1, 0], [0, 1]]) is False  # Cycle!
    print("✅ All Course Schedule tests passed!")
'''

top_p1_prob = """# 📖 Course Schedule II (LeetCode #210)

- **Difficulty**: Medium
- **Asked By**: Google, Amazon, Meta
- **Frequency**: ⭐⭐⭐⭐⭐

## 📋 Problem Statement
Return the ordering of courses you should take to finish all courses. If impossible due to cycle, return an empty array `[]`.
"""

top_p1_sol_md = """# 💡 Course Schedule II - Solution Deep Dive

## 🧠 Thought Process (Topological Sort Order)
Identical to Kahn's algorithm, but record each course as it is popped from the queue into an `order` list!
"""

top_p1_sol_py = '''"""
Problem: Course Schedule II (LeetCode #210)
Kahn's Topological Sort Ordering
Time Complexity: O(V + E)
Space Complexity: O(V + E)
"""

from collections import deque
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses

        for crs, pre in prerequisites:
            adj[pre].append(crs)
            in_degree[crs] += 1

        q = deque([i for i in range(numCourses) if in_degree[i] == 0])
        order = []

        while q:
            node = q.popleft()
            order.append(node)
            for nei in adj[node]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)

        return order if len(order) == numCourses else []

if __name__ == "__main__":
    sol = Solution()
    assert sol.findOrder(2, [[1, 0]]) == [0, 1]
    assert sol.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]) in [[0, 1, 2, 3], [0, 2, 1, 3]]
    assert sol.findOrder(2, [[1, 0], [0, 1]]) == []
    print("✅ All Course Schedule II tests passed!")
'''

print("Writing Graph & Topological Sort files...")
create_file("Graph/README.md", graph_readme)
create_file("Graph/01_Clone_Graph/problem.md", g_p1_prob)
create_file("Graph/01_Clone_Graph/solution.md", g_p1_sol_md)
create_file("Graph/01_Clone_Graph/solution.py", g_p1_sol_py)

create_file("Graph/02_Course_Schedule/problem.md", g_p2_prob)
create_file("Graph/02_Course_Schedule/solution.md", g_p2_sol_md)
create_file("Graph/02_Course_Schedule/solution.py", g_p2_sol_py)

create_file("Topological Sort/README.md", graph_readme)
create_file("Topological Sort/01_Course_Schedule_II/problem.md", top_p1_prob)
create_file("Topological Sort/01_Course_Schedule_II/solution.md", top_p1_sol_md)
create_file("Topological Sort/01_Course_Schedule_II/solution.py", top_p1_sol_py)

# =====================================================================
# 3. UNION FIND & ADVANCED GRAPH ALGORITHMS
# =====================================================================

uf_readme = """# 🤝 Topic: Union Find & Advanced Graphs (Python DSA from Scratch)

## 🌟 1. Real-Life Analogy
- **Union Find (Disjoint Set Union - DSU)**: Merging friend groups at a party. You test if two people are already in the same social circle in near-$O(1)$ time ($\alpha(N)$ inverse Ackermann) using path compression and union by rank!
- **Dijkstra's Shortest Path**: Google Maps navigation finding the fastest driving route through roads with positive travel times.
- **Minimum Spanning Tree (MST)**: Laying the minimum length of fiber optic cable to connect all cities in a grid.

## 📚 Problems in this Directory
1. `Union Find/01_Number_of_Connected_Components` (Medium - Google, Meta)
2. `Shortest Path/01_Network_Delay_Time` (Medium - Google, Amazon - Dijkstra)
3. `Minimum Spanning Tree/01_Min_Cost_to_Connect_All_Points` (Medium - Meta, Amazon - Prim's)
4. `Eulerian Circuit/01_Reconstruct_Itinerary` (Hard - Google - Hierholzer's)
5. `Strongly Connected Component/01_Critical_Connections_in_a_Network` (Hard - Amazon - Tarjan's)
"""

uf_p1_prob = """# 📖 Number of Connected Components in an Undirected Graph (LeetCode #323)

- **Difficulty**: Medium
- **Asked By**: Google, Meta, Amazon
- **Frequency**: ⭐⭐⭐⭐⭐ (The quintessential Union Find problem)
"""

uf_p1_sol_md = """# 💡 Number of Connected Components - Solution Deep Dive

## 🧠 Thought Process (Disjoint Set Union with Path Compression)
Start with `count = n`.
For each edge `(u, v)`:
- If `find(u) != find(v)`, union them and decrement `count -= 1`.
Return `count`.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(E \\cdot \\alpha(V)) \\approx O(E)$
- **Space Complexity**: $O(V)$
"""

uf_p1_sol_py = '''"""
Problem: Number of Connected Components in an Undirected Graph (LeetCode #323)
Disjoint Set Union (DSU) with Path Compression & Union by Rank
Time Complexity: O(E * alpha(V))
Space Complexity: O(V)
"""

from typing import List

class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.count = n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # Already in same component

        # Union by rank
        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        self.count -= 1
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = UnionFind(n)
        for u, v in edges:
            dsu.union(u, v)
        return dsu.count

if __name__ == "__main__":
    sol = Solution()
    assert sol.countComponents(5, [[0, 1], [1, 2], [3, 4]]) == 2
    assert sol.countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) == 1
    print("✅ All Number of Connected Components tests passed!")
'''

sp_p1_prob = """# 📖 Network Delay Time (LeetCode #743)

- **Difficulty**: Medium
- **Asked By**: Google, Amazon
- **Frequency**: ⭐⭐⭐⭐⭐ (Canonical Dijkstra's Algorithm)
"""

sp_p1_sol_md = """# 💡 Network Delay Time - Solution Deep Dive

## 🧠 Thought Process (Dijkstra's Algorithm with Min-Heap)
Min-heap of `(time_so_far, node)`.
Pop node with smallest elapsed time. If not yet visited, record its shortest distance and push all neighbors.
Result is max of shortest distances to all nodes.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(E \\log V)$
- **Space Complexity**: $O(V + E)$
"""

sp_p1_sol_py = '''"""
Problem: Network Delay Time (LeetCode #743)
Dijkstra's Shortest Path Algorithm
Time Complexity: O(E log V)
Space Complexity: O(V + E)
"""

import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n + 1)]
        for u, v, w in times:
            adj[u].append((v, w))

        min_heap = [(0, k)]  # (time, node)
        visited = {}

        while min_heap:
            time, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited[node] = time

            for nei, weight in adj[node]:
                if nei not in visited:
                    heapq.heappush(min_heap, (time + weight, nei))

        return max(visited.values()) if len(visited) == n else -1

if __name__ == "__main__":
    sol = Solution()
    assert sol.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2) == 2
    assert sol.networkDelayTime([[1,2,1]], 2, 1) == 1
    assert sol.networkDelayTime([[1,2,1]], 2, 2) == -1
    print("✅ All Network Delay Time tests passed!")
'''

mst_p1_prob = """# 📖 Min Cost to Connect All Points (LeetCode #1584)

- **Difficulty**: Medium
- **Asked By**: Meta, Amazon
- **Frequency**: ⭐⭐⭐⭐⭐ (Prim's Algorithm)
"""

mst_p1_sol_md = """# 💡 Min Cost to Connect All Points - Solution Deep Dive

## 🧠 Thought Process (Prim's MST Algorithm)
Start at node 0. Add all connecting Manhattan distance edges to a min-heap.
Repeatedly pop the smallest edge that connects to an unvisited point until all points are connected.

## ⏱️ Complexity Analysis
- **Time Complexity**: $O(N^2 \\log N)$
- **Space Complexity**: $O(N^2)$
"""

mst_p1_sol_py = '''"""
Problem: Min Cost to Connect All Points (LeetCode #1584)
Prim's Minimum Spanning Tree Algorithm
Time Complexity: O(N^2 log N)
Space Complexity: O(N)
"""

import heapq
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = set()
        min_heap = [(0, 0)]  # (cost, point_index)
        total_cost = 0

        while len(visited) < n:
            cost, u = heapq.heappop(min_heap)
            if u in visited:
                continue

            visited.add(u)
            total_cost += cost

            # Add edges to all unvisited nodes
            for v in range(n):
                if v not in visited:
                    dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    heapq.heappush(min_heap, (dist, v))

        return total_cost

if __name__ == "__main__":
    sol = Solution()
    assert sol.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]) == 20
    assert sol.minCostConnectPoints([[3,12],[-2,5],[-4,1]]) == 18
    print("✅ All Min Cost to Connect All Points tests passed!")
'''

print("Writing Union Find, Shortest Path, MST files...")
create_file("Union Find/README.md", uf_readme)
create_file("Union Find/01_Number_of_Connected_Components/problem.md", uf_p1_prob)
create_file("Union Find/01_Number_of_Connected_Components/solution.md", uf_p1_sol_md)
create_file("Union Find/01_Number_of_Connected_Components/solution.py", uf_p1_sol_py)

create_file("Shortest Path/README.md", uf_readme)
create_file("Shortest Path/01_Network_Delay_Time/problem.md", sp_p1_prob)
create_file("Shortest Path/01_Network_Delay_Time/solution.md", sp_p1_sol_md)
create_file("Shortest Path/01_Network_Delay_Time/solution.py", sp_p1_sol_py)

create_file("Minimum Spanning Tree/README.md", uf_readme)
create_file("Minimum Spanning Tree/01_Min_Cost_to_Connect_All_Points/problem.md", mst_p1_prob)
create_file("Minimum Spanning Tree/01_Min_Cost_to_Connect_All_Points/solution.md", mst_p1_sol_md)
create_file("Minimum Spanning Tree/01_Min_Cost_to_Connect_All_Points/solution.py", mst_p1_sol_py)

print("Batch 4 generated successfully!")
