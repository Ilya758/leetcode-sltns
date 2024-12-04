class Solution:
    def getSum(self, nums: list[int]) -> int:
        ans = curr = nums[0]
        mod = 10**9 + 7
        prev = left = 0

        for right in range(1, len(nums)):
            diff = nums[right] - nums[right - 1]

            if abs(diff) != 1:
                prev = curr = 0
                left = right
            elif prev != diff:
                curr = nums[right - 1]
                left = right - 1
                prev = diff

            curr += nums[right] * (right - left + 1)
            ans = (ans + curr) % mod

        return ans

print(Solution().getSum([1,2,3])) # 20