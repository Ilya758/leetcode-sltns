class Solution:
    def canArrange(self, arr: list[int], k: int) -> bool:
        freq = [0] * k

        for num in arr:
            freq[num % k] += 1

        if freq[0] & 1:
            return False

        for i in range(1, k // 2 + 1):
            if freq[i] != freq[k - i]:
                return False

        return True
    
print(Solution().canArrange([1,2,3,4,5,6], 7)) # True