class Solution:
    def minDepth(self, root) -> int:
        def dfs(node, depth):
            if not node:
                return depth

            ans = float('inf')

            if not node.left and not node.right:
                return depth + 1

            if node.left:
                ans = min(ans, dfs(node.left, depth + 1))
            if node.right:
                ans = min(ans, dfs(node.right, depth + 1))

            return ans

        return dfs(root, 0)
