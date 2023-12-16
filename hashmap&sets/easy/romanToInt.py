class Solution:
    def romanToInt(self, s: str) -> int:
        cache = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        ans = 0
        cur = ''

        for token in s:
            cur += token

            if cur not in cache:
                ans += cache[cur[:-1]]
                cur = token

        if cur in cache:
            ans += cache[cur]

        return ans


print(Solution().romanToInt("MCMXCIV"))