# https://leetcode.com/problems/reorder-list/description/

class Solution:
    def reorderList(self, head) -> None:
        if not head or not head.next or not head.next.next:
            return

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        head2 = slow.next
        slow.next = None
        curr = head2
        prev = None
 
        while curr:
            holder = curr.next
            curr.next = prev
            prev = curr
            curr = holder
    
        curr1 = head
        curr2 = prev 
        
        while curr2:
            holder1, holder2 = curr1.next, curr2.next
            curr1.next = curr2
            curr2.next = holder1
            curr1, curr2 = holder1, holder2