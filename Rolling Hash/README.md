# 🔎 Topic: String Matching, Rolling Hash & Suffix Array (Python DSA from Scratch)

## 🌟 Real-Life Analogy
Ctrl+F searching in a document:
- **KMP (Knuth-Morris-Pratt)**: Never backs up the search pointer by precomputing a prefix table (LPS).
- **Rabin-Karp Rolling Hash**: Treats character substrings like polynomial numbers in base 26/prime, allowing $O(1)$ window hash updates!
