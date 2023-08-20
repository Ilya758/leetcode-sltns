# https://leetcode.com/problems/finding-the-users-active-minutes/

from collections import Counter, defaultdict


class Solution:
    def findingUsersActiveMinutes(self, logs: list[list[int]], k: int) -> list[int]:
        ans = [0 for _ in range(k)]
        mapNums = defaultdict(set)

        for id, time in logs:
            mapNums[id].add(time)

        for i, v in Counter(map(len, list(mapNums.values()))).items():
            ans[i - 1] = v

        return ans


print(Solution().findingUsersActiveMinutes(
    logs=[[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]], k=5))  # [0,2,0,0,0]
