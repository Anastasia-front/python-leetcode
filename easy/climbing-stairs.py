class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        # Initialize variables for the previous two steps' counts
        prev1, prev2 = 1, 2

        # Build up the solutions for larger steps
        for i in range(3, n + 1):
            current = prev1 + prev2
            prev1, prev2 = prev2, current

        return prev2


# Runtime 38 ms / Memory 16.52 mb


def climbStairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    # Initialize an array to store the number of ways to reach each step
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    # Build up the solutions for larger steps
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# Runtime 37 ms / Memory 16.54 mb

n1 = 2
print(climbStairs(n1))  # Output: 2

n2 = 3
print(climbStairs(n2))  # Output: 3
