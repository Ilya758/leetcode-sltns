from collections import deque


class Solution:
    def advantageCount(self, A: list[int], B: list[int]) -> list[int]:
        q = deque(sorted(A))
        ans = [-1] * len(B)

        for v, i in sorted([-v, i] for i, v in enumerate(B)):
            ans[i] = q.pop() if -v < q[-1] else q.popleft()

        return ans

print(Solution().advantageCount([2, 7, 11, 15], [1, 10, 4, 11])) # [2, 11, 7, 15]