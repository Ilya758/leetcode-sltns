class Solution:
    def minDifference(self, nums: list[int]) -> int:
        k = 4
        n = len(nums)

        if n <= k:
            return 0

        nums.sort()
        ans = float("inf")

        for left in range(k):
            right = n - k + left
            ans = min(ans, nums[right] - nums[left])

        return ans

print(Solution().minDifference([6,6,0,1,1,4,6])) # 2