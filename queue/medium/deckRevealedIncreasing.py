from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:
        n = len(deck)
        q = deque(range(n))
        ans = [0] * n

        # here is the point
        # assume that we need to put the particular card
        # in order index + 2 => 0, 2, 4, 6, 
        # and maintain the order, while using queue
        for card in sorted(deck):
            ans[q.popleft()] = card

            if q:
                q.append(q.popleft())

        return ans

print(Solution().deckRevealedIncreasing(deck = [17,13,11,2,3,5,7]
)) # 