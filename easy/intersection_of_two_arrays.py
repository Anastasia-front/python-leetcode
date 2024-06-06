from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Convert both lists to sets
        set1 = set(nums1)
        set2 = set(nums2)

        # Find the intersection of the two sets
        result_set = set1.intersection(set2)

        # Convert the result set to a list and return it
        return list(result_set)


# Runtime 49 ms / Memory 16.66 mb


# Example usage:
solution = Solution()
print(solution.intersection([1, 2, 2, 1], [2, 2]))  # Output: [2]
print(solution.intersection([4, 9, 5], [9, 4, 9, 8, 4]))  # Output: [9, 4] or [4, 9]
