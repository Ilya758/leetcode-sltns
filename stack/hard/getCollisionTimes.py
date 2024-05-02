class Solution:
    def getCollisionTimes(self, cars: list[list[int]]) -> list[float]:
        n = len(cars)
        ans = [-1] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and cars[i][1] <= cars[stack[-1]][1]:
                stack.pop()

            while stack:
                collisionTime = (cars[stack[-1]][0] - cars[i][0]) / (cars[i][1] - cars[stack[-1]][1])

                if collisionTime < ans[stack[-1]] or ans[stack[-1]] == -1:
                    ans[i] = collisionTime
                    break

                stack.pop()

            stack.append(i)

        return ans                    
    
print(Solution().getCollisionTimes([[1,2],[2,1],[4,3],[7,2]])) # [1.00000,-1.00000,3.00000,-1.00000]