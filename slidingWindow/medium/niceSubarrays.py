class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        left = 0
        ans = 0
        odd = 0
        count = 0

        for right in range(len(nums)):
            num = nums[right] % 2
            odd += num
            count = 0 if num else count

            while odd == k:
                count += 1
                odd -= nums[left] % 2
                left += 1

            ans += count

        return ans


print(Solution().numberOfSubarrays(nums=[1, 1, 2, 1, 1], k=3))  # 2
print(Solution().numberOfSubarrays(nums=[2, 4, 6], k=1))  # 0
print(Solution().numberOfSubarrays(
    nums=[2, 2, 2, 1, 1, 2, 1, 2, 2, 2], k=2))  # 16
print(Solution().numberOfSubarrays(nums=[1, 1, 1, 1, 1], k=1))
