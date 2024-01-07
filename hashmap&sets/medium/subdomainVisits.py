from collections import defaultdict


class Solution:
    def subdomainVisits(self, cpdomains: list[str]) -> list[str]:
        cache = defaultdict(int)
        ans = []

        for domain in cpdomains:
            c, d = domain.split(' ')
            entries = d.split('.')

            for i in range(len(entries)):
                entry = '.'.join(entries[i:])
                cache[entry] += int(c)

        for k, v in cache.items():
            ans.append(f'{v} {k}')

        return ans
    
print(Solution().subdomainVisits(cpdomains = ["9001 discuss.leetcode.com"])) # ["9001 leetcode.com","9001 discuss.leetcode.com","9001 com"]