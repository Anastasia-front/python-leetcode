from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif candidate == num:
                count += 1
            else:
                count -= 1

        # At this point, candidate is a potential majority element
        # We need to verify if it indeed appears more than n / 2 times
        count = 0
        for num in nums:
            if num == candidate:
                count += 1

        if count > len(nums) // 2:
            return candidate
        else:
            # If the majority element always exists, we'll never reach here
            return -1  # Indicating no majority element found


# Runtime 164 ms / Memory 17.97 mb

sol = Solution()
print(sol.majorityElement([3, 2, 3]))  # Output: 3
print(sol.majorityElement([2, 2, 1, 1, 1, 2, 2]))  # Output: 2
