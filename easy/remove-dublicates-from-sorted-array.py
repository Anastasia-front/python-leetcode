class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        # Initialize pointers
        slow = 0

        # Iterate through the array
        for fast in range(1, len(nums)):
            # Check if the current element is different from the previous one
            if nums[fast] != nums[slow]:
                # Move the slow pointer and update the unique element
                slow += 1
                nums[slow] = nums[fast]

        # The length of the unique elements is the position of the slow pointer + 1
        return slow + 1


# Runtime 81 ms / Memory 17.98 mb

solution = Solution()
nums1 = [1, 1, 2]
k1 = solution.removeDuplicates(nums1)
print(f"Output: {k1}, nums = {nums1[:k1]}")

nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k2 = solution.removeDuplicates(nums2)
print(f"Output: {k2}, nums = {nums2[:k2]}")

nums3 = [1, 1, 1, 1, 1, 2]
k3 = solution.removeDuplicates(nums2)
print(f"Output: {k3}, nums = {nums3[:k3]}")


# '_' as string


class MySolution:
    def removeDuplicates(self, nums: list[int]) -> int:
        unique_nums_list = []
        unique_nums = set(nums)

        for num in unique_nums:
            unique_nums_list.append(num)

        if len(nums) > len(unique_nums_list):
            remainder = len(nums) - len(unique_nums_list)
            for i in range(remainder):
                unique_nums_list.append("_")
        return unique_nums_list


# Runtime 35 ms / Memory 16.66 mb
solution = MySolution()

print("Solution - Runtime 35 ms / Memory 16.66 mb")
print(solution.removeDuplicates([1, 1, 1, 1, 1, 2]))
