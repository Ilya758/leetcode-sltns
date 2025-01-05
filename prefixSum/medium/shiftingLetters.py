from itertools import accumulate


class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        n = len(s)
        events = [0] * (n + 1)

        for start, end, d in shifts:
            if d == 0:
                d = -1

            events[start] += d if d else -1
            events[end + 1] += -d if d else 1

        events = list(accumulate(events))
        prefix = [(ord(s[i]) - 97 + events[i]) % 26 for i in range(n)]
       
        return ''.join([chr(x + 97) for x in prefix])

print(Solution().shiftingLetters(s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]])) # ace