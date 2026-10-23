"""
Problem: Merge Two Sorted Lists (LeetCode #21)
Dummy Head Splice
Time Complexity: O(M + N)
Space Complexity: O(1)
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 if list1 else list2
        return dummy.next

def to_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

def from_list(vals):
    dummy = ListNode(0)
    curr = dummy
    for v in vals:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

if __name__ == "__main__":
    sol = Solution()
    l1 = from_list([1, 2, 4])
    l2 = from_list([1, 3, 4])
    merged = sol.mergeTwoLists(l1, l2)
    assert to_list(merged) == [1, 1, 2, 3, 4, 4]
    print("✅ All Merge Two Sorted Lists tests passed!")
