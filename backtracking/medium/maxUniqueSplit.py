class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        
        def bt(start, seen):
            if start == n:
                return len(seen)

            res = 0

            for end in range(start + 1, n + 1):
                sub = s[start:end]

                if sub not in seen:
                    seen.add(sub)
                    res = max(res, bt(end, seen))
                    seen.remove(sub)

            return res

        return bt(0, set())

print(Solution().maxUniqueSplit('wwwzfvedwfvhsww')) # 11