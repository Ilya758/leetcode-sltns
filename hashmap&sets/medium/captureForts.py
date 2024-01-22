class Solution:
    def captureForts(self, forts: list[int]) -> int:
        f = []

        for i in range(len(forts)):
            cur = forts[i]

            if cur in [1, -1]:
                f.append([i, cur])

        ans = 0

        for i in range(1, len(f)):
            prev, cur = f[i - 1], f[i]

            if prev[1] != cur[1]:
                ans = max(ans, cur[0] - prev[0] - 1)

        return ans
    
print(Solution().captureForts(forts = [1,0,0,-1,0,0,0,0,1])) # 4