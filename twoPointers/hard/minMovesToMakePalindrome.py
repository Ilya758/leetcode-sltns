class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        i, j = 0, len(s) - 1
        s = list(s)
        ans = 0

        while i < j:
            if s[i] != s[j]:
                k = j

                while i < k and s[i] != s[k]:
                    k -= 1

                if i == k:
                    s[k], s[k + 1] = s[k + 1], s[k]
                    ans += 1
                    continue
                else:
                    while k < j:
                        s[k], s[k + 1] = s[k + 1], s[k]
                        ans += 1
                        k += 1

            i += 1
            j -= 1

        return ans
    
print(Solution().minMovesToMakePalindrome("aabb")) # 2