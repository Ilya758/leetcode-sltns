# https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans = []

        def backtrack(curr: list[int] = [], i=0):
            if i <= len(nums):
                ans.append(curr[:])

                for j in range(i, len(nums)):
                    curr.append(nums[j])
                    backtrack(curr, j + 1)
                    curr.pop()

        backtrack()

        return ans


print(Solution().subsets(nums=[1, 2, 3]))
# [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
