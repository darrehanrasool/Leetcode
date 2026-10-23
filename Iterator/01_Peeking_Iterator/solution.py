"""
Problem: Peeking Iterator (LeetCode #284)
Generator/Iterator Lookahead Buffer
"""

class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self._has_next = iterator.hasNext()
        self._peeked_val = iterator.next() if self._has_next else None

    def peek(self):
        return self._peeked_val

    def next(self):
        val = self._peeked_val
        self._has_next = self.iterator.hasNext()
        self._peeked_val = self.iterator.next() if self._has_next else None
        return val

    def hasNext(self):
        return self._has_next

class SimpleIterator:
    def __init__(self, items):
        self.items = items
        self.idx = 0

    def hasNext(self):
        return self.idx < len(self.items)

    def next(self):
        val = self.items[self.idx]
        self.idx += 1
        return val

if __name__ == "__main__":
    base = SimpleIterator([1, 2, 3])
    pi = PeekingIterator(base)
    assert pi.next() == 1
    assert pi.peek() == 2
    assert pi.next() == 2
    assert pi.next() == 3
    assert pi.hasNext() is False
    print("✅ All Peeking Iterator tests passed!")
