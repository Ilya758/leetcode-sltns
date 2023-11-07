class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        ans = []

        while head:
            while stack and stack[-1][1] < head.val:
                i, _ = stack.pop()
                ans[i] = head.val

            stack.append([len(ans), head.val])
            ans.append(0)
            head = head.next

        return ans