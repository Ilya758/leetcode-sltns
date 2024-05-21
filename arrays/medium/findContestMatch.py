class Solution(object):
    def findContestMatch(self, n):
        team = list(map(str, range(1, n+1)))
        
        while n > 1:
            for i in range(n // 2):
                team[i] = "({},{})".format(team[i], team.pop())

            n //= 2

        return team[0]
    
print(Solution().findContestMatch(8)) # (((1,8),(4,5)),((2,7),(3,6)))