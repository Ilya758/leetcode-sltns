from collections import defaultdict


class Solution:
    def killProcess(self, pid: list[int], ppid: list[int], kill: int) -> list[int]:
        cache = defaultdict(list)

        for i in range(len(pid)):
            cache[ppid[i]].append(pid[i])

        ans = [kill]
        stack = [kill]

        while stack:
            for node in cache[stack.pop()]:
                ans.append(node)
                stack.append(node)

        return ans
    
print(Solution().killProcess(pid = [1,2,3], ppid = [0,1,2], kill = 1)) # [1, 2, 3]