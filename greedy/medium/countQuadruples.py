from collections import defaultdict


class Solution:
    def countQuadruples(self, s, t):
        a = defaultdict(int)
        b = defaultdict(int)

        for i, x in enumerate(s):
            if x not in a:
                a[x] = i

        for i, x in enumerate(t):
            b[x] = i

        ans = 0
        curMin = float('inf')

        for x in a:
            if x in b:
                dist = a[x] - b[x] 
                if dist < curMin:
                    curMin = a[x] - b[x]
                    ans = 1
                elif dist == curMin:
                    ans += 1

        return ans
    
print(Solution().countQuadruples(firstString = "abcd", secondString = "bccda")) # 1