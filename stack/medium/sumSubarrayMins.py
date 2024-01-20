class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        MOD = 10 ** 9 + 7
        stack = []
        n = len(arr)
        ans = 0

        for i in range(n + 1):
            while stack and (i == n or arr[stack[-1]] >= arr[i]):
                mid = stack.pop()
                left = stack[-1] if stack else -1
                right = i
                count = (mid - left) * (right - mid)
                ans = (ans + count * arr[mid]) % MOD

            stack.append(i)

        return ans


print(Solution().sumSubarrayMins([3,1,2,4])) # 17