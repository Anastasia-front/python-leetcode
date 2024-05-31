class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # Check if n is a power of two and the single 1 bit is in the correct position for a power of four
        return n > 0 and (n & (n - 1)) == 0 and (n & 0xAAAAAAAA) == 0


# Runtime 28 ms / Memory 16.52 mb


# Example usage:
sol = Solution()
print(sol.isPowerOfFour(16))  # Output: True
print(sol.isPowerOfFour(5))  # Output: False
print(sol.isPowerOfFour(1))  # Output: True
