class Solution:
    def canChange(self, start: str, target: str) -> bool:
        left = right = 0
        n = len(start)

        while left < n and right < n:
            while left < n and start[left] == '_':
                left += 1

            while right < n and target[right] == '_':
                right += 1

            if left == right == n:
                return True

            if left == n or right == n or start[left] != target[right]:
                return False

            if start[left] == 'L' and left < right:
                return False
            
            if start[left] == 'R' and left > right:
                return False

            left += 1
            right += 1

        while left < n:
            if start[left] != '_':
                return False

            left += 1

        while right < n:
            if target[right] != '_':
                return False

            right += 1

        return True

print(Solution().canChange("R_L_", "__LR")) # False