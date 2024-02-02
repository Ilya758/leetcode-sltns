class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        nums = []

        def bt(num):
            if num >= low:
                if num <= high:
                    nums.append(num)
                else:
                    return

            for i in range(1, 10):
                if num % 10 + 1 == i or num == 0:
                    bt(num * 10 + i)
            
        bt(0)

        return sorted([num for num in nums if low <= num <= high])
    
print(Solution().sequentialDigits(low = 100, high = 300)) # [123,234]