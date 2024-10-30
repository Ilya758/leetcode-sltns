class Solution:
    def minimumMountainRemovals(self, nums: list[int]) -> int:
        n = len(nums)
        A, B = [1] * n, [1] * n

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    A[i] = max(A[i], A[j] + 1)

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[i] > nums[j]:
                    B[i] = max(B[i], B[j] + 1)

        ans = float('inf')

        for i in range(n):
            a, b = A[i], B[i]

            if a > 1 and b > 1:
                ans = min(ans, n - a - b + 1)

        return ans
    
print(Solution().minimumMountainRemovals(nums = [2,1,1,5,6,2,3,1])) # 3