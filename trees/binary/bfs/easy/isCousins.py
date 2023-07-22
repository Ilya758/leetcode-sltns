# https://leetcode.com/problems/cousins-in-binary-tree/

from collections import deque


class Solution:
    def isCousins(self, root, x: int, y: int) -> bool:
        q = deque([root])

        while q:
            n = len(q)
            levelQ = []

            for _ in range(n):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                    levelQ.append(node.left.val)
                if node.right:
                    q.append(node.right)
                    levelQ.append(node.right.val)

                if node.left and node.right:
                    if (node.left.val == x and node.right.val == y) or (node.left.val == y and node.right.val == x):
                        return False

            if x in levelQ and y in levelQ:
                return True

        return False
