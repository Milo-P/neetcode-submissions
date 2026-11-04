class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        highest_price = prices[len(prices) - 1]
        max_profit = 0

        for i in range(len(prices) - 1, -1, -1):
            highest_price = max(prices[i], highest_price)
            max_profit = max(highest_price - prices[i], max_profit)
        
        return max_profit

            