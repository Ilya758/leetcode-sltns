class Solution:
    def twoSumLessThanK(self, nums: list[int], k: int) -> int:
        nums.sort()
        ans = -1
        n = len(nums)

        for i in range(len(nums)):
            if nums[i] >= k:
                break

            left, right = i + 1, n

            while left < right:
                mid = (left + right) >> 1
                diff = nums[i] + nums[mid]

                if diff >= k:
                    right = mid
                else:
                    left = mid + 1
                    ans = max(ans, diff)
            
        return ans


print(Solution().twoSumLessThanK([254,914,110,900,147,441,209,122,571,942,136,350,160,127,178,839,201,386,462,45,735,467,153,415,875,282,204,534,639,994,284,320,865,468,1,838,275,370,295,574,309,268,415,385,786,62,359,78,854,944], 200)) # 198