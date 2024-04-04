from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 0:
            return []

        triangle = [[1]]  # Initialize Pascal's triangle with the first row

        # Generate subsequent rows
        for i in range(1, numRows):
            prev_row = triangle[-1]  # Get the previous row
            new_row = [1]  # First element of each row is always 1

            # Calculate each element of the current row
            for j in range(1, i):
                new_row.append(prev_row[j - 1] + prev_row[j])

            new_row.append(1)  # Last element of each row is always 1
            triangle.append(new_row)  # Add the new row to the triangle

        return triangle


# Runtime 38 ms / Memory 16.69 mb
