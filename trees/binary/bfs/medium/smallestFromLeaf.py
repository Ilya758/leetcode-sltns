class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        strs = []

        def dfs(node, path):
            if node:
                val = path + chr(97 + node.val)

                if not node.left and not node.right:
                    strs.append(val[::-1])
                else:
                    dfs(node.left, val)
                    dfs(node.right, val)

        dfs(root, '')
        
        return min(strs)