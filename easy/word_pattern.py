class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()  # Split the string into words

        if len(pattern) != len(words):
            return False  # If lengths do not match, return false

        # Create two dictionaries to hold the mappings
        char_to_word = {}
        word_to_char = {}

        for char, word in zip(pattern, words):
            if char in char_to_word:
                # Check if the current mapping is consistent
                if char_to_word[char] != word:
                    return False
            else:
                # Check if the word is already mapped to another character
                if word in word_to_char:
                    return False
                # Establish the new mapping
                char_to_word[char] = word
                word_to_char[word] = char

        return True


# Runtime 28 ms / Memory 16.48 mb


# Examples to test the function
solution = Solution()

# Example 1
pattern1 = "abba"
s1 = "dog cat cat dog"
print(solution.wordPattern(pattern1, s1))  # Output: True

# Example 2
pattern2 = "abba"
s2 = "dog cat cat fish"
print(solution.wordPattern(pattern2, s2))  # Output: False

# Example 3
pattern3 = "aaaa"
s3 = "dog cat cat dog"
print(solution.wordPattern(pattern3, s3))  # Output: False

# Example 4 (Additional Example)
pattern4 = "abc"
s4 = "dog cat fish"
print(solution.wordPattern(pattern4, s4))  # Output: True

# Example 5 (Additional Example)
pattern5 = "abba"
s5 = "dog dog dog dog"
print(solution.wordPattern(pattern5, s5))  # Output: False
