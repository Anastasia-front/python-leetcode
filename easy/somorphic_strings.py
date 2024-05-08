class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mapping_s_to_t = {}
        mapping_t_to_s = {}

        for char_s, char_t in zip(s, t):
            if char_s not in mapping_s_to_t and char_t not in mapping_t_to_s:
                mapping_s_to_t[char_s] = char_t
                mapping_t_to_s[char_t] = char_s
            elif (
                mapping_s_to_t.get(char_s) != char_t
                or mapping_t_to_s.get(char_t) != char_s
            ):
                return False

        return True


# Runtime 36 ms / Memory 16.5 mb

# Example 1
s1 = "egg"
t1 = "add"
print(Solution().isIsomorphic(s1, t1))  # Output: True

# Example 2
s2 = "foo"
t2 = "bar"
print(Solution().isIsomorphic(s2, t2))  # Output: False

# Example 3
s3 = "paper"
t3 = "title"
print(Solution().isIsomorphic(s3, t3))  # Output: True
