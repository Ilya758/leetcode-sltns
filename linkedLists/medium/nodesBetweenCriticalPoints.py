class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> list[int]:
        nums = []
        indexes = []
        ans = [-1, -1]

        while head:
            nums.append(head.val)
            head = head.next

        for i in range(1, len(nums) - 1):
            a, b, c = nums[i-1:i+2]

            if a > b < c or a < b > c:
                indexes.append(i)

        if len(indexes) < 2:
            return ans

        ans[0] = ans[1] = indexes[-1] - indexes[0]

        for i in range(1, len(indexes)):
            ans[0] = min(ans[0], indexes[i] - indexes[i - 1])

        return ans