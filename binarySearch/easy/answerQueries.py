class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        nums.sort()
        prefix = [nums[0]]
        ans = []

        for i in range(1, len(nums)):
            prefix.append(prefix[i - 1] + nums[i])

        def search(q):
            left = 0
            right = len(prefix) - 1

            while left <= right:
                mid = (right + left) // 2

                if prefix[mid] == q:
                    return mid + 1
                elif q < prefix[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            return left

        for q in queries:
            ans.append(search(q))

        return ans
                
print(Solution().answerQueries(nums = [4,5,2,1], queries = [3,10,21])) # [2,3,4]