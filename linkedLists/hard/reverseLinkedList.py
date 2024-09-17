class Solution:
    def reverseLinkedList(self, head, k):
        prev, cur = None, head

        while k:
            cur.next, prev, cur = prev, cur, cur.next
            k -= 1

        return prev
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        ptr = head

        while count < k and ptr:
            count += 1
            ptr = ptr.next

        if count == k:
            reversedHead = self.reverseLinkedList(head, k)
            head.next = self.reverseKGroup(ptr, k)
            
            return reversedHead

        return head