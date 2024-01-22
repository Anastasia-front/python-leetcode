from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        min_len = min(len(s) for s in strs)

        for i in range(min_len):
            if not all(s[i] == strs[0][i] for s in strs):
                return strs[0][:i]

        return strs[0][:min_len]

# Runtime 32 ms / Memory 16.60 mb
solution_instance = Solution()
strs1 = ["flower", "flow", "flight"]
print('check 1:')
print(solution_instance.longestCommonPrefix(strs1))  # Output: "fl"

strs2 = ["dog", "raceCar", "car"]
print('check 2:')
print(solution_instance.longestCommonPrefix(strs2))  # Output: ""
