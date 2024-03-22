class Solution:
    def numSubarrayBoundedMax(self, nums: list[int], left: int, right: int) -> int:
        ans = 0
        prev = 0
        i = 0

        for j in range(len(nums)):
            cur = nums[j]

            if left <= cur <= right:
                prev = j - i + 1
                ans += prev
            elif cur < left:
                ans += prev
            else:
                prev = 0
                i = j + 1

        return ans

print(Solution().numSubarrayBoundedMax([2,1,4,3], 2, 3)) # 3