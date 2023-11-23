class Solution:
    def checkArithmeticSubarrays(self, nums: list[int], l: list[int], r: list[int]) -> list[bool]:
        def check(arr):
            curMin = min(arr)
            curMax = max(arr)

            if (curMax - curMin) % (len(arr) - 1) != 0:
                return False

            diff = (curMax - curMin) / (len(arr) - 1)
            interval = set(arr)
            curr = curMin + diff

            while curr < curMax:
                if curr not in interval:
                    return False
                
                curr += diff
            
            return True

        ans = []
        
        for i in range(len(l)):
            arr = nums[l[i] : r[i] + 1]
            ans.append(check(arr))
        
        return ans
    
print(Solution().checkArithmeticSubarrays(nums = [4,6,5,9,3,7],l = [0,0,2], r = [2,3,5])) # [true,false,true]