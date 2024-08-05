class Solution:
    def minMoves(self, rooks: list[list[int]]) -> int:
        def calc(idx):
            res = id = 0
            rooks.sort(key=lambda x:x[idx])

            for i in range(len(rooks)):
                if rooks[i][idx] == id and i == id:
                    id += 1
                else:
                    res += abs(i - rooks[i][idx])
                    id = i
                    
            return res

        return calc(0) + calc(1)
    
print(Solution().minMoves(rooks = [[0,0],[1,0],[1,1]])) # 3