class Solution:
    def isArraySpecial(self, nums: list[int], queries: list[list[int]]) -> list[bool]:
        pairs = []
        prev = 0
        n = len(nums)

        for i in range(1, n):
            if (nums[i] ^ nums[i - 1]) & 1 == 0:
                pairs.append([prev, i - 1])
                prev = i

        pairs.append([prev, n - 1])

        def check(x):
            left, right = 0, len(pairs) - 1

            while left <= right:
                mid = (left + right) >> 1
                A, B = pairs[mid]
                
                if A <= x <= B:
                    return mid
                if x > B:
                    left = mid + 1
                else:
                    right = mid - 1
                
            return left

        return [check(a) == check(b) for a, b in queries]

print(Solution().isArraySpecial([3,4,1,2,6], [[0, 3]])) # True