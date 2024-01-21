class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {}  # Using a dictionary to store indices of numbers

        for i, num in enumerate(nums):
            complement = target - num
            print(num,complement)
            if complement in num_dict:
                # If the complement is found in the dictionary, return the indices
                print(num_dict[complement], i)
                return [num_dict[complement], i]
            else:
                # Otherwise, add the current number and its index to the dictionary
                num_dict[num] = i

        # If no solution is found
        return None
nums = [2, 7, 11, 15]
target = 9

solution = Solution()
result = solution.twoSum(nums, target)
print(result)