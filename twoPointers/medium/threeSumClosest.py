class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        distance = float('inf')
        n = len(nums)

        for i in range(n - 2):
            cur = target - nums[i]
            left, right = i + 1, n - 1

            while left < right:
                s = nums[left] + nums[right]

                if abs(distance) > abs(cur - s):
                    distance = cur - s
                if s == cur:
                    return target 
                if s > cur:
                    right -= 1
                else:
                    left += 1

        return target - distance


print(Solution().threeSumClosest(nums = [-1,2,1,-4], target = 1
)) # 2