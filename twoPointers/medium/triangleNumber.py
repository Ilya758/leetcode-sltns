class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        ans = 0
        nums.sort()

        for k in range(2, len(nums)):
            nxt = nums[k]
            i, j = 0, k - 1

            while i < j:
                prev, cur = nums[i], nums[j]

                if prev + cur > nxt:
                    ans += j - i
                    j -= 1
                else:
                    i += 1

        return ans
    
print(Solution().triangleNumber([2,2,3,4])) # 3