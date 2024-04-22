from collections import deque


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ans = []
        q = deque([root])

        while q:
            lvl = []
            n = len(q)

            for _ in range(n):
                node = q.popleft()
                
                if node:
                    lvl.append(node.val)

                    for nei in node.children:
                        q.append(nei)
            
            if lvl:
                ans.append(lvl)

        return ans