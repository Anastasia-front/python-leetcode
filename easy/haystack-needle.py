class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = 0
        length = len(needle)
        start_index = -1

        if length == 0:
            return -1

        i = 0
        while i < len(haystack):
            if index < length:
                if haystack[i] != needle[index]:
                    if start_index != -1:
                        i = start_index + 1
                        start_index = -1
                        index = 0
                    else:
                        i += 1
                else:
                    if index == 0:
                        start_index = i
                    index += 1
                    i += 1
            else:
                return start_index

        return start_index if index == length else -1


# Runtime 45 ms / Memory 16.70 mb

solution = Solution()
result = solution.strStr(haystack="sadbutsad", needle="sad")
print(result)

result1 = solution.strStr(haystack="leetcode", needle="leeto")
print(result1)

result2 = solution.strStr(haystack="hello", needle="ll")
print(result2)

result3 = solution.strStr(haystack="mississippi", needle="issip")
print(result3)


# chat GPT
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        n, m = len(haystack), len(needle)

        for i in range(n - m + 1):
            if haystack[i : i + m] == needle:
                return i

        return -1

    # Runtime 30 ms / Memory 16.56 mb
