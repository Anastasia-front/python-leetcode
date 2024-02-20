class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0

        # Iterate from the rightmost digits to the leftmost
        i, j = len(a) - 1, len(b) - 1

        while i >= 0 or j >= 0 or carry:
            # Get the digits at the current positions or 0 if already reached the beginning
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0

            # Calculate the sum and carry
            total = digit_a + digit_b + carry
            result.append(str(total % 2))
            carry = total // 2

            # Move to the next positions
            i -= 1
            j -= 1

        # Reverse the result to get the correct order
        return "".join(result[::-1])


# Runtime 39 ms / Memory 16.55 mb

solution = Solution()
result = solution.addBinary(a="11", b="1")
print(result)

result = solution.addBinary(a="1010", b="1011")
print(result)


# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"
