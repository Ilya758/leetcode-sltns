class Solution:
    def circularArrayLoop(self, nums: list[int]) -> bool:
        n = len(nums)

        def move(prev, nxt):
            res = (prev + nxt) % n

            if res < 0:
                res += n

            return res

        def notACycle(prevDir, pointer):
            return prevDir != (nums[pointer] >= 0) or abs(nums[pointer] % n) == 0

        for i in range(n):
            slow = fast = i
            curDir = nums[i] >= 0

            while True:
                slow = move(slow, nums[slow])

                if notACycle(curDir, slow):
                    break

                fast = move(fast, nums[fast])
                
                if notACycle(curDir, fast):
                    break

                fast = move(fast, nums[fast])
                
                if notACycle(curDir, fast):
                    break

                if slow == fast:
                    return True

        return False
                
print(Solution().circularArrayLoop([2,-1,1,2,2])) # True