from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def createBinaryTree(self, descriptions: list[list[int]]) -> Optional[TreeNode]:
        nodes = defaultdict(TreeNode)
        hasParent = set()

        for parent, child, isLeft in descriptions:
            if child not in nodes: nodes[child] = TreeNode(child)
            if parent not in nodes: nodes[parent] = TreeNode(parent)
            
            if isLeft: nodes[parent].left = nodes[child]
            else: nodes[parent].right = nodes[child]
            
            hasParent.add(child)
            
        for child in nodes.keys():
            if child not in hasParent:
                return nodes[child].val

    
print(Solution().createBinaryTree([[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]))