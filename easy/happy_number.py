class Solution:
    def isHappy(self, n: int) -> bool:
        def digit_square_sum(num):
            result = 0
            while num:
                digit = num % 10
                result += digit * digit
                num //= 10
            return result

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = digit_square_sum(n)

        return n == 1


# Runtime 41 ms / Memory 16.47 mb
