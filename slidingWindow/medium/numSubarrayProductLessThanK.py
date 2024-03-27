class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        i = 0
        total = 1
        ans = 0

        for j in range(len(nums)):
            total *= nums[j]

            while i <= j and total >= k:
                total /= nums[i]
                i += 1
            
            ans += j - i + 1

        return ans

print(Solution().numSubarrayProductLessThanK([10,5,2,6], 100)) # 8