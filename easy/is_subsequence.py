class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Pointers for s and t
        pointer_s, pointer_t = 0, 0
        
        # Length of s and t
        len_s, len_t = len(s), len(t)
        
        # Traverse t
        while pointer_t < len_t:
            # Check if characters match
            if pointer_s < len_s and s[pointer_s] == t[pointer_t]:
                pointer_s += 1
            pointer_t += 1
        
        # If we have traversed all characters in s
        return pointer_s == len_s

# TASK 392
# Runtime 25 ms / Memory 16.53 mb

solution = Solution()
print(solution.isSubsequence("abc", "ahbgdc"))  # Output: true
print(solution.isSubsequence("axc", "ahbgdc"))  # Output: false
