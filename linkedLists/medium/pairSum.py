class Solution:
    def pairSum(self, head) -> int:
        slow = head
        fast = head
        stack = []

        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        ans = float('-inf')

        while slow:
            ans = max(ans, slow.val + stack.pop())
            slow = slow.next

        return ans
