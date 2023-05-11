class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        nums.sort()
        ptr = nums[0]
        ans = 1

        for i in range(1, len(nums)):
            if nums[i] - ptr > k:
                ptr = nums[i]
                ans += 1

        return ans


print(Solution().partitionArray(nums=[3, 6, 1, 2, 5], k=2))  # 2
print(Solution().partitionArray(nums=[1, 2, 3], k=1))  # 2
