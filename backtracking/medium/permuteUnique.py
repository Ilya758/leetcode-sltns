class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        ans = set()

        def backtrack(curr: list[int]):
            if len(curr) == len(nums):
                ans.add(tuple(nums[i] for i in curr))
                return

            for num in range(len(nums)):
                if num not in curr:
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()

        backtrack([])

        return ans
    
print(Solution().permute(nums=[1, 2, 3]))
# [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]