# https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        vals = []

        def dfs(node):
            if not node: return

            vals.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        vals.sort()
        ans = float('inf')

        for i in range(1, len(vals)):
            num = abs(vals[i] - vals[i - 1])

            if num < ans: ans = num
        
        return ans