# The isBadVersion API is already defined for you.
# Mock implementation for testing purposes
def isBadVersion(version: int) -> bool:
    # Let's assume the bad version is set for testing
    bad_version = 4  # Replace this with the actual bad version you want to test against
    return version >= bad_version


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n

        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left


# Runtime 41 ms / Memory 16.42 mb
