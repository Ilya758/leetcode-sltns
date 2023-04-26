# https://leetcode.com/problems/add-digits/description/

def addDigits(num: int) -> int:
    return 1 + (num - 1) % 9 if num else 0


print(addDigits(38))  # 0
print(addDigits(0))  # 0
