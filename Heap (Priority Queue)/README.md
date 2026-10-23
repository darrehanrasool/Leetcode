# 🏔️ Topic: Heap / Priority Queue (Python DSA from Scratch)

## 🌟 1. Real-Life Analogy: What is a Heap?
An **Emergency Room triage system**:
Patients don't see the doctor in order of arrival (FIFO). The patient with the most urgent condition (highest priority) is always treated first!
- **Min-Heap**: Smallest element is at the root ($O(1)$ lookup, $O(\log K)$ insertion/removal).
- In Python: standard `heapq` module is a **Min-Heap**.

## 🤖 2. Why AI Engineers Care
- **Top-K Sampling & Beam Search in LLMs**: At every generation step, picking the top $K$ most probable next tokens uses a Min-Heap.
- **k-Nearest Neighbors (k-NN)**: Finding the closest vector embeddings to a query embedding.
- **Dijkstra's Algorithm & A* Search**: Path planning in robotics and gaming.

## 📚 Problems in this Directory
1. `01_Kth_Largest_Element_in_an_Array` (Medium - Meta, Amazon)
2. `02_Top_K_Frequent_Elements` (Medium - Meta, Google)
3. `03_Find_Median_from_Data_Stream` (Hard - Google, Amazon, Citadel)
