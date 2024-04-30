class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count


# Runtime 40 ms / Memory 16.50 mb

solution = Solution()
print(solution.hammingWeight(11))  # Output: 3
print(solution.hammingWeight(128))  # Output: 1
print(solution.hammingWeight(2147483645))  # Output: 30
