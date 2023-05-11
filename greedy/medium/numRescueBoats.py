class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()

        left, right = 0, len(people) - 1
        ans = 0

        while (left <= right):
            ans += 1

            if people[left] + people[right] <= limit:
                left += 1

            right -= 1
        return ans


print(Solution().numRescueBoats(people=[1, 2], limit=3))  # 1
print(Solution().numRescueBoats(people=[3, 2, 2, 1], limit=3))  # 3
