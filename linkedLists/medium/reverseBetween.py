
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int, depth = 0) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(next=head)
        prev = dummy
        cur = head

        while cur:
            depth += 1

            if left <= depth < right:
                nextNode = cur.next
                cur.next = nextNode.next
                nextNode.next = prev.next
                prev.next = nextNode
            else:
                if depth < right:
                    prev = prev.next
                cur = cur.next

        return dummy.next