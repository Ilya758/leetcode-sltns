from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            left, right = False, False
            
            if node.left:
                left = dfs(node.left)
            if node.right:
                right = dfs(node.right)

            match node.val:
                case 0:
                    return False
                case 1:
                    return True
                case 2:
                    return left or right
                case _:
                    return left and right

        return dfs(root)