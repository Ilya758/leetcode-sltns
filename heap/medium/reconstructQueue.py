from collections import deque


class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        ans = deque()
        
        people.sort(key = lambda x: (-x[0], x[1]))

        for person in people:
            ans.insert(person[1], person)

        return list(ans)

print(Solution().reconstructQueue(people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]])) # [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]