"""
Problem: Linked List Cycle (LeetCode #141)
Floyd's Cycle-Finding Algorithm (Tortoise & Hare)
Time Complexity: O(N)
Space Complexity: O(1)
"""

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

if __name__ == "__main__":
    sol = Solution()
    n1 = ListNode(3)
    n2 = ListNode(2)
    n3 = ListNode(0)
    n4 = ListNode(-4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2  # cycle back to n2
    assert sol.hasCycle(n1) is True

    n_linear = ListNode(1)
    n_linear.next = ListNode(2)
    assert sol.hasCycle(n_linear) is False
    print("✅ All Linked List Cycle tests passed!")
