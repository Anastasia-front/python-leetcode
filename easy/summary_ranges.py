from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        result = []
        start = nums[0]
        end = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == end + 1:
                end = nums[i]
            else:
                if start == end:
                    result.append(str(start))
                else:
                    result.append(f"{start}->{end}")
                start = nums[i]
                end = nums[i]

        # Add the last range
        if start == end:
            result.append(str(start))
        else:
            result.append(f"{start}->{end}")

        return result


# Runtime 41 ms / Memory 16.65 mb


# Example 1
# Input: nums = [0, 1, 2, 4, 5, 7]
# Output: ["0->2", "4->5", "7"]
nums1 = [0, 1, 2, 4, 5, 7]
print(Solution().summaryRanges(nums1))  # Output: ["0->2", "4->5", "7"]

# Example 2
# Input: nums = [0, 2, 3, 4, 6, 8, 9]
# Output: ["0", "2->4", "6", "8->9"]
nums2 = [0, 2, 3, 4, 6, 8, 9]
print(Solution().summaryRanges(nums2))  # Output: ["0", "2->4", "6", "8->9"]
