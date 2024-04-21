from collections import deque

class Solution:
    def continuousSubarrays(self, nums: list[int]) -> int:
        maxDeque, minDeque = deque(), deque()
        ans = left = 0

        for right in range(len(nums)):
            while maxDeque and nums[maxDeque[-1]] < nums[right]:
                maxDeque.pop()
            while minDeque and nums[minDeque[-1]] > nums[right]:
                minDeque.pop()

            maxDeque.append(right)
            minDeque.append(right)

            while nums[maxDeque[0]] - nums[minDeque[0]] > 2:
                left += 1
                
                if maxDeque[0] < left:
                    maxDeque.popleft()
                if minDeque[0] < left:
                    minDeque.popleft()

            ans += right - left + 1

        return ans


print(Solution().continuousSubarrays([5,4,2,4])) # 8