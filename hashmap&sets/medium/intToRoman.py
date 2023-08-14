# https://leetcode.com/problems/integer-to-roman/description/

class Solution:
    def intToRoman(self, num: int) -> str:
        digits = list(map(int, list(str(num))))
        n = len(digits)
        ans = ''

        nums = {
            0: "",
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M",
        }

        for i, d in enumerate(digits):
            quant = 10 ** (n - i - 1)

            if d not in nums:
                if d > 5:
                    if d == 9:
                        ans += nums[quant] + nums[10 * quant]
                    else:
                        ans += nums[5 * quant] + \
                            "".join([nums[quant]] * (d - 5))
                else:
                    if d == 4:
                        ans += nums[quant] + nums[5 * quant]
                    else:
                        ans += "".join([nums[quant]] * d)

            else:
                ans += nums[d * quant]

        return ans


print(Solution().intToRoman(num=58))  # "LVIII"
