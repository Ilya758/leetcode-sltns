class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []

        def dfs(node):
            if not node:
                return -1

            left = dfs(node.left)
            right = dfs(node.right)
            cur = max(left, right) + 1

            if cur == len(ans):
                ans.append([])

            ans[cur].append(node.val)

            return cur

        dfs(root)

        return ans


