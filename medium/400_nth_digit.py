# Given an integer n, return the nth digit of the infinite integer sequence [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...].


# Example 1:

# Input: n = 3
# Output: 3
# Example 2:

# Input: n = 11
# Output: 0
# Explanation: The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.


# Constraints:

# 1 <= n <= 231 - 1


class Solution:
    def findNthDigit(self, n: int) -> int:
        # Initialize the digit length
        digit_length = 1
        count = 9
        start = 1

        # Find the range in which the nth digit falls
        while n > digit_length * count:
            n -= digit_length * count
            digit_length += 1
            count *= 10
            start *= 10

        # Determine the actual number in the range
        num = start + (n - 1) // digit_length

        # Find the digit within the number
        num_str = str(num)
        return int(num_str[(n - 1) % digit_length])


# Runtime 28 ms / Memory 16.46 mb


# Example usage:
solution = Solution()
print(solution.findNthDigit(3))  # Output: 3
print(solution.findNthDigit(11))  # Output: 0
