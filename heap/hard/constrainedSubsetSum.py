import heapq


class Solution:
    def constrainedSubsetSum(self, nums: list[int], k: int) -> int:
        heap = [(-nums[0], 0)]
        ans = nums[0]
        
        for i in range(1, len(nums)):
            while i - heap[0][1] > k:
                heapq.heappop(heap)

            curr = max(0, -heap[0][0]) + nums[i]
            ans = max(ans, curr)
            heapq.heappush(heap, (-curr, i))

        return ans


print(Solution().constrainedSubsetSum(nums =
[10,-2,-10,-5,20],
k =
2)) # 23