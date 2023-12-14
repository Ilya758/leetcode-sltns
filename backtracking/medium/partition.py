class Solution:
    def partition(self, s: str) -> list[list[str]]:
        ans = []
        n = len(s)

        def bt(j, count, path):
            if count == n:
                ans.append(path[:])
                return
            elif j >= n:
                return

            for k in range(j + 1, n + 1):
                if s[j:k] == s[j:k][::-1]:
                    path.append(s[j:k])
                    bt(k, count + k - j, path)
                    path.pop()

        bt(0, 0, [])

        return ans

print(Solution().partition(s = "aab")) # [["a","a","b"],["aa","b"]]
