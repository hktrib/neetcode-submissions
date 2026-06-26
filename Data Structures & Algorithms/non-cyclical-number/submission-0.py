class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()

        def sum_digits(num) -> int:
            digits = []

            while num > 0:
                last_digit = num % 10
                digits.append(last_digit)
                num = num // 10


            digit_sum = sum([digit ** 2 for digit in digits])

            return digit_sum
        
        while n not in seen:
            seen.add(n)

            n = sum_digits(n)
            if n == 1:
                return True

        
        return False

