# 💡 Course Schedule - Solution Deep Dive

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
