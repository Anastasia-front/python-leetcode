class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Preprocess the string: convert to lowercase and remove non-alphanumeric characters
        cleaned_string = "".join(char.lower() for char in s if char.isalnum())

        # Check if the cleaned string is equal to its reverse
        return cleaned_string == cleaned_string[::-1]


# Runtime 39 ms / Memory 21.77 mb

s1 = "A man, a plan, a canal: Panama"
s2 = "race a car"
s3 = " "

solution = Solution()
print(solution.isPalindrome(s1))  # Output: True
print(solution.isPalindrome(s2))  # Output: False
print(solution.isPalindrome(s3))  # Output: True
