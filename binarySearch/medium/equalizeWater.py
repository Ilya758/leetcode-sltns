class Solution:
    def equalizeWater(self, buckets: list[int], loss: int) -> float:
        left, right = 0, max(buckets)
        loss = 1 - loss / 100

        def check(k):
            pour_in, pour_out = 0, 0
            
            for num in buckets:
                if num < k:
                    pour_in += (k - num) / loss
                else:
                    pour_out += num - k
                    
            return pour_in <= pour_out

        while right - left > 1e-5:
            mid = (left + right) / 2

            if check(mid):
                left = mid
            else:
                right = mid

        return left

print(Solution().equalizeWater(buckets = [1,2,7], loss = 80
)) # 2