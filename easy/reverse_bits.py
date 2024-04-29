class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result = (result << 1) | (
                n & 1
            )  # Shift result to the left and add the LSB of n
            n >>= 1  # Shift n to the right
        return result


# Runtime 36 ms / Memory 16.5 mb

solution = Solution()
print(solution.reverseBits(0b00000010100101000001111010011100))  # Output: 964176192
print(solution.reverseBits(0b11111111111111111111111111111101))  # Output: 3221225471
