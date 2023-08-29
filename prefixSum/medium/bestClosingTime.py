class Solution:
    def bestClosingTime(self, customers: str) -> int:
        cur = total = customers.count('Y')
        ans = 0

        for j in range(len(customers)):
            total += 1 if customers[j] == 'N' else -1
            
            if total < cur:
                cur = total
                ans = j + 1

        return ans

print(Solution().bestClosingTime(customers = "YYNY")) # 2
