"""Given a string s containing just the characters 
'(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type."""


class MySolution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        dict = {"(": ")", "{": "}", "[": "]"}
        list = []

        for bracket in s:
            if bracket in dict:
                list.append(bracket)
            elif not list or dict[list.pop()] != bracket:
                return False

        return not list


# Runtime 36 ms / Memory 16.67 mb
mySolution = MySolution()

print("MySolution - Runtime 36 ms / Memory 16.67 mb")
print(mySolution.isValid("{]"))


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping:
                # Pop the top element from the stack if it is not empty,
                # otherwise assign a dummy value to handle the case of a closing bracket without a corresponding open bracket.
                top_element = stack.pop() if stack else "#"

                # Check if the popped element matches the corresponding opening bracket.
                if mapping[char] != top_element:
                    return False
            else:
                # If it is an opening bracket, push it onto the stack.
                stack.append(char)

        # If the stack is empty, all parentheses are balanced.
        return not stack


# Runtime 35 ms / Memory 16.66 mb
solution = Solution()

print("Solution - Runtime 35 ms / Memory 16.66 mb")
print(solution.isValid("{[]]}"))
