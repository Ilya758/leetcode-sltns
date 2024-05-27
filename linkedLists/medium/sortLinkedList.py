class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = head
        cur = ans
        prev = None

        while cur:
            nxt = cur.next

            if prev and cur.val < 0:
                prev.next = prev.next.next
                cur.next = ans
                ans = cur
                nxt = prev.next
            else:
                prev = cur

            cur = nxt

        return ans