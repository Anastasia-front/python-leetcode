class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        s = list(s)
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] not in vowels:
                left += 1
            elif s[right] not in vowels:
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        return "".join(s)


# Runtime 50 ms / Memory 17.34 mb


# Example usage:
solution = Solution()
print(solution.reverseVowels("hello"))  # Output: "holle"
print(solution.reverseVowels("leetcode"))  # Output: "leotcede"
