# 🎯 Topic: Binary Search (Python DSA from Scratch)

## 🌟 1. Real-Life Analogy: What is Binary Search?
Looking up a word in a **printed physical dictionary** (e.g. 100,000 words):
You don't start at page 1 reading word by word.
You open the exact middle of the book.
- If your word starts with 'M' and you see 'T', you tear the entire right half of the book away!
- In just **17 page flips**, you can find any single word in a 100,000-page book ($2^{17} > 100,000$)!
This is **$O(\log N)$ logarithmic time**.

## 🤖 2. Why AI Engineers Care
- **Binary Search on the Answer Range**: Hyperparameter optimization, finding learning rate boundaries, or determining minimum GPU batch sizes before Out-Of-Memory (OOM).
- **Quantization & Threshold Tuning**: Finding the exact classification threshold to meet a target false positive rate (Precision-Recall curve search).

## 📚 Problems in this Directory
1. `01_Binary_Search` (Easy - Google, Meta)
2. `02_Search_in_Rotated_Sorted_Array` (Medium - Meta, Google, Amazon)
3. `03_Find_Minimum_in_Rotated_Sorted_Array` (Medium - Amazon, Microsoft)
4. `04_Koko_Eating_Bananas` (Medium - Google, Airbnb - Binary Search on Answer)
