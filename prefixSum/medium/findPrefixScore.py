class Solution:
    def findPrefixScore(self, nums: list[int]) -> list[int]:
        score = nums[0]
        ans = [nums[0] * 2]

        for i in range(1, len(nums)):
            score = max(score, nums[i])
            ans.append(ans[i - 1] + nums[i] + score)

        return ans
        
print(Solution().findPrefixScore(nums = [2,3,7,5,10])) # [4,10,24,36,56]