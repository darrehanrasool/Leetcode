"""
Problem: Word Frequency (LeetCode #192)
Shell / Python Counter Equivalency
Equivalent bash command: cat words.txt | tr -s ' ' '\n' | sort | uniq -c | sort -r | awk '{print $2, $1}'
"""

from collections import Counter

def word_frequency(text: str):
    words = text.strip().split()
    counts = Counter(words)
    return sorted(counts.items(), key=lambda x: -x[1])

if __name__ == "__main__":
    text = "the day is sunny the the the sunny is is"
    res = word_frequency(text)
    assert res[0] == ("the", 4)
    assert res[1] == ("is", 3)
    assert res[2] == ("sunny", 2)
    assert res[3] == ("day", 1)
    print("✅ All Shell / Word Frequency tests passed!")
