# https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = set()
        left = 0
        right = 1
        n = len(nums)
        map = dict()
        nums.sort()

        while left < n - 1:
            if -nums[right] in map:
                ans.add((nums[left], nums[right], nums[map[-nums[right]]]))
            else:
                map[nums[left] + nums[right]] = right

            right += 1

            if right == n:
                left += 1
                right = left + 1
                map.clear()

        return list(ans)


print(Solution().threeSum(nums=[-1, 0, 1, 2, -1, -4]))  # [[-1,-1,2],[-1,0,1]]
