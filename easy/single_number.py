from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result


# Test cases
solution = Solution()
nums1 = [2, 2, 1]
nums2 = [4, 1, 2, 1, 2]
nums3 = [1]

print(solution.singleNumber(nums1))  # Output: 1
print(solution.singleNumber(nums2))  # Output: 4
print(solution.singleNumber(nums3))  # Output: 1
