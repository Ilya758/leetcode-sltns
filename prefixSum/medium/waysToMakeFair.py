class Solution:
    def waysToMakeFair(self, nums: list[int]) -> int:
        totalEven = sum(nums[::2])
        totalOdd = sum(nums[1::2])
        odd, even = 0, 0
        ans = 0

        for i, num in enumerate(nums):
            if i & 1:
                totalOdd -= num
            else:
                totalEven -= num

            newOdd = odd + totalEven 
            newEven = even + totalOdd

            if newOdd == newEven:
                ans += 1

            if i & 1:
                odd += num
            else:
                even += num

        return ans
        
print(Solution().waysToMakeFair([2,1,6,4]))

