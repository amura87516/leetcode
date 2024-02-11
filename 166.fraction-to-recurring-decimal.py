#
# @lc app=leetcode id=166 lang=python3
#
# [166] Fraction to Recurring Decimal
#

# @lc code=start
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        # handle negative sign
        is_negative = (numerator < 0) ^ (denominator < 0)
        sign = "-" if is_negative else ""
        numerator = -numerator if is_negative else numerator

        # get integer part
        integer = str(numerator // denominator)
        numerator %= denominator

        # Divisible
        if numerator == 0:
            return f"{sign}{integer}"

        
        # get decimal part
        decimal = ""
        cnt = 0
        remain_set = {numerator: cnt}
        while numerator:
            cnt += 1
            numerator *= 10
            decimal += str(numerator // denominator)
            numerator %= denominator

            # recurring decimal
            if numerator in remain_set:
                front = decimal[:remain_set[numerator]]
                back = decimal[remain_set[numerator]:]
                return f"{sign}{integer}.{front}({back})"
            else:
                remain_set[numerator] = cnt
        
        # finite decimal
        return f"{sign}{integer}.{decimal}"
# @lc code=end

2\n1
4\n333
1\n6
7\n22
-50\n8