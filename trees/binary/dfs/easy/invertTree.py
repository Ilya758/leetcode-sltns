class Solution:
    def invertTree(self, root):
        def dfs(node):
            if not node:
                return

            tmp = node.right
            node.right = node.left
            node.left = tmp
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return root
