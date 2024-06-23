from collections import deque


class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        minQ = deque([])
        maxQ = deque([])
        left = ans = 0

        for right in range(len(nums)):
            cur = nums[right]

            while minQ and minQ[-1] > cur: minQ.pop()
            while maxQ and maxQ[-1] < cur: maxQ.pop()
            
            minQ.append(cur)
            maxQ.append(cur)

            while maxQ[0] - minQ[0] > limit:
                if maxQ[0] == nums[left]: maxQ.popleft()
                if minQ[0] == nums[left]: minQ.popleft()
                
                left += 1

            ans = max(ans, right - left + 1)

        return ans

print(Solution().longestSubarray(nums = [8,2,4,7], limit = 4)) # 2