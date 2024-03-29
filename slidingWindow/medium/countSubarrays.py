class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        curMax = max(nums)
        ans = 0
        n = len(nums)
        i, count = 0, 0

        for j in range(n):
            count += int(nums[j] == curMax)

            while i <= j and count == k:
                count -= int(nums[i] == curMax)
                i += 1

            ans += j - i + 1

        return n * (n + 1) // 2 - ans   
    
print(Solution().countSubarrays(nums = [1,3,2,3,3], k = 2)) # 6