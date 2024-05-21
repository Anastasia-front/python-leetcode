class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        for factor in [2, 3, 5]:
            while n % factor == 0:
                n //= factor

        return n == 1


# Runtime 29 ms / Memory 16.75 mb


# Example usage:
solution = Solution()

# Example 1:
n1 = 6
print(f"Is {n1} an ugly number? {solution.isUgly(n1)}")  # Output: True
# Explanation: 6 = 2 × 3

# Example 2:
n2 = 1
print(f"Is {n2} an ugly number? {solution.isUgly(n2)}")  # Output: True
# Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.

# Example 3:
n3 = 14
print(f"Is {n3} an ugly number? {solution.isUgly(n3)}")  # Output: False
# Explanation: 14 is not ugly since it includes the prime factor 7.

# Additional Example 4:
n4 = 8
print(f"Is {n4} an ugly number? {solution.isUgly(n4)}")  # Output: True
# Explanation: 8 = 2 × 2 × 2

# Additional Example 5:
n5 = 30
print(f"Is {n5} an ugly number? {solution.isUgly(n5)}")  # Output: True
# Explanation: 30 = 2 × 3 × 5

# Additional Example 6:
n6 = -6
print(f"Is {n6} an ugly number? {solution.isUgly(n6)}")  # Output: False
# Explanation: Negative numbers are not considered ugly numbers.
