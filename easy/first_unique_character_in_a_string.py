class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Step 1: Create a dictionary to count the frequency of each character
        char_count = {}
        
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        # Step 2: Iterate through the string to find the first unique character
        for index, char in enumerate(s):
            if char_count[char] == 1:
                return index
        
        # If no unique character is found, return -1
        return -1
    
# TASK 387
# Runtime 113 ms / Memory 17.05 mb

# Example usage:
solution = Solution()
print(solution.firstUniqChar("leetcode"))       # Output: 0
print(solution.firstUniqChar("loveleetcode"))   # Output: 2
print(solution.firstUniqChar("aabb"))           # Output: -1

