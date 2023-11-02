class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        cache = set()
        ans = 0
        n = len(nums)

        for i in range(n):
            for j in range(i, n):
                cache.add(nums[j])
                ans += len(cache) ** 2

            cache.clear()

        return ans

print(Solution().sumCounts(nums = [1,2,1])) # 15