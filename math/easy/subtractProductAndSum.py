# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/description/

def subtractProductAndSum(n: int) -> int:
    nums: list[int] = list(map(int, str(n)))
    product = 1
    sum = 0

    for num in nums:
        product *= num
        sum += num

    return product - sum


print(subtractProductAndSum(234))  # 15
print(subtractProductAndSum(4421))  # 21
