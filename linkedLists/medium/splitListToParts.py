class Solution:
    def splitListToParts(self, head, k: int):
        n = 0
        cur = head

        while cur:
            n += 1
            cur = cur.next

        size = n // k
        mod = n % k
        ans = [size for _ in range(k)]

        for i in range(mod):
            ans[i] += 1

        cur = head

        for i in range(k):
            if cur:
                ptr = cur
                
                for j in range(ans[i] - 1):
                    cur = cur.next
                
                tmp = cur.next
                cur.next = None
                cur = tmp
                ans[i] = ptr
            else:
                ans[i] = None

        return ans
        