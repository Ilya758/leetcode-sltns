class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        ans = []
        
        def bt(start, path, curSum):
            if curSum == 0:
                ans.append(path[:])
                return
            if curSum < 0:
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                path.append(candidates[i])
                bt(i + 1, path, curSum - candidates[i])
                path.pop()
        
        bt(0, [], target)
        
        return ans

print(Solution().combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8))