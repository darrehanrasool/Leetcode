# 🔗 Topic: Linked List & Doubly-Linked List (Python DSA from Scratch)

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
