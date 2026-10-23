# 🪟 Topic: Sliding Window (Python DSA from Scratch)

## 🌟 1. Real-Life Analogy: What is a Sliding Window?
Imagine a **magnifying glass** or a **moving camera frame** scanning across a film strip:
- The window has a `left` edge and a `right` edge: `[left ... right]`.
- As the camera moves right, new objects enter the frame.
- If the frame becomes invalid (e.g. too noisy or contains duplicate items), we shrink the frame by sliding the `left` edge forward.

## 🤖 2. Why AI Engineers Care
- **Token Context Windows in LLMs**: Sliding context windows are how LLMs process documents longer than their context length (e.g. 8K tokens window sliding over a 100K token book).
- **Time Series Feature Engineering**: Moving averages, rolling volatility, and rolling standard deviation over financial or sensor metrics.
- **Convolution in CNNs**: A convolutional kernel sliding over pixel matrices is a 2D sliding window!

## 📚 Problems in this Directory
1. `01_Longest_Substring_Without_Repeating_Characters` (Medium - Google, Meta, Amazon)
2. `02_Minimum_Window_Substring` (Hard - Meta, Google, Airbnb)
