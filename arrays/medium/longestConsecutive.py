class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = set(nums)
        ans = 0

        for num in nums:
            if (num - 1) not in nums:
                c = 0

                while (c + nums) in nums:
                    c += 1

                ans = max(ans, c)

        return ans


print(Solution().longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # 9
print(Solution().longestConsecutive(
    nums=[9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]))  # 7
