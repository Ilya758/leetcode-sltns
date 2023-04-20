from collections import deque
from typing import Optional

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        q = deque([(root, 0)])
        
        while q:
            n = len(q)
            _, startPoint = q[0]

            for _ in range(n):
                node, index = q.popleft()

                print(index)

                if node.left:
                    q.append((node.left, 2 * index)) 
                if node.right:
                    q.append((node.right, 2 * index + 1)) 

            ans = max(ans, index - startPoint + 1)

        return ans