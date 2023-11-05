class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummy = ListNode(-1, list1)
        left = None
        right = None
        c = 0

        while list1 and (not left or not right):
            c += 1

            if c == a: left = list1
            if c == b: right = list1.next.next

            list1 = list1.next

        if left: left.next = list2

        while list2.next: list2 = list2.next

        list2.next = right

        return dummy.next