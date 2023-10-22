class Solution:
    def maximumScore(self, nums: list[int], k: int) -> int:
        n = len(nums)
        left = k
        right = k
        ans = nums[k]
        curMin = nums[k]

        while left > 0 or right < n - 1:
            if (nums[left - 1] if left else 0) < (nums[right + 1] if right < n - 1 else 0):
                right += 1
                curMin = min(curMin, nums[right])
            else:
                left -= 1
                curMin = min(curMin, nums[left])

            ans = max(ans, curMin * (right - left + 1))

        return ans    


print(Solution().maximumScore(nums = [1,4,3,7,4,5], k = 3
)) # 15