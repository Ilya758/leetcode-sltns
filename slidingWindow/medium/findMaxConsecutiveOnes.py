class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        left = right = 0
        n = len(nums)

        while right < n:
            if not nums[right]:
                right += 1
                break

            right += 1

        ans = right - left
        prev = right

        while right < n:
            if not nums[right]:
                left = prev
                prev = right + 1

            ans = max(ans, right - left + 1)
            right += 1

        return ans
    
print(Solution().findMaxConsecutiveOnes([1,1,0,1])) # 4