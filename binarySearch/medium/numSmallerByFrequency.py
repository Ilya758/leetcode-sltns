class Solution:
    def numSmallerByFrequency(self, queries: list[str], words: list[str]) -> list[int]:
        def extractFrequency(w):
            min = w[0]

            for char in w:
                if char < min: min = char
            
            return w.count(min)
            
        words = sorted([extractFrequency(w) for w in words])

        def search(k):
            left, right = 0, len(words)

            while left < right:
                mid = (left + right) // 2

                if words[mid] > k: right = mid
                else: left = mid + 1

            return len(words) - left

        return [search(extractFrequency(x)) for x in queries]

print(Solution.numSmallerByFrequency(queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
)) # [1,2]