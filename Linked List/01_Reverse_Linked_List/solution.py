"""
Problem: Reverse Linked List (LeetCode #206)
Iterative Three-Pointer Reversal
Time Complexity: O(N)
Space Complexity: O(1)
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

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
    ll = from_list([1, 2, 3, 4, 5])
    rev = sol.reverseList(ll)
    assert to_list(rev) == [5, 4, 3, 2, 1]
    print("✅ All Reverse Linked List tests passed!")
