class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if nums.count(target) != 0:
            return nums.index(target)

        if target > nums[-1]:
            return len(nums)

        for index, num in enumerate(nums):
            if target <= num:
                return index
            else:
                continue


# Runtime 47 ms / Memory 17.36 mb

solution = Solution()
result = solution.searchInsert(nums=[1, 3, 5, 6], target=5)
print(result)

result = solution.searchInsert(nums=[1, 3, 5, 6], target=2)
print(result)

result = solution.searchInsert(nums=[1, 3, 5, 6], target=7)
print(result)


# Chat GPT

def search_insert(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left


# Runtime 52 ms / Memory 17.48 mb

nums1, target1 = [1, 3, 5, 6], 5
result1 = search_insert(nums1, target1)
print(result1)  # Output: 2

nums2, target2 = [1, 3, 5, 6], 2
result2 = search_insert(nums2, target2)
print(result2)  # Output: 1

nums3, target3 = [1, 3, 5, 6], 7
result3 = search_insert(nums3, target3)
print(result3)  # Output: 4