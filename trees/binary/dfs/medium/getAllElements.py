class Solution:
    def getAllElements(self, root1, root2):
        nums = []

        def dfs(node):
            if node:
                nums.append(node.val)
                dfs(node.left)
                dfs(node.right)

        dfs(root1)
        dfs(root2)

        return sorted(nums)