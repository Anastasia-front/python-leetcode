# Runtime 50 ms / Memory 11.72 mb

class WithoutStrSolution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :returnType: bool
        """
        # Handle negative numbers (they are not palindromes)
        if x < 0:
            return False

        # Reverse the integer
        reversed_x = 0
        original_x = x

        while x > 0:
            digit = x % 10
            reversed_x = reversed_x * 10 + digit
            x //= 10

        # Check if the reversed integer is equal to the original
        return original_x == reversed_x

print("withoutStrSolution - Runtime 50 ms / Memory 11.72 mb")
withoutStrSolution = WithoutStrSolution()


print(withoutStrSolution.isPalindrome(121))  # Output: True
print(withoutStrSolution.isPalindrome(-121))  # Output: False
print(withoutStrSolution.isPalindrome(10))  # Output: False


# Runtime 48 ms / Memory 11.41 mb
class SimpleSolution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :returnType: bool
        """
        # Convert the integer to a string
        str_x = str(x)

        # Check if the string is equal to its reverse
        return str_x == str_x[::-1]


print("simpleSolution - Runtime 48 ms / Memory 11.41 mb")
simpleSolution = SimpleSolution()

result = simpleSolution.isPalindrome(1011301)
print(result)


# Runtime 46 ms / Memory 11.54 mb
class MySolution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :returnType: bool
        """
        str_x = str(x)
        rev_x = str_x[::-1]

        length = len(str_x)

        if length == 1:
            return True

        iteration = (length // 2) + 1

        for i in range(iteration):
            if str_x[i] == rev_x[i]:
                if iteration - 1 == i:
                    return True
                continue
            else:
                return False


print("MySolution - Runtime 46 ms / Memory 11.54 mb")
solution = MySolution()

result = solution.isPalindrome(101761301)
print(result)
