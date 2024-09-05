from bisect import bisect_left
from typing import Optional


class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        nums = []

        def dfs(node):
            if node:
                dfs(node.left)
                nums.append(node.val)
                dfs(node.right)

        ans = []
        dfs(root)
        x = bisect_left(nums, target)
        left, right = x - 1, x

        def getDiff(p):
            return abs(target - nums[p]) if 0 <= p < len(nums) else float('inf')

        while k:
            k -= 1
            
            if getDiff(left) < getDiff(right):
                ans.append(nums[left])
                left -= 1
            else:
                ans.append(nums[right])
                right += 1

        return ans