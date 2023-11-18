from collections import defaultdict


class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        cache = defaultdict(int)
        maxFreq = 0

        def dfs(node):
            nonlocal maxFreq

            if node:
                left = dfs(node.left)
                right = dfs(node.right)
                val = node.val + left + right
                cache[val] += 1
                maxFreq = max(maxFreq, cache[val])

                return val

            return 0

        dfs(root)
        ans = []

        for k, v in cache.items():
            if v == maxFreq: ans.append(k)

        return ans