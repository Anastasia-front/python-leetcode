class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return (n & (n - 1)) == 0


# Runtime 21 ms / Memory 16.54 mb


# Examples
solution = Solution()

# Example 1
# Input: n = 1
# Output: true
print(solution.isPowerOfTwo(1))  # Output: True

# Example 2
# Input: n = 16
# Output: true
print(solution.isPowerOfTwo(16))  # Output: True

# Example 3
# Input: n = 3
# Output: false
print(solution.isPowerOfTwo(3))  # Output: False
