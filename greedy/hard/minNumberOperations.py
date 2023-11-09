class Solution:
    def minNumberOperations(self, target: list[int]) -> int:
        ans = target[0]
        curMax = target[0]

        for i in range(1, len(target)):
            num = target[i]

            if curMax < num: ans += num - curMax 

            curMax = num
        
        return ans
    
print(Solution().minNumberOperations([1,3,5,7,9])) # 9