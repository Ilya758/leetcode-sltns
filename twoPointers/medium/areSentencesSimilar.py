class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        a, b = sentence1.split(), sentence2.split()

        if len(a) > len(b):
            b, a = a, b

        n, m = len(a), len(b)
        i = 0

        while i < n and a[i] == b[i]:
            i += 1

        while i < n and a[i] == b[m - n + i]:
            i += 1

        return i == n
    
print(Solution().areSentencesSimilar("My name is john", "My john")) # True