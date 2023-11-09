class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        dummy = ListNode(0)
        newHead = dummy

        while head:
            while stack and stack[-1] < head.val: stack.pop()

            stack.append(head.val)
            head = head.next

        for num in stack:
            newHead.next = ListNode(num)
            newHead = newHead.next

        return dummy.next
    