class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.ans = 0

        def dfs(node):
            if node:
                if not node.left and not node.right:
                    return [1]

                left = dfs(node.left)
                right = dfs(node.right)

                for i in left:
                    for j in right:
                        if i + j <= distance:
                            self.ans += 1

                return [i + 1 for i in left + right if i + 1 < distance]

            return []

        dfs(root)

        return self.ans