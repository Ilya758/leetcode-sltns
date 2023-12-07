class Solution:
    def minimumSize(self, nums: list[int], maxOperations: int) -> int:
        left, right = 1, max(nums)

        def check(k):
            ops = 0

            for num in nums:
                ops += (num - 1) // k

            return ops <= maxOperations

        while left < right:
            mid = (left + right) >> 1
        
            if check(mid): right = mid
            else: left = mid + 1

        return left
    
print(Solution().minimumSize(nums = [9], maxOperations = 2)) # 3