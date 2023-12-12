class Solution:
    def semiOrderedPermutation(self, nums: list[int]) -> int:
        n = len(nums)
        left, right = nums.index(1), nums.index(n)

        return left + n - right - 1 - int(left > right)
        
print(Solution().semiOrderedPermutation(nums = [2,1,4,3])) # 2