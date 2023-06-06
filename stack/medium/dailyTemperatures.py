class Solution:
    def dailyTemperatures(self, temp: list[int]) -> list[int]:
        n = len(temp)
        ans = [0] * n
        stack = []

        for i, value in enumerate(temp):
            while stack and value > temp[stack[-1]]:
                j = stack.pop()
                ans[j] = i - j

            stack.append(i)

        return ans


print(Solution().dailyTemperatures(
    temp=[73, 74, 75, 71, 69, 72, 76, 73]))  # [1,1,4,2,1,1,0,0]
