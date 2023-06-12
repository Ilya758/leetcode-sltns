# https://leetcode.com/problems/summary-ranges/description/

class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        ans = []
        cur = 0
        n = len(nums)

        for i in range(1, n + 1):
            if i == n or nums[i] - 1 != nums[i - 1]:
                if (cur == i - 1):
                    ans.append(f'{nums[cur]}')
                else:
                    ans.append(f'{nums[cur]}->{nums[i - 1]}')

                cur = i
        return ans


print(Solution().summaryRanges(nums=[0, 1, 2, 4, 5, 7]))
# ["0->2","4->5","7"]
print(Solution().summaryRanges(nums=[0, 2, 3, 4, 6, 8, 9]))
# ["0","2->4","6","8->9"]
