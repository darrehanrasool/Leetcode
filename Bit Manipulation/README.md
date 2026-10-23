# ⚡ Topic: Bit Manipulation & Bitmask (Python DSA from Scratch)

## 🌟 1. Real-Life Analogy
A bank of light switches: each switch is either ON (`1`) or OFF (`0`).
- `AND (&)`: Both switches on.
- `OR (|)`: At least one switch on.
- `XOR (^)`: Exactly one switch on (toggles state; `x ^ x = 0`).
- `NOT (~)`: Invert all switches.
- `Left Shift (<< 1)`: Multiply by 2.
- `Right Shift (>> 1)`: Divide by 2.

## 🤖 2. Why AI Engineers Care
- **Quantized Neural Networks (INT4 / FP8 / NF4)**: LLM quantization (bitsandbytes, AWQ, GPTQ) packs 4-bit weights into 32-bit registers using bitmasks and shifts.
- **Attention Bitmasks**: Causal attention and padding masks are represented as binary bitmasks.

## 📚 Problems
1. `01_Number_of_1_Bits` (Easy - Google, Apple)
2. `02_Counting_Bits` (Easy - Meta, Amazon)
