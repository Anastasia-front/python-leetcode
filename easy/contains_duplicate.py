from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


# Runtime 414 ms / Memory 31.98 mb

# Example 1
nums1 = [1, 2, 3, 1]
print(Solution().containsDuplicate(nums1))  # Output: True

# Example 2
nums2 = [1, 2, 3, 4]
print(Solution().containsDuplicate(nums2))  # Output: False

# Example 3
nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print(Solution().containsDuplicate(nums3))  # Output: True
