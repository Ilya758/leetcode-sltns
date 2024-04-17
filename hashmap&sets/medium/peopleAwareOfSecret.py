from collections import defaultdict


class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        days = 1
        q, wait = defaultdict(int), defaultdict(list)
        total = 0
        wait[days + delay] = [days, 1]

        while (wait or q) and days <= n:
            if days in q:
                total -= q.pop(days)

            if days in wait:
                i, count = wait[days]
                q[i + forget] = count
                total += count
                wait.pop(days)

            if total:
                wait[days + delay] = [days, total]    

            days += 1
        
        cur = sum(q.values()) + sum([count for _, count in wait.values()])

        return cur % (10**9 + 7)

print(Solution().peopleAwareOfSecret(n = 6, delay = 2, forget = 4)) # 5