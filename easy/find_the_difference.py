class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        from collections import Counter
        
        # Count frequency of each character in both strings
        count_s = Counter(s)
        count_t = Counter(t)
        
        # Find the character with a frequency difference of one
        for char in count_t:
            if count_t[char] != count_s.get(char, 0):
                return char

# TASK 389
# Runtime 38 ms / Memory 16.62 mb
solution = Solution()
print(solution.findTheDifference("abcd", "abcde"))  # Output: "e"
print(solution.findTheDifference("", "y"))  # Output: "y"
