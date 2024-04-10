class Solution:
    def subArrayRanges(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        stack = []

        for right in range(n + 1):
            while stack and (n == right or nums[stack[-1]] >= nums[right]):
                mid = stack.pop()
                left = stack[-1] if stack else -1
                count = (right - mid) * (mid - left)
                ans -= nums[mid] * count

            stack.append(right)

        stack.clear()

        for right in range(n + 1):
            while stack and (n == right or nums[stack[-1]] <= nums[right]):
                mid = stack.pop()
                left = stack[-1] if stack else -1
                count = (right - mid) * (mid - left)
                ans += nums[mid] * count

            stack.append(right)

        return ans
    
print(Solution.subArrayRanges([3, 1])) # 5