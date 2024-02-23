class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        left, right = 1, x
        result = 0

        while left <= right:
            mid = left + (right - left) // 2

            if mid * mid == x:
                return mid
            elif mid * mid < x:
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result


# Runtime 34 ms / Memory 16.64 mb

solution = Solution()
result = solution.mySqrt(4)
print(result)

result = solution.mySqrt(8)
print(result)
