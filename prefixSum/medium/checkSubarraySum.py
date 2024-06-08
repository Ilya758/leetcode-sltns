class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        total = 0
        cache = {0: -1}

        for i in range(len(nums)):
            total = (total + nums[i]) % k
            
            if total in cache:
                if i - cache[total] > 1:
                    return True
            else: cache[total] = i

        return False
    
print(Solution().checkSubarraySum(nums=[23,2,6,4,7], k = 6)) # True