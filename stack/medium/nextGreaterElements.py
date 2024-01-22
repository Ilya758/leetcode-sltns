class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        stack = []
        ans = [-1] * len(nums)

        for i in range(len(nums) * 2):
            while stack and nums[stack[-1]] < nums[i % len(nums)]:
                print(stack[-1], nums[i % len(nums)])
                ans[stack.pop()] = nums[i % len(nums)]

            stack.append(i % len(nums))

        return ans
    
print(Solution().nextGreaterElements([1,2,3,4,9,6,8])) # [2,3,4,9,-1,8,9]