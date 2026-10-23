# 🕸️ Topic: Graph & Topological Sort (Python DSA from Scratch)

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
