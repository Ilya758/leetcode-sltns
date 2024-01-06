class Solution:
    def longestNiceSubarray(self, nums: list[int]) -> int:
        left = 0
        prev = 0
        ans = 1

        for right in range(len(nums)):
            while left < right and prev & nums[right] != 0:
                prev ^= nums[left]
                left += 1

            prev |= nums[right]
            ans = max(ans, right - left + 1)  

        return ans

print(Solution().longestNiceSubarray([1,3,8,48,10])) # 3