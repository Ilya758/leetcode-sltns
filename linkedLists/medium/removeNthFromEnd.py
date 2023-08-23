# Definition for singly-linked list.
from typing import Optional


# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        depth = 0
        dummy = head

        while dummy:
            dummy = dummy.next
            depth += 1
        
        prev = ListNode(0, head)
        dummy = prev

        while depth > n:
            depth -= 1
            prev = prev.next

        prev.next = prev.next.next

        return dummy.next


list1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
Solution().removeNthFromEnd(head=list1, n=2)
Solution().removeNthFromEnd(head=ListNode(1), n=1)