class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        digits_as_str = [str(d) for d in digits]
        number = "".join(digits_as_str)
        plus_one = int(number) + 1
        result = []

        for digit in str(plus_one):
            result.append(int(digit))
        return result


# Runtime 40 ms / Memory 16.39 mb

solution = Solution()
digits = [1, 2, 3]
result = solution.plusOne(digits)
print(result)

digits = [4, 3, 2, 1]
result = solution.plusOne(digits)
print(result)

digits = [9]
result = solution.plusOne(digits)
print(result)


# Example 1:

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
# Example 2:

# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].
# Example 3:

# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].


# chat GPT
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        carry = 1

        for i in range(len(digits) - 1, -1, -1):
            total = digits[i] + carry
            digits[i] = total % 10
            carry = total // 10

        if carry:
            digits.insert(0, carry)

        return digits

    # Runtime 38 ms / Memory 16.61 mb


solution = Solution()
digits = [1, 2, 3]
result = solution.plusOne(digits)
print(result)

digits = [4, 3, 2, 1]
result = solution.plusOne(digits)
print(result)

digits = [9]
result = solution.plusOne(digits)
print(result)
