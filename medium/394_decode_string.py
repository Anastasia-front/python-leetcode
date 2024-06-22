# iven an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

# The test cases are generated so that the length of the output will never exceed 105.


# Example 1:

# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# Example 2:

# Input: s = "3[a2[c]]"
# Output: "accaccacc"
# Example 3:

# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"


# Constraints:

# 1 <= s.length <= 30
# s consists of lowercase English letters, digits, and square brackets '[]'.
# s is guaranteed to be a valid input.
# All the integers in s are in the range [1, 300].


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []  # This will store characters and numbers temporarily.
        current_num = 0
        current_str = ""

        for char in s:
            if char.isdigit():
                # If the character is a digit, update the current number.
                current_num = current_num * 10 + int(char)
            elif char == "[":
                # If the character is '[', push the current number and string to stack.
                stack.append(current_str)
                stack.append(current_num)
                # Reset current string and number for new sequence.
                current_str = ""
                current_num = 0
            elif char == "]":
                # If the character is ']', pop the number and previous string from stack.
                num = stack.pop()
                prev_str = stack.pop()
                # Update the current string by repeating it 'num' times and appending to previous string.
                current_str = prev_str + num * current_str
            else:
                # If the character is a letter, just append it to the current string.
                current_str += char

        return current_str


# Runtime 30 ms / Memory 16.60 mb


# Example usage:
sol = Solution()
print(sol.decodeString("3[a]2[bc]"))  # Output: "aaabcbc"
print(sol.decodeString("3[a2[c]]"))  # Output: "accaccacc"
print(sol.decodeString("2[abc]3[cd]ef"))  # Output: "abcabccdcdcdef"
