from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum


# Runtime 111 ms / Memory 17.76 mb

nums = [3, 0, 1]
solution = Solution()
print(solution.missingNumber(nums))  # Output: 2
nums = [0, 1]
solution = Solution()
print(solution.missingNumber(nums))  # Output: 2
nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
solution = Solution()
print(solution.missingNumber(nums))  # Output: 8
