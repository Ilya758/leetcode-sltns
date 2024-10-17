class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        n = len(s)
        indexes = [0] * (n)
        indexes[n - 1] = n - 1
        
        for i in range(n - 2, -1, -1):
            indexes[i] = (
                i
                if s[i] > s[indexes[i + 1]]
                else indexes[i + 1]
            )

        for i in range(n):
            if s[i] < s[indexes[i]]:
                s[i], s[indexes[i]] = s[indexes[i]], s[i]

                return int(''.join(s))

        return num

print(Solution().maximumSwap(2736)) # 7236