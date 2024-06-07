from collections import Counter
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Count the occurrences of each element in nums1
        counts = Counter(nums1)

        # List to store the result
        result = []

        # Iterate through nums2 and find intersections
        for num in nums2:
            if counts[num] > 0:
                result.append(num)
                counts[num] -= 1

        return result


# Runtime 49 ms / Memory 16.61 mb


# Example usage:
solution = Solution()
print(solution.intersect([1, 2, 2, 1], [2, 2]))  # Output: [2, 2]
print(solution.intersect([4, 9, 5], [9, 4, 9, 8, 4]))  # Output: [4, 9] or [9, 4]


# Runtime 46 ms / Memory 16.59 mb


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        result = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                result.append(nums1[i])
                i += 1
                j += 1

        return result
