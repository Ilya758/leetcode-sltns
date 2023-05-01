# https://leetcode.com/problems/path-sum-iii/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ans = 0

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, paths):
            if not node:
                return

            tmp = [*paths, 0]

            for i in range(len(tmp)):
                tmp[i] += node.val

                if tmp[i] == targetSum:
                    self.ans += 1

            dfs(node.left, tmp)
            dfs(node.right, tmp)

        dfs(root, [])

        return self.ans
