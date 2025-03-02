from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        m = 1
        current = head
        while current.next is not None:
            current = current.next
            m += 1
        if m == 1:
            return None
        if m == n:
            return head.next
        i = 0
        current = head
        while i < (m - n - 1):
            current = current.next
            i += 1
        current.next = current.next.next
        return head
