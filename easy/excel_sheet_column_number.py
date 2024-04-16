class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for char in columnTitle:
            result = result * 26 + (ord(char) - ord("A") + 1)
        return result


# Runtime 40 ms / Memory 16.53 mb

sol = Solution()
print(sol.titleToNumber("A"))  # Output: 1
print(sol.titleToNumber("AB"))  # Output: 28
print(sol.titleToNumber("ZY"))  # Output: 701

