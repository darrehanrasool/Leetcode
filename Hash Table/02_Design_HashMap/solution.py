"""
Problem: Design HashMap (LeetCode #706)
Bucket Array with Chaining
Time Complexity: O(1) average per operation
Space Complexity: O(N)
"""

class MyHashMap:
    def __init__(self):
        self.size = 1009  # Prime number for uniform distribution
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        idx = self._hash(key)
        bucket = self.buckets[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key: int) -> int:
        idx = self._hash(key)
        bucket = self.buckets[idx]
        for k, v in bucket:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        bucket = self.buckets[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return

if __name__ == "__main__":
    h = MyHashMap()
    h.put(1, 1)
    h.put(2, 2)
    assert h.get(1) == 1
    assert h.get(3) == -1
    h.put(2, 1)
    assert h.get(2) == 1
    h.remove(2)
    assert h.get(2) == -1
    print("✅ All Design HashMap tests passed!")
