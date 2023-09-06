from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstFromPreorder(self, preorder: list[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
            
        node = TreeNode(preorder[0])
        node.left = self.bstFromPreorder([x for x in preorder if x < preorder[0]])
        node.right = self.bstFromPreorder([x for x in preorder if x > preorder[0]])

        return node