from collections import deque


class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        ans = 0

        def getCount(temp):
            cur = 0
            cache = { x: i for i, x in enumerate(temp) }
            temp.sort()
            i = 0

            while i < len(temp):
                j = cache[temp[i]]

                if i != j:
                    temp[i], temp[j] = temp[j], temp[i]
                    cur += 1
                else:
                    i += 1

            return cur

        while q:
            n = len(q)
            nums = []

            for _ in range(n):
                node = q.popleft()
                nums.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            ans += getCount(nums)
                           
        return ans 
