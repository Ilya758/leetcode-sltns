class Solution:
    def earliestFullBloom(self, plantTime, growTime):
        flowers = sorted(zip(plantTime, growTime), key=lambda x: [-x[1], x[0]])
        ans, passed = 0, 0

        for p, g in flowers:
            ans = max(ans, passed + p + g)
            passed += p
            
        return ans
    
print(Solution().earliestFullBloom(plantTime = [1,4,3], growTime = [2,3,1])) # 9