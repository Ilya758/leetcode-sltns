class Solution:
    def insert(self, head: 'Optional[Node]', x: int) -> 'Node':
        if not head:
            node = Node(x)
            node.next = node

            return node

        prev, cur = head, head.next
        flag = False

        while True:
            if prev.val <= x <= cur.val:
                flag = True
            elif prev.val > cur.val:
                if x >= prev.val or x <= cur.val:
                    flag = True

            if flag:
                prev.next = Node(x, cur)

                return head

            prev, cur = cur, cur.next

            if prev == head:
                break
        
        prev.next = Node(x, cur)

        return head