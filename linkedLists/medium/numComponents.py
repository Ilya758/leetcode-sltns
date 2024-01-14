class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        vals = []

        while head:
            vals.append(head.val)
            head = head.next

        ans = 0
        cache = { x: 1 for x in nums }
        connected = False

        for left in range(len(vals)):
            if not cache:
                break

            if vals[left] in cache:
                if not connected:
                    connected = True
                    ans += 1

                del cache[vals[left]]
            else:
                connected = False

        return ans