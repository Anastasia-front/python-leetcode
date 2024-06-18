# Given a positive integer n, you can apply one of the following operations:

# If n is even, replace n with n / 2.
# If n is odd, replace n with either n + 1 or n - 1.
# Return the minimum number of operations needed for n to become 1.


# Example 1:

# Input: n = 8
# Output: 3
# Explanation: 8 -> 4 -> 2 -> 1
# Example 2:

# Input: n = 7
# Output: 4
# Explanation: 7 -> 8 -> 4 -> 2 -> 1
# or 7 -> 6 -> 3 -> 2 -> 1
# Example 3:

# Input: n = 4
# Output: 2


# Constraints:

# 1 <= n <= 231 - 1


class Solution:
    def integerReplacement(self, n: int) -> int:
        memo = {}

        def helper(x):
            if x == 1:
                return 0
            if x in memo:
                return memo[x]

            if x % 2 == 0:
                memo[x] = 1 + helper(x // 2)
            else:
                memo[x] = 1 + min(helper(x + 1), helper(x - 1))

            return memo[x]

        return helper(n)


# Runtime 42 ms / Memory 16.61 mb


# Example usage:
solution = Solution()
print(solution.integerReplacement(8))  # Output: 3
print(solution.integerReplacement(7))  # Output: 4
print(solution.integerReplacement(4))  # Output: 2
