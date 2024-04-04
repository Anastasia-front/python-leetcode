class Solution:
    def maxProfit(self, prices):
        if not prices or len(prices) < 2:
            return 0

        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)

        return max_profit


# Runtime 803 ms / Memory 27.46 mb


prices1 = [7, 1, 5, 3, 6, 4]
prices2 = [7, 6, 4, 3, 1]

solution = Solution()
print(solution.maxProfit(prices1))  # Output: 5
print(solution.maxProfit(prices2))  # Output: 0
