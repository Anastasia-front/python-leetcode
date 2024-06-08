class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 1:
            return False

        low, high = 1, num

        while low <= high:
            mid = (low + high) // 2
            square = mid * mid

            if square == num:
                return True
            elif square < num:
                low = mid + 1
            else:
                high = mid - 1

        return False


# TASK 367
# Runtime 30 ms / Memory 16.35 mb

# Example usage:
solution = Solution()
print(solution.isPerfectSquare(16))  # Output: True
print(solution.isPerfectSquare(14))  # Output: False
