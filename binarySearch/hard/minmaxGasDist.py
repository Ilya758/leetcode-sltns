class Solution:
    def minmaxGasDist(self, stations: list[int], k: int) -> float:
        left, right = 0, 10**8

        def get(x):
            res = 0

            for i in range(1, len(stations)):
                res += int((stations[i] - stations[i - 1]) / x)

            return res <= k

        while right - left > 10**-6:
            mid = (left + right) / 2  

            if get(mid):
                right = mid
            else:
                left = mid

        return left 

print(Solution().minmaxGasDist([1,2,3,4,5,6,7,8,9,10], 9)) # 0.5