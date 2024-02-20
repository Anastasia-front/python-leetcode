class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word = s.strip().split()[-1]
        return len(last_word)


# Runtime 41 ms / Memory 16.57 mb

solution = Solution()
s = "   fly me   to   the moon  "
result = solution.lengthOfLastWord(s)
print(result)

s = "fluffy is still boy"
result = solution.lengthOfLastWord(s)
print(result)
