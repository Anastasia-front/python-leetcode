class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        else:
            return 1 + (num - 1) % 9


# Runtime 42 ms / Memory 16.57 mb


# Example
solution = Solution()
print(solution.addDigits(38))  # Output: 2
print(solution.addDigits(0))  # Output: 0
