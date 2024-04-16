class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root)

        cur = 1
        q = deque([root])

        while cur < depth:
            n = len(q)

            for _ in range(n):
                node = q.popleft()

                if cur == depth - 1:
                    left = node.left
                    right = node.right
                    node.left = TreeNode(val, left)
                    node.right = TreeNode(val, None, right)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            cur += 1

        return root
