# Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

# You must write an algorithm that runs in O(n) time and uses O(1) extra space.


# Example 1:

# Input: n = 13
# Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
# Example 2:

# Input: n = 2
# Output: [1,2]


# Constraints:

# 1 <= n <= 5 * 104


from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []

        def dfs(current):
            if current > n:
                return
            result.append(current)
            for i in range(10):
                next_number = current * 10 + i
                if next_number > n:
                    break
                dfs(next_number)

        for i in range(1, 10):
            if i > n:
                break
            dfs(i)

        return result


# Runtime 83 ms / Memory 24.74 mb


# Example usage:
sol = Solution()
print(sol.lexicalOrder(13))  # Output: [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]
print(sol.lexicalOrder(2))  # Output: [1, 2]
