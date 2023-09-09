class Solution:
    def maxAncestorDiff(self, root):
        def dfs(node, curMin = float('inf'), curMax = float('-inf')):
            if not node:
                return curMax - curMin

            MIN = min(curMin, node.val)
            MAX = max(curMax, node.val)
            left = dfs(node.left, MIN, MAX)
            right = dfs(node.right, MIN, MAX)

            return max(left, right) 

        return dfs(root)