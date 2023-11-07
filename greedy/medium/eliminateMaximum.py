class Solution:
    def eliminateMaximum(dist: list[int], speed: list[int]) -> int:
        monsters = sorted([d / s for d, s in zip(dist, speed)])
        ans = 0
        
        while ans < len(monsters):
            if monsters[ans] > ans: ans += 1
            else: break

        return ans

print(Solution.eliminateMaximum(dist =
[3,3,5,7,7],
speed =
[1,1,4,2,2]))