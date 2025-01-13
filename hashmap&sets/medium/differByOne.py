from collections import defaultdict


class Solution:
    def differByOne(self, words: list[str]) -> bool:
        n = len(words)
        m = len(words[0])
        cache = defaultdict(int)
        mod = 10 ** 9 + 7
        base = 256

        def getPow(pos):
            return pow(base, m - pos - 1, mod)
        
        def getHash(word):
            hash = 0

            for t in word:
                hash = (hash * base + ord(t)) % mod 

            return hash

        def collide(a, b):
            return sum(int(words[a][i] != words[b][i]) for i in range(m)) == 1

        for i in range(n):
            hash = getHash(words[i])
            cache[hash] = i

            for j in range(m):
                newHash = (hash - ord(words[i][j]) * getPow(j)) % mod

                if newHash in cache and collide(cache[newHash], i):
                    return True

                cache[newHash] = i

        return False
            
print(Solution().differByOne(["abcd","acbd", "aacd"])) # True        