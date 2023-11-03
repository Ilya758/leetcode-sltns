class Solution:
    def findAndReplacePattern(self, words: list[str], pattern: str) -> list[str]:
        ans = []
        cache = dict()
        matched = set()
        
        for word in words:
            isValid = True

            for i in range(len(pattern)):
                w, p = word[i], pattern[i]

                if w in cache:
                    if cache[w] != p:
                        isValid = False
                        break
                elif p in matched:
                    isValid = False
                    break
                else: 
                    cache[w] = p
                    matched.add(p)

            if isValid: ans.append(word)
            
            cache.clear()
            matched.clear()

        return ans
    
print(Solution().findAndReplacePattern(words = ["abc","deq","mee","aqq","dkd","ccc"],pattern = "abb")) # ["mee","aqq"]