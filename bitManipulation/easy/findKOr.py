class Solution:
    def findKOr(self, nums: list[int], k: int) -> int:
        ans = 0
        
        for i in range(32):
            c = 0
            mask = 1 << i
            
            for j in nums:
                if j & mask:
                    c += 1
            
            if c >= k:
                ans |= mask
        return ans

    
print(Solution().findKOr(nums = [7,12,9,8,9,15], k = 4)) # 9