class Solution:
    def distributeCoins(self, root):
        self.ans = 0
        
        def dfs(node):
            if not node:
                return 0
                
            left, right = dfs(node.left), dfs(node.right)
            self.ans += abs(left) + abs(right)

            return node.val + left + right - 1

        dfs(root)
        
        return self.ans
