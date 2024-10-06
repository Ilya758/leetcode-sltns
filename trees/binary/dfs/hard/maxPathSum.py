class Solution:
    ans = float('-inf')

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0

            left, right = max(dfs(node.left), 0), max(dfs(node.right), 0)
            self.ans = max(self.ans, left + right + node.val)

            return max(node.val + left, node.val + right)

        dfs(root)
        
        return self.ans
