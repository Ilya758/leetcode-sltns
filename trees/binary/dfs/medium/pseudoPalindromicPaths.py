class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        digits = [0] * 9
        ans = 0

        def dfs(node):
            if node:
                digits[node.val - 1] += 1
                dfs(node.left)
                dfs(node.right)

                if not node.left and not node.right:
                    nonlocal ans
                    x = 0

                    for d in digits:
                        x += d & 1

                    if x < 2:
                        ans += 1

                digits[node.val - 1] -= 1
                
        dfs(root)

        return ans 
        