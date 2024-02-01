from collections import deque


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        ans = 0
        q = deque([root])

        while q:
            n = len(q)

            for i in range(n):
                node = q.popleft()

                if i == 0:
                    ans = node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
        return ans