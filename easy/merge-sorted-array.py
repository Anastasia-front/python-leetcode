class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Initialize pointers for nums1 and nums2
        p1, p2 = m - 1, n - 1
        # Initialize the pointer for the merged array
        p = m + n - 1

        # Merge nums1 and nums2 from the end
        while p1 >=  0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # If there are remaining elements in nums2, copy them to nums1
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1

        return nums1


# Runtime 81 ms / Memory 17.98 mb

solution = Solution()
nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [3, 4, 5]
m = 3
n = 3
print(solution.merge(nums1, m, nums2, n))
