from collections import deque


class Solution:
    def maximumInvitations(self, edges: list[int]) -> int:
        n = len(edges)
        indegree = [0] * n

        for i in range(n):
            indegree[edges[i]] += 1

        q = deque([i for i in range(n) if not indegree[i]])
        depth = [1] * n

        while q:
            person = q.popleft()
            nxt = edges[person]
            depth[nxt] = max(depth[nxt], depth[person] + 1)
            indegree[nxt] -= 1

            if not indegree[nxt]:
                q.append(nxt)

        maxCycle = twoInvitations = 0

        for i in range(n):
            if indegree[i]:
                current = i
                cycle = 0

                while indegree[current]:
                    indegree[current] = 0
                    cycle += 1
                    current = edges[current]

                if cycle == 2:
                    twoInvitations += depth[i] + depth[edges[i]]
                else:
                    maxCycle = max(maxCycle, cycle)

        return max(maxCycle, twoInvitations)

print(Solution().maximumInvitations(edges = [3,0,1,4,1])) # 4