# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/
from collections import deque


class Solution:
    def populate(self, root: 'Node') -> 'Node':
        q = deque([root])

        while q:
            n = len(q)
            prev = None

            for _ in range(n):
                node = q.popleft()

                if node:
                    if prev:
                        prev.next = node
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

                prev = node

        return root