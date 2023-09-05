
# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cache = dict()
        cur = head

        while cur:
            cache[cur] = Node(cur.val)
            cur = cur.next

        cur = head

        while cur:
            if cur.next:
                cache[cur].next = cache[cur.next]
            if cur.random:
                cache[cur].random = cache[cur.random]
            cur = cur.next

        return cache[head] if head in cache else None 