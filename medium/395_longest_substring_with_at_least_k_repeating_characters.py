# Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.

# if no such substring exists, return 0.


# Example 1:

# Input: s = "aaabb", k = 3
# Output: 3
# Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
# Example 2:

# Input: s = "ababbc", k = 2
# Output: 5
# Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.


# Constraints:

# 1 <= s.length <= 104
# s consists of only lowercase English letters.
# 1 <= k <= 105


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) == 0 or k > len(s):
            return 0
        if k == 1:
            return len(s)

        # Frequency of each character in the string
        freq = {}
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

        # Find the first character that appears less than k times
        for char in freq:
            if freq[char] < k:
                # Split by this character and solve for each substring
                return max(self.longestSubstring(sub, k) for sub in s.split(char))

        # If no character appears less than k times, the whole string is valid
        return len(s)


# Runtime 45 ms / Memory 16.62 mb


# Example usage
solution = Solution()
print(solution.longestSubstring("aaabb", 3))  # Output: 3
print(solution.longestSubstring("ababbc", 2))  # Output: 5
