class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1


# Runtime 52 ms / Memory 16.47 mb


# Example usage:
sol = Solution()
print(sol.isPowerOfThree(27))  # Output: True
print(sol.isPowerOfThree(0))  # Output: False
print(sol.isPowerOfThree(-1))  # Output: False
