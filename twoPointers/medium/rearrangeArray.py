class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        isEven = True
        left = 0
        right = 0
        ans = []
        n = len(nums)

        while len(ans) != n:
            if isEven:
                if left < n and nums[left] >= 0:
                    ans.append(nums[left])
                    isEven = False
                left += 1
            else:
                if right < n and nums[right] <= 0:
                    ans.append(nums[right])
                    isEven = True
                right += 1

        return ans


print(Solution().rearrangeArray(
    nums=[-1, 1]))  # [3,-2,1,-5,2,-4]
print(Solution().rearrangeArray(
    nums=[3, 1, -2, -5, 2, -4]))  # [3,-2,1,-5,2,-4]
