class Solution:
    def __init__(self):
        self.seen = {None: None}
            
    def dfs(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        if not root:
            return None

        if self.seen.get(root):
            return self.seen.get(root)

        copiedNode = NodeCopy(root.val)
        self.seen[root] = copiedNode
        copiedNode.left = self.dfs(root.left)
        copiedNode.right = self.dfs(root.right)
        copiedNode.random = self.dfs(root.random)
        
        return copiedNode

    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        return self.dfs(root)
