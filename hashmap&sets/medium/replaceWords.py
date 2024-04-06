from collections import defaultdict


class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        cache = defaultdict(list)

        for d in dictionary:
            cache[d[0]].append(d)

        ans = []

        for chunk in sentence.split(' '):
            if chunk[0] in cache:
                roots = cache[chunk[0]]
                cur = chunk

                for r in roots:
                    if chunk.startswith(r) and len(cur) > len(r):
                        cur = r

                ans.append(cur) 
            else:
                ans.append(chunk)

        return ' '.join(ans)
    
print(Solution().replaceWords(dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery")) # the cat was rat by the bat