class Solution:
    def minKBitFlips(self, nums: list[int], k: int) -> int:
        cur = 0  
        ans = 0  

        for i in range(len(nums)):
            if i >= k and nums[i - k] == 2:
                cur -= 1

            if (cur % 2) == nums[i]:
                if i + k > len(nums):
                    return -1

                nums[i] = 2
                cur += 1
                ans += 1

        return ans
    
print(Solution().minKBitFlips(nums = [0,1,0,1,1,1,0,1,0,1], k = 6)) # 4