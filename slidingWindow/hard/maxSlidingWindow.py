# https://leetcode.com/problems/sliding-window-maximum/description/
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        # 1. we're going to use deque
        # that is the first element we treat
        # as a MAX value in current sliding window
        q = deque()
        ans = []

        for i in range(len(nums)):
            # 2. any time we see that
            # current value is more that the last
            # in queue, the last elem in queue
            # will never be a MAX and we'll remove it
            while q and nums[i] > nums[q[-1]]:
                q.pop()

            # than replace it or just append the index
            # of a current number
            q.append(i)

            # any time the window length condition
            # is broken
            if q[0] + k == i:
                # shrink it
                q.popleft()

            # at the first iteration k - 1
            # we start to fill the ans
            if i >= k - 1:
                ans.append(nums[q[0]])

        return ans


print(Solution().maxSlidingWindow(nums=[1], k=1))  # [1]
print(Solution().maxSlidingWindow(
    nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))  # [3,3,5,5,6,7]
