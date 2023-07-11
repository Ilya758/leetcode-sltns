# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/

from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list[int]:
        # 1. Tricky solution assumes we want at each step has a parent node
        def dfs(node, parent):
            if not node:
                return

            node.parent = parent
            dfs(node.left, node)
            dfs(node.right, node)

        # 2. After dfs, this isn't a binary tree anymore, and we can
        # treat this structure as a directed graph, but this doesn't affect
        # anything
        dfs(root, None)

        # 3. Start from target node by doing standard bfs until
        # it reveals all of the nodes, that are right on a distance of K
        q = deque([target])
        seen = set({target})
        lvl = 0

        while q and lvl < k:
            n = len(q)

            for _ in range(n):
                node = q.popleft()

                for neig in [node.left, node.right, node.parent]:
                    if neig and neig not in seen:
                        q.append(neig)
                        seen.add(neig)

            lvl += 1

        return [node.val for node in q]
