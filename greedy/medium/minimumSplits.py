from math import gcd


class Solution:
    def minimumSplits(self, nums: list[int]) -> int:
        ans = 0
        cur = 1

        for num in nums:
            cur = gcd(num, cur)

            if cur == 1:
                ans += 1
                cur = num

        return ans
    
print(Solution().minimumSplits([17779020,6955041,5516067,479658,3677378])) # 