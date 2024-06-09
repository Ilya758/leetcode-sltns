class Solution:
    def maxTurbulenceSize(self, A: list[int]) -> int:
        n = len(A)
        ans = 1
        left = 0

        def compare(a, b):
            if a == b: return 0
            return 1 if a > b else -1

        for right in range(1, n):
            x = compare(A[right - 1], A[right])

            if x == 0:
                left = right
            elif right == n - 1 or x * compare(A[right], A[right + 1]) != -1:
                ans = max(ans, right - left + 1)
                left = right

        return ans
    
print(Solution().maxTurbulenceSize([9,4,2,10,7,8,8,1,9])) # 5