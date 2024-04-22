from collections import deque


class CBTInserter:
    def makeQueue(self, root: Optional[TreeNode]):
        q = deque([root])
        res = deque([])
        
        while q:
            n = len(q)

            for _ in range(n):
                node = q.popleft()

                if node and (not node.left or not node.right):
                    res.append(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return res

    def __init__(self, root: Optional[TreeNode]):
        self.q = self.makeQueue(root) if root else deque([])
        self.root = root

    def insert(self, val: int) -> int:
        if not self.q:
            self.root = TreeNode(val)
            self.q.append(self.root)
        else:
            cur = self.q[0]

            if not cur.left:
                cur.left = TreeNode(val)
                self.q.append(cur.left)
            elif not cur.right:
                cur.right = TreeNode(val)
                self.q.append(cur.right)
            else:
                self.q.popleft()
                return self.insert(val)

        return self.q[0].val

    def get_root(self) -> Optional[TreeNode]:
        return self.root