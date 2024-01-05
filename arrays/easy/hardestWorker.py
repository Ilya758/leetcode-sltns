class Solution:
    def hardestWorker(self, n: int, logs: list[list[int]]) -> int:
        ans, maxTime = logs[0]

        for i in range(1, len(logs)):
            id, curTime = logs[i]
            diff = curTime - logs[i - 1][1]

            if maxTime < diff:
                maxTime = diff
                ans = id
            elif maxTime == diff:
                ans = min(ans, id)

        return ans
    
print(Solution().hardestWorker(n = 10, logs = [[0,3],[2,5],[0,9],[1,15]])) # 1