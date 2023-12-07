class Solution:
    def largestOddNumber(self, num: str) -> str:
        odds = set({"1", "3", "5", "7", "9"})

        for i in range(len(num) -1, -1, -1):
          if num[i] in odds:
            return num[0:i+1]

        return ""
    
print(Solution().largestOddNumber(num = "35427")) # 35427