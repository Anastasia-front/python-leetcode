class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber > 0:
            columnNumber -= 1
            remainder = columnNumber % 26
            result = chr(remainder + 65) + result
            columnNumber //= 26
        return result


# Runtime 43 ms / Memory 16.51 mb

solution = Solution()

# Example 1
columnNumber = 1
# Output: "A"
print(solution.convertToTitle(columnNumber))

# Example 2
columnNumber = 28
# Output: "AB"
print(solution.convertToTitle(columnNumber))

# Example 3
columnNumber = 701
# Output: "ZY"
print(solution.convertToTitle(columnNumber))
