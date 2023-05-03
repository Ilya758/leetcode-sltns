# https://leetcode.com/problems/even-odd-tree/

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isEvenOddTree(root: Optional[TreeNode]) -> bool:
    isOdd = 0
    q = deque([root])

    def isInvalid(vals: list[int], isOdd: bool) -> bool:
        if not isOdd:
            vals.reverse()

        for i in range(1, len(vals)):
            if vals[i] <= vals[i - 1]:
                return True

        return False

    while q:
        # 1. switch isOdd
        isOdd = (isOdd + 1) % 2
        # 2. get all of the vals in current level
        vals = [node.val for node in q]

        # 3. check, if there're invalid
        if isInvalid(vals, isOdd):
            return False

        # 4. perform dfs,
        for _ in range(len(q)):
            node = q.popleft()

            # 4.1 by checking constraints
            if (node.val % 2 != isOdd):
                return False
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    return True
