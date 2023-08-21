# https://leetcode.com/problems/reverse-linked-list/description/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1. store the prev and a cur node
        prev, cur = None, head

        # 2. while the list isn't empty
        while cur:
            # 3. swap the values
            prev = ListNode(cur.val, prev)
            cur = cur.next

        return prev