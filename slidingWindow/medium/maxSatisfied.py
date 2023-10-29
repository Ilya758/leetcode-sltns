class Solution:
    def maxSatisfied(self, customers: list[int], grumpy: list[int], minutes: int) -> int:
        cur = 0
        left = 0
        curMax = 0
        prefix = 0

        for right in range(len(customers)):
            prefix += customers[right] if grumpy[right] == 0 else 0
            cur += customers[right] if grumpy[right] else 0
            minutes -= 1

            while minutes == 0:
                curMax = max(curMax, cur)
                cur -= customers[left] if grumpy[left] else 0
                minutes += 1
                left += 1

        return prefix + curMax
    
print(Solution().maxSatisfied(customers =
[1,0,1,2,1,1,7,5],
grumpy =
[0,1,0,1,0,1,0,1],
minutes =
3)) # 16