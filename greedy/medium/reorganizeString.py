# https://leetcode.com/problems/reorganize-string/description/
from collections import Counter
from heapq import *


class Solution:
    def reorganizeString(self, s: str) -> str:
        # the idea behind the task is a possible recreation of a string,
        # by rearranging chars as the adjacents ones aren't similar;
        # this can be acheavable by placing THE MOST freq chars 
        # at the start of a string like 'aaabc' => 'abaca';
        # one thing to notice: the are vast of possible valid variations,
        # thus the task requires to return ANY valid of them, otherwise
        # an empty string

        # 1. count freq of chars, by preparing the max heap
        items = [[-freq, char] for char, freq in Counter(s).items()]
        ans = []

        # 2. create max heap
        heapify(items)

        while items:
            # 3. pop the first max freq char
            prevF, prevC = heappop(items)

            # 4. be sure if the last symbol is equal to the first in q
            if ans and ans[-1] == prevC:
                # 4.1 this means, that we don't have any 
                # available chars for rearranging
                if not items:
                    return ''

                # 4.2 otherwise use the next char in q
                nextF, nextC = heappop(items)
                
                # because we're storing negative vals, 
                # be sure we're incrementing them like
                # -2 + 1 = -1 => back to the q
                nextF += 1
                ans.append(nextC)

                # 4.3 return char in q, if the freq isn't 0
                if nextF < 0:  
                    heappush(items, [nextF, nextC])

                # 4.4 return the first elem in q we popped before
                heappush(items, [prevF, prevC])
            else:
                # 5. otherwise use this char in result string
                prevF += 1
                ans.append(prevC)
                
                # the same as in 4.3
                if prevF < 0:
                    heappush(items, [prevF, prevC])
                        
        return "".join(ans)
     
print(Solution().reorganizeString(s = "sfffp")) # 'aba