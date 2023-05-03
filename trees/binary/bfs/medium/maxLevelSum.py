# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxLevelSum(root: Optional[TreeNode]) -> int:
    ans = 0
    max = float("-inf")
    lvl = 1
    q = deque([root])

    while q:
        curr = 0

        for _ in range(len(q)):
            node = q.popleft()
            curr += node.val

            if (node.left):
                q.append(node.left)
            if (node.right):
                q.append(node.right)

        if (max < curr):
            max = curr
            ans = lvl

        lvl += 1

    return ans
