class Solution:
    def largestTriangleArea(self, points: list[list[int]]) -> float:
        n = len(points)
        ans = 0

        for i in range(n):
            a, b = points[i]

            for j in range(i + 1, n):
                c, d = points[j]

                for k in range(j + 1, n):
                    e, f = points[k]
                    area = 0.5 * abs(a*(d-f) + c*(f-b) + e*(b-d))
                    ans = max(ans, area)

        return ans

print(Solution().largestTriangleArea([[0,0],[0,1],[1,0],[0,2],[2,0]]
)) # 2