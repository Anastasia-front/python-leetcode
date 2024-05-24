from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastNonZeroFoundAt = 0  # Pointer for the position of the last non-zero element

        # Move all non-zero elements to the beginning of the array
        for current in range(len(nums)):
            if nums[current] != 0:
                # Swap the elements
                nums[lastNonZeroFoundAt], nums[current] = (
                    nums[current],
                    nums[lastNonZeroFoundAt],
                )
                lastNonZeroFoundAt += 1

        # After the loop, all non-zero elements are at the beginning of the array
        # and all zeros are at the end in the order they appeared


# Runtime 120 ms / Memory 17.90 mb


# Example usage:
sol = Solution()
nums = [0, 1, 0, 3, 12]
sol.moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]
