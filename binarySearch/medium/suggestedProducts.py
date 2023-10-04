class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        products.sort()
        ans, word = [], ''

        def search(word):
            left = 0
            right = len(products) - 1

            while left < right:
                mid = (left + right) >> 1

                if products[mid] < word:
                    left = mid + 1
                else:
                    right = mid
            
            return left

        for c in searchWord:
            word += c
            i = search(word)
            ans.append([w for w in products[i:i+3] if w.startswith(word)])

        return ans
    
print(Solution().suggestedProducts(products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse")) # [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
