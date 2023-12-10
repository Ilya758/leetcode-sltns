class Solution:
    def specialArray(self, nums: list[int]) -> int:
        def check(k):
            res = 0
            
            for num in nums:
                if num >= k:
                    res += 1
                    
            return res

        left, right = 0, len(nums)

        while left <= right:
            mid = (left + right) >> 1
            res = check(mid)
            
            if mid == res:
                return mid
            elif res > mid:
                left = mid + 1
            else: 
                right = mid - 1
            
        return -1

print(Solution().specialArray(nums = [0,4,3,0,4]))