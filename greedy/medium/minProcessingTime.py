class Solution:
    def minProcessingTime(self, processorTime: list[int], tasks: list[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        ans = 0

        for i, proc in enumerate(processorTime):
            for j in range(i * 4, i * 4 + 4):
                ans = max(ans, proc + tasks[j])

        return ans
    
print(Solution().minProcessingTime(processorTime = [10,20], tasks = [2,3,1,2,5,8,4,3])) # 23