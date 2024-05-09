class Solution:
    def maximumCoins(self, heroes: list[int], monsters: list[int], coins: list[int]) -> list[int]:
        mc = sorted(zip(monsters, coins))
        prefix = [0]

        for i in range(len(mc)):
            prefix.append(prefix[-1] + mc[i][1])

        def search(k):
            left, right = 0, len(mc)

            while left < right:
                mid = (left + right) >> 1

                if k >= mc[mid][0]:
                    left = mid + 1
                else:
                    right = mid

            return left

        return [prefix[search(k)] for k in heroes]
    

print(Solution().maximumCoins(heroes = [1,4,2], monsters = [1,1,5,2,3], coins = [2,3,4,5,6])) # [5,16,10]