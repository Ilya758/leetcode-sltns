class Solution:
    def minTimeToType(self, word: str) -> int:
        ans, pointer = 0, 0

        for i in range(len(word)):
            code = ord(word[i]) - 97
            moves = 1

            if pointer < code:
                moves += min(code - pointer, 26 + pointer - code);
            else: moves += min(pointer - code, 26 + code - pointer)            

            ans += moves
            pointer = code

        return ans
    
print(Solution().minTimeToType('e')) # 9