class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ans = [1] * len(nums)
        product = 1

        for i in range(0, len(nums) - 1):
            product *= nums[i]
            ans[i+1] = product

        product = 1

        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= product
            product *= nums[i]

        return ans


print(Solution().productExceptSelf(nums=[1, 2, 3, 4]))  # [24, 12, 8, 6]
