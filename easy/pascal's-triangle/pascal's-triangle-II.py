from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]  # Initialize the first row with 1
        for i in range(1, rowIndex + 1):
            # Generate the current row based on the previous row
            # Start from the end of the row to avoid overwriting values prematurely
            for j in range(len(row) - 1, 0, -1):
                row[j] += row[j - 1]
            # Append 1 to the end of the row (it's always 1)
            row.append(1)
        return row


# Runtime 40 ms / Memory 16.51 mb

solution = Solution()
print(solution.getRow(3))  # Output: [1, 3, 3, 1]
print(solution.getRow(0))  # Output: [1]
print(solution.getRow(1))  # Output: [1, 1]
