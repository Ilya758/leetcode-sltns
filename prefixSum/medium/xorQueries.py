class Solution:
    def xorQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        ans = []
        prefix = [0, arr[0]]

        for i in range(1, len(arr)): 
            prefix.append(prefix[i] ^ arr[i])

        for left, right in queries: 
            ans.append(prefix[left] ^ prefix[right + 1])

        return ans
    
print(Solution().xorQueries(arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]])) # [2,7,14,8] 