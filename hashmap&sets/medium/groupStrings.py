from collections import defaultdict


class Solution:
    def groupStrings(self, strings: list[str]) -> list[list[str]]:
        cache = defaultdict(list)

        for s in strings:
            key = []

            for i in range(1, len(s)):
                a, b = ord(s[i - 1]), ord(s[i])

                if a < b:
                    key.append(str(b - a))
                else:
                    key.append(str(b + ord('z') - 96 - a))

            cache['-'.join(key)].append(s)

        return cache.values()
    
print(Solution().groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"])) # [['abc', 'bcd', 'xyz'], ['acef'], ['az', 'ba'], ['a', 'z']]