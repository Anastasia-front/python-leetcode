from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_index = {}
        for i, num in enumerate(nums):
            if num in num_index and i - num_index[num] <= k:
                return True
            num_index[num] = i
        return False


# Runtime 462 ms / Memory 29.76 mb


# Example 1
nums1 = [1, 2, 3, 1]
k1 = 3
print(Solution().containsNearbyDuplicate(nums1, k1))  # Output: True

# Example 2
nums2 = [1, 0, 1, 1]
k2 = 1
print(Solution().containsNearbyDuplicate(nums2, k2))  # Output: True

# Example 3
nums3 = [1, 2, 3, 1, 2, 3]
k3 = 2
print(Solution().containsNearbyDuplicate(nums3, k3))  # Output: False
