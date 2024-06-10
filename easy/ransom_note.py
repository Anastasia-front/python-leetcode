from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Count the frequency of each letter in both ransomNote and magazine
        ransom_counter = Counter(ransomNote)
        magazine_counter = Counter(magazine)

        # Check if the magazine contains enough of each letter to form the ransom note
        for letter, count in ransom_counter.items():
            if magazine_counter[letter] < count:
                return False

        return True


# TASK 383
# Runtime 54 ms / Memory 16.72 mb

# Example usage:
solution = Solution()
print(solution.canConstruct("a", "b"))  # Output: False
print(solution.canConstruct("aa", "ab"))  # Output: False
print(solution.canConstruct("aa", "aab"))  # Output: True
