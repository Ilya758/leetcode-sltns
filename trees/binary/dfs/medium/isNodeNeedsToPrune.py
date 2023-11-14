class Solution:
    def isNodeNeedsToPrune(self, node):
        return not node.val and not node.left and not node.right

    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if node:
                node.left = dfs(node.left)
                node.right = dfs(node.right)

                return None if self.isNodeNeedsToPrune(node) else node
            
            return node

        return dfs(root)