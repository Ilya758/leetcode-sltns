class Solution:
    def splitNum(self, num: int) -> int:
        s = list(str(num))
        s.sort()
        left = 0
        right = 0

        for i in range(len(s)):
            if i & 1:
                right = right * 10 + int(s[i])
            else:
                left = left * 10 + int(s[i])
                
        return left + right
    
print(Solution().splitNum(num = 4325)) # 59