class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        isFirst = False
        prev = False

        for b in bits:
            if b:
                if prev:
                    prev = False
                    isFirst = False
                else:
                    prev = True
            else:
                if prev:
                    prev = False
                    isFirst = False
                else:
                    isFirst = True

        return isFirst
    
print(Solution().isOneBitCharacter(bits = [1, 0, 0])) # True