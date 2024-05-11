class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        left, right = max(nums), sum(nums)

        def check(x):
            total = 0
            count = 1

            for num in nums:
                total += num

                if total > x:
                    total = num
                    count += 1

            return count <= k

        while left < right:
            mid = (left + right) >> 1

            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left

print(Solution().splitArray([1,4,4], 3)) # 4
