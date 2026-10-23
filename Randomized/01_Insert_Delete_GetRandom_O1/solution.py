"""
Problem: Insert Delete GetRandom O(1) (LeetCode #380)
Array + Hash Map Index Mapping
All operations in O(1) time
"""

import random

class RandomizedSet:
    def __init__(self):
        self.val_to_idx = {}
        self.vals = []

    def insert(self, val: int) -> bool:
        if val in self.val_to_idx:
            return False
        self.val_to_idx[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_idx:
            return False
        # Swap with last element to pop in O(1)
        idx_to_remove = self.val_to_idx[val]
        last_val = self.vals[-1]

        self.vals[idx_to_remove] = last_val
        self.val_to_idx[last_val] = idx_to_remove

        self.vals.pop()
        del self.val_to_idx[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.vals)

if __name__ == "__main__":
    rs = RandomizedSet()
    assert rs.insert(1) is True
    assert rs.remove(2) is False
    assert rs.insert(2) is True
    assert rs.getRandom() in [1, 2]
    assert rs.remove(1) is True
    assert rs.getRandom() == 2
    print("✅ All RandomizedSet tests passed!")
