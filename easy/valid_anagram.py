class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # Initialize a dictionary to count character frequencies
        char_count = {}

        # Count character frequencies in string s
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        # Decrement character frequencies based on string t
        for char in t:
            if char not in char_count:
                return False
            char_count[char] -= 1
            if char_count[char] < 0:
                return False

        # Check if all character frequencies are zero
        for count in char_count.values():
            if count != 0:
                return False

        return True


# Runtime 56 ms / Memory 16.73 mb
