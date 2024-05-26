class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0


# Runtime 38 ms / Memory 16.60 mb


# Examples to test the function
solution = Solution()

# Example 1
n1 = 4
print(f"Can win with {n1} stones: {solution.canWinNim(n1)}")  # Output: False

# Example 2
n2 = 1
print(f"Can win with {n2} stones: {solution.canWinNim(n2)}")  # Output: True

# Example 3
n3 = 2
print(f"Can win with {n3} stones: {solution.canWinNim(n3)}")  # Output: True

# Example 4 (Additional Example)
n4 = 5
print(f"Can win with {n4} stones: {solution.canWinNim(n4)}")  # Output: True

# Example 5 (Additional Example)
n5 = 8
print(f"Can win with {n5} stones: {solution.canWinNim(n5)}")  # Output: False
