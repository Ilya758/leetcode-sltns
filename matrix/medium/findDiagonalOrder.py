from collections import deque


class Solution:
    def findDiagonalOrder(self, nums: list[list[int]]) -> list[int]:
        queue = deque([(0, 0)])
        ans = []
        
        while queue:
            row, col = queue.popleft()
            ans.append(nums[row][col])
            
            if col == 0 and row + 1 < len(nums):
                queue.append((row + 1, col))
                
            if col + 1 < len(nums[row]):
                queue.append((row, col + 1))
        
        return ans

print(Solution().findDiagonalOrder(nums = [[1,2,3],[4,5,6],[7,8,9]]))
# [1,4,2,7,5,3,8,6,9]