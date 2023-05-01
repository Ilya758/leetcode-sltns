# https://leetcode.com/problems/path-sum-ii/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pathSum(root: Optional[TreeNode], targetSum: int) -> list[list[int]]:
    ans = []

    def dfs(node, paths, sum):
        if not node:
            return

        sum += node.val
        tmp = [*paths, node.val]

        if sum == targetSum and not node.left and not node.right:
            ans.append(tmp)
            return

        dfs(node.left, tmp, sum)
        dfs(node.right, tmp, sum)

    dfs(root, [], 0)

    return ans
