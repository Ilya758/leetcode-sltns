class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = dummy
        total = 0
        cache = {0: dummy}

        while cur:
            total += cur.val
            cache[total] = cur
            cur = cur.next

        total = 0
        cur = dummy

        while cur:
            total += cur.val
            cur.next = cache[total].next
            cur = cur.next

        return dummy.next