# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    print("fake API")


class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n

        while low <= high:
            mid = (low + high) // 2
            result = guess(mid)

            if result == 0:
                return mid
            elif result == -1:
                high = mid - 1
            else:
                low = mid + 1

        return -1  # Should never reach here if the input is valid


# Example usage:
# Assuming the guess API and pick value are defined elsewhere in the code.
# solution = Solution()
# print(solution.guessNumber(10))  # Output should be the picked number


# TASK 374
# Runtime 43 ms / Memory 16.38 mb
