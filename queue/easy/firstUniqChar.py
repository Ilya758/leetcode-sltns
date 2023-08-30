from collections import Counter, deque


class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        q = deque()
        ans = 0

        for char in s:
            q.append(char)

            if c[q[0]] > 1:
                while q and c[q[0]] > 1:
                    q.popleft()
                    ans += 1
            elif c[q[0]] == 1:
                return ans

        return -1
        
print(Solution().firstUniqChar(s='loveleetcode')) # 2