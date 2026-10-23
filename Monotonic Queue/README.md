# 🚶 Topic: Queue & Monotonic Queue (Python DSA from Scratch)

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
