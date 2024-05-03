class Solution:
    def compareVersion(self, A: str, B: str) -> int:
        x = [int(t) for t in A.split('.')]
        y = [int(t) for t in B.split('.')]
        i = 0
        a, b = len(x), len(y)

        while i < a or i < b:
            diff = (x[i] if i < a else 0) - (y[i] if i < b else 0) 

            if diff:
                return 1 if diff > 0 else -1

            i += 1

        return 0

print(Solution().compareVersion(A = "1.0.5", B = "1.1")) # 1