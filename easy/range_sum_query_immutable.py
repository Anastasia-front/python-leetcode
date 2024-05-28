# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sums = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            self.prefix_sums[i] = self.prefix_sums[i - 1] + nums[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sums[right + 1] - self.prefix_sums[left]


# Runtime 77 ms / Memory 20.10 mb


# Example usage:
nums = [-2, 0, 3, -5, 2, -1]
numArray = NumArray(nums)

# Example 1
result1 = numArray.sumRange(0, 2)  # return (-2) + 0 + 3 = 1
print(f"sumRange(0, 2): {result1}")

# Example 2
result2 = numArray.sumRange(2, 5)  # return 3 + (-5) + 2 + (-1) = -1
print(f"sumRange(2, 5): {result2}")

# Example 3
result3 = numArray.sumRange(0, 5)  # return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
print(f"sumRange(0, 5): {result3}")
