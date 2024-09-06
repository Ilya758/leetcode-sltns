class Solution:
    def maximumSumScore(self, nums: list[int]) -> int:
        prefix = [nums[0]]
        n = len(nums)

        for i in range(1, n):
            prefix.append(nums[i] + prefix[-1])

        ans = float('-inf')

        for i in range(n):
            ans = max(ans, prefix[i], prefix[-1] - (prefix[i - 1] if i else 0))

        return ans
    
print(Solution().maximumSumScore([-3,-5])) # -3