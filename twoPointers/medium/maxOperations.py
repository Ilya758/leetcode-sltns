class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        nums.sort()
        ans = 0
        i, j = 0, len(nums) - 1 

        while i < j:
            cur = nums[i] + nums[j]

            if cur == k:
                ans += 1
                i += 1
                j -= 1
            elif cur > k:
                j -= 1
            else:
                i += 1

        return ans
    
print(Solution().maxOperations(nums = [1,2,3,4], k = 5)) # 2