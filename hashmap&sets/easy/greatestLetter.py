class Solution:
    def getKey(self, char):
        return ord(char) - ord('a')

    def isLowerCased(self, char):
        return char == char.lower()

    def greatestLetter(self, s: str) -> str:
        cache = [[False, False] for _ in range(26)]

        ans = -1

        for char in s:
            case = 0 if self.isLowerCased(char) else 1
            key = self.getKey(char.lower())
            cache[key][case] = True

            if cache[key][0] and cache[key][1]:
                index = ord(char.lower())

                if ans < index:
                    ans = index

        return chr(ans).upper() if ans != -1 else ''


print(Solution().greatestLetter(s="lEeTcOdE"))  # E
print(Solution().greatestLetter(s="arRAzFif"))  # R
