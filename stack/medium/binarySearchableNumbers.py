class Solution:
    def binarySearchableNumbers(self, nums: list[int]) -> int:
        stack = []
        curMax = float('-inf')

        for num in nums:
            while stack and stack[-1] > num:
                stack.pop()

            if num > curMax:
                stack.append(num)
                curMax = num
                
        return len(stack)
    
print(Solution().binarySearchableNumbers([-1,5,7,9,6])) # 2