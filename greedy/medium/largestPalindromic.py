# https://leetcode.com/problems/largest-palindromic-number/

from collections import Counter
from heapq import *


class Solution:
    def largestPalindromic(self, num: str) -> str:
        part = ''
        middle = ''
        heap = [[-int(k), v] for k, v in Counter(str(num)).items()]
        heapify(heap)

        while heap:
            topK, freq = heappop(heap)

            if freq - 2 >= 0:
                freq -= 2

                if (not part and int(topK)) or part:
                    part += str(-topK)

                if freq:
                    heappush(heap, [topK, freq])
            elif not middle:
                middle = str(-topK)

        ans = part + middle + part[::-1]

        return ans if ans else '0'


print(Solution().largestPalindromic(num="444947137"))  # "7449447"
print(Solution().largestPalindromic(num="00009"))  # "9"
