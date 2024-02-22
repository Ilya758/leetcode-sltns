class Solution:
    def stoneGameVI(self, A: list[int], B: list[int]) -> int:
        total = [(A[i] + B[i], A[i], B[i]) for i in range(len(A))]
        total.sort(reverse = True)
        b = sum(B)
        a = 0
        
        for i in range(0, len(A), 2):
            a += total[i][1]
            b -= total[i][2]

        if a > b:
            return 1
        elif a < b:
            return -1

        return 0
        
print(Solution().stoneGameVI([1,3], [2,1])) # 1