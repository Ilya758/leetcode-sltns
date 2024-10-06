class Solution:
    ans = 0

    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        def dfs(node, val):
            if not node:
                return val

            left, right = dfs(node.left, node.val), dfs(node.right, node.val)
            equals = node.val == left == right
            self.ans += int(equals) 

            return node.val if equals else -1001

        dfs(root, 0)

        return self.ans
