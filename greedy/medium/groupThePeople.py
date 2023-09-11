from collections import defaultdict


class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        groups = defaultdict(list)
        ans = []

        for i, v in enumerate(groupSizes):
            groups[v].append(i)

        for k, g in groups.items():
            l = int(len(g) / k)
            ans += [g[i::l] for i in range(l)]

        ans.sort(key=len)

        return ans

print(Solution().groupThePeople(groupSizes = [3,3,3,3,3,1,3]
)) # [[5],[0,1,2],[3,4,6]]