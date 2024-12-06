class Solution:
    def expressiveWords(self, s: str, words: list[str]) -> int:
        n = len(s)

        def check(w):
            m = len(w)

            if n < m:
                return False

            left, right = 0, 0

            while left < n and right < m:
                if s[left] == w[right]:
                    prev = s[left]
                    lc = rc = 0

                    while left < n and s[left] == prev:
                        left += 1
                        lc += 1

                    while right < m and w[right] == prev:
                        right += 1
                        rc += 1

                    if lc != rc and (lc < 3 or lc < rc):
                        return False
                else:
                    return False

            return left == n and right == m
        
        return sum(check(w) for w in words)
    
print(Solution().expressiveWords("heeellooo", ["hello", "hi", "helo"])) # 1