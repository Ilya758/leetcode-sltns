
# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/

from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def distanceK(root: TreeNode, target: TreeNode, k: int) -> list[int]:
    # 1. first we convert binary tree into undirected graph.
    def dfs(node: TreeNode | None, parent: TreeNode | None):
        if not node:
            return

        # by assigning the Parent node to all of the nodes
        node.parent = parent

        dfs(node.left, node)
        dfs(node.right, node)

    dfs(root, None)
    # finally, all of the nodes has left, right and parent node

    q = deque([target])
    seen = {target}
    dist = 0

    # 2. perform bfs, until q isn't empty and we'll reach destination
    while q and dist < k:
        n = len(q)

        for _ in range(n):
            node = q.popleft()

            for neig in [node.left, node.right, node.parent]:
                if neig and neig not in seen:
                    seen.add(neig)
                    q.append(neig)

        dist += 1

    return [node.val for node in q]
