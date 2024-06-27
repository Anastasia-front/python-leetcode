# Given a string s represents the serialization of a nested list, implement a parser to deserialize it and return the deserialized NestedInteger.

# Each element is either an integer or a list whose elements may also be integers or other lists.


# Example 1:

# Input: s = "324"
# Output: 324
# Explanation: You should return a NestedInteger object which contains a single integer 324.
# Example 2:

# Input: s = "[123,[456,[789]]]"
# Output: [123,[456,[789]]]
# Explanation: Return a NestedInteger object containing a nested list with 2 elements:
# 1. An integer containing value 123.
# 2. A nested list containing two elements:
#     i.  An integer containing value 456.
#     ii. A nested list with one element:
#          a. An integer containing value 789


# Constraints:

# 1 <= s.length <= 5 * 104
# s consists of digits, square brackets "[]", negative sign '-', and commas ','.
# s is the serialization of valid NestedInteger.
# All the values in the input are in the range [-106, 106].


class NestedInteger:
    def __init__(self, value=None):
        if value is None:
            self.value = []
        else:
            self.value = value

    def isInteger(self):
        return isinstance(self.value, int)

    def add(self, elem):
        if not self.isInteger():
            self.value.append(elem)

    def setInteger(self, value):
        self.value = value

    def getInteger(self):
        if self.isInteger():
            return self.value
        return None

    def getList(self):
        if not self.isInteger():
            return self.value
        return None


class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if s[0] != "[":
            # Case when s is a single integer
            return NestedInteger(int(s))

        stack = []
        num = None
        negative = False

        for i in range(len(s)):
            char = s[i]
            if char == "-":
                negative = True
            elif char.isdigit():
                num = (num or 0) * 10 + int(char)
            elif char == "[":
                stack.append(NestedInteger())
            elif char in ",]":
                if num is not None:
                    if negative:
                        num = -num
                    stack[-1].add(NestedInteger(num))
                num = None
                negative = False
                if char == "]" and len(stack) > 1:
                    ni = stack.pop()
                    stack[-1].add(ni)

        return stack[0]


# Runtime 64 ms / Memory 18.13 mb


# Example usage
solution = Solution()
s1 = "324"
s2 = "[123,[456,[789]]]"
print(solution.deserialize(s1).getInteger())  # Output: 324
print(solution.deserialize(s2).getList())  # Output: NestedInteger list representation
