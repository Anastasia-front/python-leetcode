from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


# Runtime 163 ms / Memory 20.98 mb


s = ["h", "e", "l", "l", "o"]
solution = Solution()
solution.reverseString(s)
print(s)  # Output: ['o', 'l', 'l', 'e', 'h']

s = ["H", "a", "n", "n", "a", "h"]
solution.reverseString(s)
print(s)  # Output: ['h', 'a', 'n', 'n', 'a', 'H']
