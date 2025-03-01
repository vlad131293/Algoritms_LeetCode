from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def get_number(self, ls: Optional[ListNode]) -> int:
        number = ls.val
        next_node = ls.next
        k = 1
        while next_node is not None:
            number += next_node.val * 10**k
            next_node = next_node.next
            k += 1
        return number

    def put_number(self, num: int) -> Optional[ListNode]:
        d = num % 10
        num = num // 10
        ls = ListNode(val=d)
        current_node = ls
        while num != 0:
            d = num % 10
            num = num // 10
            current_node.next = ListNode(val=d)
            current_node = current_node.next
        return ls

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        num_1: int = self.get_number(l1)
        num_2: int = self.get_number(l2)
        res = num_1 + num_2
        l: ListNode = self.put_number(res)
        return l
