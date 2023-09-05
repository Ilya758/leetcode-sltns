from collections import deque


class Solution:
    def sumEvenGrandparent(self, root) -> int:
        ans = 0
        q = deque([[root, None, None]])

        while q:
            n = len(q)

            for _ in range(n):
                node, parent, grand = q.popleft()

                if grand and grand.val % 2 == 0:
                    ans += node.val
                
                if node.left:
                    q.append([node.left, node, parent])
                if node.right:
                    q.append([node.right, node, parent])

        return ans