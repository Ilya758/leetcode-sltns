from collections import Counter


class Solution:
    def maxScoreWords(self, words: list[str], letters: list[str], score: list[int]) -> int:
        n = len(words)
        self.ans = 0
        map = Counter(letters)
        
        def bt(i, s):
            if i <= n:
                self.ans = max(self.ans, s)
                
                for j in range(i, n):
                    lowest = float('inf')
                    curr = s

                    for c in words[j]:
                        map[c] -= 1
                        lowest = min(lowest, map[c])
                        curr += score[ord(c) - 97]    

                    if lowest >= 0:
                        bt(j + 1, curr)
                        
                    for c in words[j]:
                        map[c] += 1

        bt(0, 0)

        return self.ans
    
print(Solution().maxScoreWords(words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
)) # 23