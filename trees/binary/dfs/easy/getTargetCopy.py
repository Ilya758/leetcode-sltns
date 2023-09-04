class Solution:
    def getTargetCopy(self, original, cloned, target):
        def dfs(o, c):
            if not o:
                return None

            if o is target:
                return c

            return dfs(o.left, c.left) or dfs(o.right, c.right)

        return dfs(original, cloned)
