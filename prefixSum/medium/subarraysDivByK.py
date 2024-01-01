class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        prefix = [0] * k
        prefix[0] = 1
        cur = 0
        ans = 0

        for num in nums:
            cur += num
            mod = cur % k
            ans += prefix[mod]
            prefix[mod] += 1

        return ans
    
print(Solution().subarraysDivByK(nums = [4,5,0,-2,-3,1], k = 5)) # 7