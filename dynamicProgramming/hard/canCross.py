from functools import cache


class Solution:
    def canCross(self, stones: list[int]) -> bool:
        # save the last stone
        last = stones[-1]
        # optimize look up by converting stones into a Set
        stones = set(stones)

        @cache
        def dp(cur, step):
            if cur == last:
                return True
    
            nextStep = cur + step 

            if nextStep in stones and nextStep != cur:
                if dp(nextStep, step):
                    return True

            if nextStep - 1 in stones and nextStep - 1 != cur:
                if dp(nextStep - 1, step - 1):
                    return True

            if nextStep + 1 in stones:
                if dp(nextStep + 1, step + 1):
                    return True

            return False   

        # start look up from 0, 0
        return dp(0, 0)


print(Solution().canCross(stones = [0,1,3,5,6,8,12,17])) # True
print(Solution().canCross(stones=[0, 2])) # False 