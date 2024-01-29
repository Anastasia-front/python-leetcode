class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        if not nums:
            return 0

        result = 0
        for num in nums:
            if num != val:
                nums[result] = num
                result += 1
            else:
                continue
        return result


# Runtime 35 ms / Memory 16.66 mb
solution = Solution()
nums1 = [3, 2, 2, 3]
result = solution.removeElement(nums1, 3)
print(f"Output: {result}, nums: {nums1[:result]}")


# with return as str
class Solution:
    def removeElement(self, nums: list[int], val: int) -> str:
        filtered_nums = []
        for num in nums:
            if num != val:
                filtered_nums.append(num)
            else:
                continue
        result = [x for x in nums if x != val]
        return f"{len(filtered_nums)}, nums = {result}"


solution = Solution()
nums1 = [3, 2, 2, 3]
print(solution.removeElement(nums1, 2))
